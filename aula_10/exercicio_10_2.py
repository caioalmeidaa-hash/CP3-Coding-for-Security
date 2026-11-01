import requests,json
from pathlib import Path
s=requests.Session();s.headers['Accept']='application/vnd.github+json';ultimo=None

def buscar(caminho,params=None):
    try:
        r=s.get('https://api.github.com'+caminho,params=params,timeout=10)
        if r.status_code in (403,429):print('Limite de requisições atingido');return None
        if r.status_code==404:print('Não encontrado');return None
        r.raise_for_status();return r.json()
    except (requests.RequestException,ValueError) as e:print('Erro:',e);return None
while True:
    op=input('1 perfil 2 repositórios 3 detalhe 4 salvar JSON 5 sair: ')
    if op=='5':break
    if op=='1':
        usuario=input('Usuário: ');ultimo=buscar('/users/'+usuario)
        if ultimo:print('Nome:',ultimo.get('name'),'Repos:',ultimo.get('public_repos'),'Seguidores:',ultimo.get('followers'))
    elif op=='2':
        usuario=input('Usuário: ');pagina=int(input('Página: ') or '1');ultimo=buscar('/users/'+usuario+'/repos',{'per_page':10,'page':pagina,'sort':'updated'})
        if ultimo:
            for x in ultimo:print(x['full_name'],'★',x['stargazers_count'])
    elif op=='3':
        repo=input('Dono/repo: ');ultimo=buscar('/repos/'+repo)
        if ultimo:print('Nome:',ultimo['full_name'],'Linguagem:',ultimo.get('language'),'Stars:',ultimo['stargazers_count'])
    elif op=='4' and ultimo is not None:
        Path('github_resultado.json').write_text(json.dumps(ultimo,ensure_ascii=False,indent=2),encoding='utf8');print('Salvo em github_resultado.json')
