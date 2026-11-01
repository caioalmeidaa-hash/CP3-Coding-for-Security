# Exercício 7.2 — Parâmetros
`GET /api/incidentes?pagina=1&tamanho=5&severidade=critica&status=aberto`
- `pagina`: inteiro a partir de 1 (padrão 1)
- `tamanho`: 1 a 100 (padrão 10)
- `severidade`: filtro exato opcional
- `status`: filtro exato opcional
Ordenação por `criado_em` decrescente. Os filtros são combinados.
