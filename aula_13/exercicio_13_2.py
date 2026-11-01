from llm_util import classificar
from collections import Counter
from pathlib import Path
logs=['GET /index.html ip=192.168.1.10 status=200','GET /../../etc/passwd ip=91.240.118.172 status=400','POST /login ip=185.220.101.1 status=401 (5x seguidas)']
for arquivo in ('auth.log','web_access.log'):
    p=Path(__file__).with_name(arquivo)
    if p.exists():logs+=p.read_text(encoding='utf8').splitlines()
contagem=Counter()
for log in logs:
    if not log.strip():continue
    rotulo,origem=classificar(log);contagem[rotulo]+=1;print(f'[{rotulo}] ({origem}) {log}')
print('Resumo:',dict(contagem))
