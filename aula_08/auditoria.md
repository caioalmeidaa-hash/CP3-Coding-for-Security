# Exercício 8.3 — Auditoria de código
| Falha | OWASP (classificação conforme apostila) | Correção |
|---|---|---|
| 1. SQL Injection por concatenação | A05 | `cur.execute('SELECT * FROM users WHERE nome=%s',(nome,))` |
| 2. XSS ao concatenar HTML | A05 | Template Jinja2 com autoescape, sem `safe` |
| 3. Debug em `0.0.0.0` | A02 | `debug=False`, deploy com servidor WSGI e configuração restrita |
| 4. Senha hardcoded | A04/A02 | Segredos via variáveis de ambiente/gerenciador de segredos |
| 5. Ausência de logs | A09 | Logging estruturado de acessos, falhas e alertas, sem senhas |

A mensagem genérica de falha de login evita enumeração de usuários. Não publicar dados de autenticação em logs.
