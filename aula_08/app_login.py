import os
import mysql.connector
from mysql.connector import Error

def conectar():
    return mysql.connector.connect(host=os.getenv('MYSQL_HOST','localhost'),user=os.getenv('MYSQL_USER','root'),password=os.getenv('MYSQL_PASSWORD',''),database=os.getenv('MYSQL_DATABASE','seguranca'))

from flask import Flask,request,jsonify
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime,timedelta,timezone
from collections import defaultdict
app=Flask(__name__);tentativas=defaultdict(list)
def preparar():
    c=conectar();cur=c.cursor();cur.execute('CREATE TABLE IF NOT EXISTS usuarios_login(nome VARCHAR(80) PRIMARY KEY,senha_hash VARCHAR(255) NOT NULL)')
    for nome,senha in [('admin','Cyber@2024'),('analista','S3gur4nca!')]:cur.execute('INSERT IGNORE INTO usuarios_login(nome,senha_hash) VALUES(%s,%s)',(nome,generate_password_hash(senha)))
    c.commit();c.close()
@app.post('/login')
def login():
    d=request.get_json(silent=True)
    if not isinstance(d,dict) or not d.get('usuario') or not d.get('senha'):return jsonify(erro='Campos obrigatórios'),400
    chave=request.remote_addr or 'local';agora=datetime.now(timezone.utc);tentativas[chave]=[t for t in tentativas[chave] if agora-t<timedelta(minutes=5)]
    if len(tentativas[chave])>=5:return jsonify(erro='Muitas tentativas, tente mais tarde'),429
    try:
        c=conectar();cur=c.cursor();cur.execute('SELECT senha_hash FROM usuarios_login WHERE nome=%s',(d['usuario'],));r=cur.fetchone();c.close()
    except Exception:return jsonify(erro='Serviço indisponível'),500
    if not r or not check_password_hash(r[0],d['senha']):tentativas[chave].append(agora);return jsonify(erro='Credenciais inválidas'),401
    tentativas[chave]=[];return jsonify(mensagem='Login OK')
if __name__=='__main__':preparar();app.run(port=5004,debug=False)
