import os
import mysql.connector
from mysql.connector import Error

def conectar():
    return mysql.connector.connect(host=os.getenv('MYSQL_HOST','localhost'),user=os.getenv('MYSQL_USER','root'),password=os.getenv('MYSQL_PASSWORD',''),database=os.getenv('MYSQL_DATABASE','seguranca'))

from mysql.connector import IntegrityError
con=conectar();cur=con.cursor(dictionary=True)
cur.execute('CREATE TABLE IF NOT EXISTS usuarios (id INT AUTO_INCREMENT PRIMARY KEY,nome VARCHAR(100),email VARCHAR(150) UNIQUE,nivel_acesso INT NOT NULL)');con.commit()
for nome,email,nivel in [('Carlos Silva','carlos@empresa.com',3),('Ana Costa','ana@empresa.com',5),('Bruno Lima','bruno@empresa.com',1)]:
    cur.execute('INSERT IGNORE INTO usuarios(nome,email,nivel_acesso) VALUES(%s,%s,%s)',(nome,email,nivel))
con.commit()
while True:
    op=input('1 cadastrar 2 listar 3 buscar 4 mudar nível 5 remover 6 sair: ')
    if op=='6':break
    try:
        if op=='1':
            nome,email=input('Nome: '),input('Email: ');nivel=int(input('Nível 1-5: '))
            if not 1<=nivel<=5:print('Nível inválido');continue
            cur.execute('INSERT INTO usuarios(nome,email,nivel_acesso) VALUES(%s,%s,%s)',(nome,email,nivel))
        elif op=='2':
            cur.execute('SELECT * FROM usuarios');print(*cur.fetchall(),sep='\n')
        elif op=='3':
            cur.execute('SELECT * FROM usuarios WHERE email=%s',(input('Email: '),));print(cur.fetchone())
        elif op=='4':
            email=input('Email: ');nivel=int(input('Nível 1-5: '))
            if not 1<=nivel<=5:print('Nível inválido');continue
            cur.execute('UPDATE usuarios SET nivel_acesso=%s WHERE email=%s',(nivel,email));print('Nível atualizado!' if cur.rowcount else 'Não encontrado')
        elif op=='5':cur.execute('DELETE FROM usuarios WHERE email=%s',(input('Email: '),))
        con.commit()
    except IntegrityError:con.rollback();print('Erro: email já existe')
    except ValueError:print('Digite um número válido')
cur.close();con.close()
