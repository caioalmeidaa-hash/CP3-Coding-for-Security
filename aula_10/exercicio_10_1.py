import requests

def consultar(cve):
    try:
        r=requests.get('https://services.nvd.nist.gov/rest/json/cves/2.0',params={'cveId':cve},timeout=15)
        if r.status_code==404:return 'CVE não encontrada'
        r.raise_for_status();v=r.json().get('vulnerabilities',[])
        if not v:return 'CVE não encontrada'
        c=v[0]['cve'];desc=next((x['value'] for x in c.get('descriptions',[]) if x['lang']=='en'),'Sem descrição')
        metricas=c.get('metrics',{});m=next((metricas[k][0]['cvssData'] for k in ('cvssMetricV40','cvssMetricV31','cvssMetricV30','cvssMetricV2') if metricas.get(k)),{})
        return f"{c['id']}\nCVSS: {m.get('baseScore','N/D')} ({m.get('baseSeverity','N/D')})\nDescrição: {desc}"
    except requests.Timeout:return 'Timeout na consulta'
    except (requests.RequestException,ValueError,KeyError) as e:return f'Falha na consulta: {type(e).__name__}'
if __name__=='__main__':print(consultar(input('CVE [CVE-2021-44228]: ') or 'CVE-2021-44228'))
