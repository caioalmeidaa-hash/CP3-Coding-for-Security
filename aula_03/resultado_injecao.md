# Exercício 3.2 — Demonstração defensiva
Em um banco local contendo três usuários fictícios, a busca por concatenação permite que a entrada de teste altere a condição WHERE e retorne os três registros. A busca parametrizada trata a entrada como dado literal e não retorna nenhum registro. **Não utilizar concatenação SQL em produção.** O resultado deve ser confirmado executando o script local.
