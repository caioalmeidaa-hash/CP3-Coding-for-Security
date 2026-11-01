import os
from pymongo import MongoClient

def colecao(nome):
    cliente=MongoClient(os.getenv('MONGO_URI','mongodb://localhost:27017/'),serverSelectionTimeoutMS=3000)
    cliente.admin.command('ping')
    return cliente['seguranca'][nome]

from datetime import datetime

def consultar(fonte=None,tipo=None,ip=None,desde=None):
    filtro={}
    for k,v in {'fonte':fonte,'tipo':tipo,'ip':ip}.items():
        if v is not None:filtro[k]=v
    if desde is not None:filtro['timestamp']={'$gte':desde}
    return list(colecao('eventos').find(filtro).sort('timestamp',-1))
if __name__=='__main__':
    for d in consultar(tipo='FAIL',ip='185.220.101.1'):print(d)
