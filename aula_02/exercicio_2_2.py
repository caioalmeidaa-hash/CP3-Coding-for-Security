import os
from pymongo import MongoClient

def colecao(nome):
    cliente=MongoClient(os.getenv('MONGO_URI','mongodb://localhost:27017/'),serverSelectionTimeoutMS=3000)
    cliente.admin.command('ping')
    return cliente['seguranca'][nome]

from datetime import datetime
from pathlib import Path
c=colecao('eventos'); caminho=Path(__file__).with_name('auth.log')
if not caminho.exists():raise SystemExit('Coloque seu auth.log original nesta pasta (exemplo: auth_exemplo.log).')
docs=[]
for linha in caminho.read_text(encoding='utf8').splitlines():
    partes=linha.split()
    if len(partes)<4:continue
    try: instante=datetime.strptime(' '.join(partes[:2]),'%Y-%m-%d %H:%M:%S')
    except ValueError:continue
    campos=dict(p.split('=',1) for p in partes[3:] if '=' in p)
    docs.append({'timestamp':instante,'tipo':partes[2],'fonte':'auth','ip':campos.get('ip'),'detalhes':campos})
if docs:c.insert_many(docs)
print('Total de eventos inseridos:',len(docs))
for x in c.aggregate([{'$match':{'tipo':'FAIL'}},{'$group':{'_id':'$ip','total':{'$sum':1}}},{'$sort':{'total':-1}},{'$limit':5}]):print(x['_id'],'->',x['total'],'falhas')
