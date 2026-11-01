import os
import mysql.connector
from mysql.connector import Error

def conectar():
    return mysql.connector.connect(host=os.getenv('MYSQL_HOST','localhost'),user=os.getenv('MYSQL_USER','root'),password=os.getenv('MYSQL_PASSWORD',''),database=os.getenv('MYSQL_DATABASE','seguranca'))

# Demonstração SOMENTE no banco local de laboratório, com dados fictícios.
con=conectar();cur=con.cursor(dictionary=True)
cur.execute('CREATE TABLE IF NOT EXISTS usuarios_demo (id INT AUTO_INCREMENT PRIMARY KEY,nome VARCHAR(100))')
cur.execute('DELETE FROM usuarios_demo')
cur.executemany('INSERT INTO usuarios_demo(nome) VALUES(%s)',[('Carlos',),('Ana',),('Bruno',)])
con.commit()
def buscar_inseguro(nome):
    cur.execute("SELECT * FROM usuarios_demo WHERE nome='"+nome+"'")
    return cur.fetchall()
def buscar_seguro(nome):
    cur.execute('SELECT * FROM usuarios_demo WHERE nome=%s',(nome,))
    return cur.fetchall()
entrada="' OR '1'='1"
print('[INSEGURO]',len(buscar_inseguro(entrada)),'usuários retornados')
print('[SEGURO]',len(buscar_seguro(entrada)),'usuários retornados')
con.close()
