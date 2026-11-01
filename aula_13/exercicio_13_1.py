import os
from openai import OpenAI
historico=[{'role':'system','content':'Você é um tutor de segurança defensiva. Responda de modo claro e seguro.'}]
print('Chatbot de segurança: digite /sair para encerrar')
while True:
    pergunta=input('Você: ').strip()
    if pergunta=='/sair':print('Assistente: Até logo!');break
    if not pergunta:continue
    historico.append({'role':'user','content':pergunta})
    try:
        if not os.getenv('OPENAI_API_KEY'):raise RuntimeError('Defina OPENAI_API_KEY para usar a API')
        r=OpenAI(timeout=15,max_retries=1).chat.completions.create(model=os.getenv('OPENAI_MODEL','gpt-4o-mini'),messages=historico)
        resposta=r.choices[0].message.content or ''
        print('Assistente:',resposta);historico.append({'role':'assistant','content':resposta})
    except Exception as e:print('Erro de API:',type(e).__name__);historico.pop()
