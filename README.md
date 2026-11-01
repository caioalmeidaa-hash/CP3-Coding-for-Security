# CP3 — Coding for Security — 2º Semestre

Aqui estão as resoluções dos **30 exercícios** da seção "Exercícios" das Aulas 1, 2, 3, 4, 6, 7, 8, 10, 12 e 13 da apostila.

A Aula 11 (Docker) ficou de fora, como combinado no Teams. As Aulas 5, 9 e 14 são apresentações de checkpoint/projeto e não têm exercícios próprios na apostila.

## Como executar

1. Abra a pasta no VS Code (Python 3.11+).
2. Instale as dependências:
   ```
   py -m pip install -r requirements.txt
   ```
3. Scripts Python: `py aula_04/exercicio_4_1.py` (exemplo).
   Apps Flask: `py aula_06/app.py`.
4. Scripts SQL: abra o MySQL Shell e use
   ```
   \source C:/caminho/CP3-Coding-for-Security/aula_01/exercicio_1_1.sql
   ```

## Configuração

- **MySQL:** defina a senha no PowerShell antes de rodar (não comite senha):
  ```
  $env:MYSQL_PASSWORD='SUA_SENHA'
  ```
- **MongoDB:** a variável `MONGO_URI` usa por padrão `mongodb://localhost:27017/`.
- **OpenAI:** `OPENAI_API_KEY` é obrigatória pro chatbot (13.1) e opcional pro fallback.

## Observações

- Os exercícios com banco precisam do MySQL e/ou MongoDB rodando na máquina.
- **2.2:** pra bater as 23 ocorrências, precisa do `auth.log` original do 1º semestre. O arquivo de exemplo que deixei aqui é menor.
- **13.2:** usa logs de exemplo caso os arquivos originais não estejam disponíveis.
- **13.1:** precisa de chave de API válida e acesso ao serviço.
- Os scripts e APIs são exemplos feitos pra fins acadêmicos, não são soluções pra produção.

## Checklist de exercícios

| Exercício | Título                                          | Situação |
|-----------|-------------------------------------------------|----------|
| 1.1       | Modelagem de banco de vulnerabilidades          | Feito    |
| 1.2       | CRUD SQL completo                               | Feito    |
| 1.3       | Decisão de arquitetura com CAP                  | Feito    |
| 2.1       | CRUD de inventário de ativos                    | Feito    |
| 2.2       | Ingestão de logs do 1º semestre no MongoDB      | Feito    |
| 2.3       | Consulta com filtros avançados                  | Feito    |
| 3.1       | CRUD de usuários e permissões                   | Feito    |
| 3.2       | Prova de conceito de SQL Injection (defensivo)  | Feito    |
| 3.3       | Relatório de alertas por tipo e severidade      | Feito    |
| 4.1       | Classificador de phishing                       | Feito    |
| 4.2       | Detecção de acessos anômalos                    | Feito    |
| 4.3       | Avaliação honesta com matriz de confusão        | Feito    |
| 6.1       | API CRUD de usuários                            | Feito    |
| 6.2       | Endpoint de análise de senha                    | Feito    |
| 6.3       | API de verificação de IP em blacklist           | Feito    |
| 7.1       | API de incidentes com MongoDB                   | Feito    |
| 7.2       | Paginação e filtros                             | Feito    |
| 7.3       | API de usuários com MySQL e tratamento de erros | Feito    |
| 8.1       | Dashboard de alertas com defesa contra XSS      | Feito    |
| 8.2       | Formulário de login endurecido                  | Feito    |
| 8.3       | Auditoria de código: encontre as 5 falhas       | Feito    |
| 10.1      | Cliente para a API do NVD (CVEs)                | Feito    |
| 10.2      | Explorador da API do GitHub com menu            | Feito    |
| 10.3      | Enriquecedor de IPs com cache e rate limit      | Feito    |
| 12.1      | Pipeline de detecção com normalização           | Feito    |
| 12.2      | Torneio de algoritmos                           | Feito    |
| 12.3      | Persistência com verificação de integridade     | Feito    |
| 13.1      | Chatbot de segurança                            | Feito    |
| 13.2      | Classificador automático de logs em lote        | Feito    |
| 13.3      | Demonstração de prompt injection (defensivo)    | Feito    |
