import os
import mysql.connector
from mysql.connector import Error

def conectar():
    return mysql.connector.connect(host=os.getenv('MYSQL_HOST','localhost'),user=os.getenv('MYSQL_USER','root'),password=os.getenv('MYSQL_PASSWORD',''),database=os.getenv('MYSQL_DATABASE','seguranca'))

from flask import Flask,request,jsonify
from mysql.connector import Error,IntegrityError
app=Flask(__name__)
@app.route('/api/usuarios',methods=['GET','POST'])
def usuarios():
    try:
        con=conectar();cur=con.cursor(dictionary=True)
        try:
            cur.execute('CREATE TABLE IF NOT EXISTS usuarios_api(id INT AUTO_INCREMENT PRIMARY KEY,nome VARCHAR(100),email VARCHAR(150) UNIQUE,nivel_acesso INT)')
            if request.method=='GET':cur.execute('SELECT * FROM usuarios_api');return jsonify(cur.fetchall())
            d=request.get_json(silent=True)
            if not isinstance(d,dict) or not d.get('nome') or not d.get('email') or not isinstance(d.get('nivel_acesso'),int) or not 1<=d['nivel_acesso']<=5:return jsonify(erro='Corpo inválido'),400
            cur.execute('INSERT INTO usuarios_api(nome,email,nivel_acesso) VALUES(%s,%s,%s)',(d['nome'],d['email'],d['nivel_acesso']));con.commit();return jsonify(id=cur.lastrowid),201
        finally:cur.close();con.close()
    except IntegrityError:return jsonify(erro='email já cadastrado'),409
    except Error:return jsonify(erro='serviço indisponível'),500
@app.route('/api/usuarios/<int:id>',methods=['GET','PUT','DELETE'])
def usuario(id):
    try:
        con=conectar();cur=con.cursor(dictionary=True)
        try:
            cur.execute('SELECT * FROM usuarios_api WHERE id=%s',(id,));d=cur.fetchone()
            if not d:return jsonify(erro='Não encontrado'),404
            if request.method=='GET':return jsonify(d)
            if request.method=='DELETE':cur.execute('DELETE FROM usuarios_api WHERE id=%s',(id,));con.commit();return jsonify(mensagem='Removido')
            novo=request.get_json(silent=True)
            if not isinstance(novo,dict) or not novo.get('nome') or not novo.get('email') or not isinstance(novo.get('nivel_acesso'),int) or not 1<=novo['nivel_acesso']<=5:return jsonify(erro='Corpo inválido'),400
            cur.execute('UPDATE usuarios_api SET nome=%s,email=%s,nivel_acesso=%s WHERE id=%s',(novo['nome'],novo['email'],novo['nivel_acesso'],id));con.commit();return jsonify(mensagem='Atualizado')
        finally:cur.close();con.close()
    except IntegrityError:return jsonify(erro='email já cadastrado'),409
    except Error:return jsonify(erro='serviço indisponível'),500
if __name__=='__main__':app.run(port=5002,debug=False)
