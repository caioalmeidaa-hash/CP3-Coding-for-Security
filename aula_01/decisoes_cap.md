# Exercício 1.3 — Decisões CAP
| Cenário | Escolha | Justificativa |
|---|---|---|
| Saldo bancário | CP | Não podemos aceitar saldos divergentes. Em partição, é melhor suspender operações. |
| 500 mil eventos/min em SOC | AP | A ingestão deve continuar durante falhas de rede. Réplicas podem convergir depois. |
| Cache de tokens de sessão | AP | Cache disponível reduz interrupções, desde que haja expiração curta e revogação segura. Sessões críticas podem exigir CP. |
| Auditoria de transferências | CP | A trilha de autorização não pode divergir. Consistência é prioridade sobre disponibilidade. |
| Feed de IOCs em 5 regiões | AP | Distribuição precisa continuar mesmo em partições. Atualizações podem ser eventualmente consistentes. |
