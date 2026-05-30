# Explicação — Desafio 06 — Bio-Cadastro

**Aluno:** _(Guilherme)_
**Data:** _(29/05/2026)_

---

## O que meu programa faz

_(Primeiro comecei com Loop while True, criando variaveis 'nome' e 'colaborador' que recebe     valores str com input, com a condicao que caso a entrada seja 'sair' em alguns dos dois input.
caso a entrada no input esteja recebendo valores certo, o nome e cargo sera adicionado em equipe com o uso do 'append' em forma de dicionario. por ultimo quando eu encerro o loop while true, ainda tem outro loop com 'for' que percorre todos os funcionarios dentro da lista 'equipe' e printa na tela os nome dos funcionario e cargo.
)_

---

## Resposta à Pergunta Obrigatória

> Por que usamos um **dicionário** para cada funcionário e não uma lista com dois itens como `["Ricardo", "Dev"]`? Qual é a desvantagem de `funcionario[0]` comparado a `funcionario["nome"]`?

_(na minha visao, acho que fica mais simples  e facil trabalhar com chave e valor inves de usar indice/lista, acho que fica mais facil usando em forma de chave e valor)_

---

## Dificuldades encontradas

_(para minha condicao 'sair' nos dois input, tava tendo dificuldade pq tava salvando a entrada 'sair' dentro dos respectivos valores. confesso que pedi ajuda para ia, mas entendi o erro e a forma certa de se fazer. tambem pedi a explicacao kk.)_
 
eu tinha feito assim: 

equipe = []

while True:
    nome = str(input('digite seu nome: '))
    cargo = str(input('digite seu cargo'))
    if nome == 'sair' or cargo == 'sair':
        print('saindo...')
        break
    else:
        equipe.append({'nome': nome, 'cargo': cargo})
        print(f'colaborador adicionado com sucesso.')
    
for funcionario in equipe:
    print(f'Funcionário: {funcionario["nome"]} | Cargo: {funcionario["cargo"]}')