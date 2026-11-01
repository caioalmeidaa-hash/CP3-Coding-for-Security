import os
from pymongo import MongoClient

def colecao(nome):
    cliente=MongoClient(os.getenv('MONGO_URI','mongodb://localhost:27017/'),serverSelectionTimeoutMS=3000)
    cliente.admin.command('ping')
    return cliente['seguranca'][nome]

from pymongo.errors import DuplicateKeyError
c=colecao('ativos');c.create_index('ip',unique=True)
iniciais=[{'nome':'SRV-WEB01','tipo':'servidor','ip':'192.168.1.10','status':'ativo'},{'nome':'PC-RH03','tipo':'estacao','ip':'192.168.1.45','status':'ativo'},{'nome':'SW-CORE01','tipo':'switch','ip':'192.168.1.1','status':'inativo'}]
for item in iniciais:c.update_one({'ip':item['ip']},{'$setOnInsert':item},upsert=True)
while True:
    op=input('1 cadastrar | 2 listar | 3 buscar IP | 4 atualizar | 5 remover | 6 sair: ')
    if op=='6':break
    if op=='1':
        d={k:input(k+': ') for k in ('nome','tipo','ip','status')}
        try:c.insert_one(d);print('Ativo cadastrado!')
        except DuplicateKeyError:print('Erro: IP já cadastrado!')
    elif op=='2':
        for d in c.find({}, {'_id':0}):print(d)
    elif op=='3':print(c.find_one({'ip':input('IP: ')},{'_id':0}) or 'Não encontrado')
    elif op=='4':print('Status atualizado!' if c.update_one({'ip':input('IP: ')},{'$set':{'status':input('Novo status: ')}}).matched_count else 'Não encontrado')
    elif op=='5':print('Removidos:',c.delete_one({'ip':input('IP: ')}).deleted_count)
