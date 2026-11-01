# CP3 — Coding for Security — 2º Semestre

Resolução dos **30 exercícios** explicitamente identificados na seção "Exercícios" das Aulas 1, 2, 3, 4, 6, 7, 8, 10, 12 e 13 da apostila fornecida. **Aula 11 (Docker) excluída**, conforme Teams. Aulas 5, 9 e 14 são apresentações de checkpoints/projeto, sem exercícios próprios na apostila. Os enunciados externos dos checkpoints não foram fornecidos e não fazem parte deste pacote.

## Como executar

1. Abra esta pasta no VS Code. Use Python 3.11+.
2. `py -m pip install -r requirements.txt`
3. Scripts Python: `py aula_04/exercicio_4_1.py` (exemplo). Apps Flask: `py aula_06/app.py`.
4. Scripts SQL: use MySQL Shell com `\source C:/caminho/CP3-Coding-for-Security/aula_01/exercicio_1_1.sql`.
5. MySQL: configure no PowerShell `$env:MYSQL_PASSWORD='SUA_SENHA'` (não comite senhas). MongoDB: `MONGO_URI` padrão `mongodb://localhost:27017/`. OpenAI: `OPENAI_API_KEY` é opcional para o fallback, mas necessário para o chatbot.

## Limitações honestas

- **Não foram executados testes de integração com MySQL, MongoDB ou APIs externas** neste ambiente. Os arquivos `.py` foram verificados quanto à sintaxe.
- Exercício 2.2 requer o `auth.log` original do 1º semestre para reproduzir as contagens de 23 eventos; o exemplo incluído é menor.
- Exercício 13.2 também usa logs de exemplo se os arquivos originais não estiverem disponíveis.
- Exercício 13.1 exige uma chave de API válida e acesso ao serviço.
- Scripts e APIs são exemplos acadêmicos, não soluções de produção.

## Checklist de exercícios

| Exercício | Título | Situação |
|---|---|---|
| 1.1 | Modelagem de banco de vulnerabilidades | OK — arquivo incluído |
| 1.2 | CRUD SQL completo | OK — arquivo incluído |
| 1.3 | Decisão de arquitetura com CAP | OK — arquivo incluído |
| 2.1 | CRUD de inventário de ativos | OK — arquivo incluído |
| 2.2 | Ingestão de logs do 1º semestre no MongoDB | OK — arquivo incluído |
| 2.3 | Consulta com filtros avançados | OK — arquivo incluído |
| 3.1 | CRUD de usuários e permissões | OK — arquivo incluído |
| 3.2 | Prova de conceito de SQL Injection (defensivo) | OK — arquivo incluído |
| 3.3 | Relatório de alertas por tipo e severidade | OK — arquivo incluído |
| 4.1 | Classificador de phishing | OK — arquivo incluído |
| 4.2 | Detecção de acessos anômalos | OK — arquivo incluído |
| 4.3 | Avaliação honesta com matriz de confusão | OK — arquivo incluído |
| 6.1 | API CRUD de usuários | OK — arquivo incluído |
| 6.2 | Endpoint de análise de senha | OK — arquivo incluído |
| 6.3 | API de verificação de IP em blacklist | OK — arquivo incluído |
| 7.1 | API de incidentes com MongoDB | OK — arquivo incluído |
| 7.2 | Paginação e filtros | OK — arquivo incluído |
| 7.3 | API de usuários com MySQL e tratamento de erros | OK — arquivo incluído |
| 8.1 | Dashboard de alertas com defesa contra XSS | OK — arquivo incluído |
| 8.2 | Formulário de login endurecido | OK — arquivo incluído |
| 8.3 | Auditoria de código: encontre as 5 falhas | OK — arquivo incluído |
| 10.1 | Cliente para a API do NVD (CVEs) | OK — arquivo incluído |
| 10.2 | Explorador da API do GitHub com menu | OK — arquivo incluído |
| 10.3 | Enriquecedor de IPs com cache e rate limit | OK — arquivo incluído |
| 12.1 | Pipeline de detecção com normalização | OK — arquivo incluído |
| 12.2 | Torneio de algoritmos | OK — arquivo incluído |
| 12.3 | Persistência com verificação de integridade | OK — arquivo incluído |
| 13.1 | Chatbot de segurança | OK — arquivo incluído |
| 13.2 | Classificador automático de logs em lote | OK — arquivo incluído |
| 13.3 | Demonstração de prompt injection (defensivo) | OK — arquivo incluído |
