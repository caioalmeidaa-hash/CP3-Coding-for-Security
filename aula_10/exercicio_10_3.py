import requests,ipaddress,time,json
ips=['8.8.8.8','1.1.1.1','185.220.101.1','192.168.1.10','8.8.8.8'];cache={};stats={'http':0,'cache':0,'internos':0};relatorio=[]
for ip in ips:
    addr=ipaddress.ip_address(ip)
    if not addr.is_global:stats['internos']+=1;item={'ip':ip,'tipo':'Rede interna'}
    elif ip in cache:stats['cache']+=1;item={**cache[ip],'cache':True}
    else:
        item={'ip':ip,'tipo':'EXTERNO'}
        for tentativa in range(3):
            try:
                r=requests.get('https://ipwho.is/'+ip,timeout=8);stats['http']+=1
                if r.status_code==429:time.sleep(min(2**tentativa,4));continue
                r.raise_for_status();d=r.json();item.update(pais=d.get('country'),cidade=d.get('city'),organizacao=d.get('connection',{}).get('org'));break
            except (requests.RequestException,ValueError):item['erro']='Consulta indisponível';break
        cache[ip]=item
    print(item);relatorio.append(item)
print('Resumo:',stats)
with open('relatorio_ips.json','w',encoding='utf8') as f:json.dump({'ips':relatorio,'resumo':stats},f,ensure_ascii=False,indent=2)
