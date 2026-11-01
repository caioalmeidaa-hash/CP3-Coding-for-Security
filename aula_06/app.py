from flask import Flask,request,jsonify
import ipaddress,re
app=Flask(__name__);usuarios={};seq=1
blacklist={'185.220.101.1','45.33.32.156','91.240.118.172'}
def validar(d,atual=None):
    if not isinstance(d,dict) or not isinstance(d.get('nome'),str) or not isinstance(d.get('email'),str) or not isinstance(d.get('nivel'),int) or not 1<=d['nivel']<=5:return 'Dados inválidos ou nível inválido'
    if any(u['email']==d['email'] and i!=atual for i,u in usuarios.items()):return 'email já existe'
@app.route('/api/usuarios',methods=['GET','POST'])
def lista():
    global seq
    if request.method=='GET':return jsonify(list(usuarios.values()))
    d=request.get_json(silent=True);erro=validar(d)
    if erro:return jsonify(erro=erro),400
    u={'id':seq,**{k:d[k] for k in ('nome','email','nivel')}};usuarios[seq]=u;seq+=1;return jsonify(u),201
@app.route('/api/usuarios/<int:id>',methods=['GET','PUT','DELETE'])
def usuario(id):
    if id not in usuarios:return jsonify(erro='Não encontrado'),404
    if request.method=='GET':return jsonify(usuarios[id])
    if request.method=='DELETE':del usuarios[id];return jsonify(mensagem='Removido')
    d=request.get_json(silent=True);novo={**usuarios[id],**(d if isinstance(d,dict) else {})};erro=validar(novo,id)
    if erro:return jsonify(erro=erro),400
    usuarios[id]=novo;return jsonify(novo)
@app.post('/api/analisar-senha')
def senha():
    d=request.get_json(silent=True)
    if not isinstance(d,dict) or not isinstance(d.get('senha'),str):return jsonify(erro="campo 'senha' obrigatório"),400
    s=d['senha'];c={'tamanho_min':len(s)>=8,'maiuscula':bool(re.search('[A-Z]',s)),'minuscula':bool(re.search('[a-z]',s)),'numero':bool(re.search('[0-9]',s)),'especial':bool(re.search(r'[^A-Za-z0-9]',s))};n=sum(c.values())
    return jsonify(forca='Muito forte' if n==5 else 'Forte' if n==4 else 'Média' if n==3 else 'Fraca',criterios=c)
@app.get('/api/checar-ip/<ip>')
def ip(ip):
    try:addr=ipaddress.ip_address(ip)
    except ValueError:return jsonify(erro='IP inválido'),400
    return jsonify(ip=ip,na_blacklist=ip in blacklist,tipo='privado' if addr.is_private else 'publico')
if __name__=='__main__':app.run(port=5000,debug=False)
