import os
from pymongo import MongoClient

def colecao(nome):
    cliente=MongoClient(os.getenv('MONGO_URI','mongodb://localhost:27017/'),serverSelectionTimeoutMS=3000)
    cliente.admin.command('ping')
    return cliente['seguranca'][nome]

from flask import Flask,request,jsonify
from bson import ObjectId
from bson.errors import InvalidId
from datetime import datetime,timezone
from pymongo.errors import PyMongoError
app=Flask(__name__)
def serializar(d):
    d['_id']=str(d['_id']);return d
@app.route('/api/incidentes',methods=['GET','POST'])
def incidentes():
    try:
        c=colecao('incidentes')
        if request.method=='POST':
            d=request.get_json(silent=True)
            if not isinstance(d,dict) or not all(isinstance(d.get(k),str) and d[k] for k in ('titulo','severidade','ip_origem')):return jsonify(erro='Campos obrigatórios: titulo, severidade, ip_origem'),400
            item={k:d[k] for k in ('titulo','severidade','ip_origem')};item.update(status='aberto',criado_em=datetime.now(timezone.utc));r=c.insert_one(item);return jsonify(id=str(r.inserted_id)),201
        try:p=int(request.args.get('pagina',1));t=int(request.args.get('tamanho',10));assert p>0 and 1<=t<=100
        except (ValueError,AssertionError):return jsonify(erro='Paginação inválida'),400
        f={k:request.args[k] for k in ('severidade','status') if k in request.args}
        return jsonify([serializar(x) for x in c.find(f).sort('criado_em',-1).skip((p-1)*t).limit(t)])
    except PyMongoError:return jsonify(erro='Serviço indisponível'),503
@app.route('/api/incidentes/<id>',methods=['GET','PUT','DELETE'])
def incidente(id):
    try:oid=ObjectId(id)
    except InvalidId:return jsonify(erro='id inválido'),400
    try:
        c=colecao('incidentes');d=c.find_one({'_id':oid})
        if not d:return jsonify(erro='Não encontrado'),404
        if request.method=='GET':return jsonify(serializar(d))
        if request.method=='DELETE':c.delete_one({'_id':oid});return jsonify(mensagem='Removido')
        novo=request.get_json(silent=True)
        if not isinstance(novo,dict):return jsonify(erro='Corpo inválido'),400
        permitido={k:novo[k] for k in ('titulo','severidade','status','ip_origem') if isinstance(novo.get(k),str) and novo[k]}
        if not permitido:return jsonify(erro='Sem campos válidos'),400
        c.update_one({'_id':oid},{'$set':permitido});return jsonify(serializar(c.find_one({'_id':oid})))
    except PyMongoError:return jsonify(erro='Serviço indisponível'),503
if __name__=='__main__':app.run(port=5001,debug=False)
