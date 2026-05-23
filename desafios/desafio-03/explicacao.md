# Explicação — Desafio 03 — Sistema de Multas

**Aluno:** _(Guilherme Cavalcante)_
**Data:** _(23/05/2026)_

---

## O que meu programa faz

_(primeiramente eu criei variavel com input pegando apenas numeros int para digitar a velocidade atual.
 criei uma condicao para verifcar se a velocidade passa acima de 80;
 uma variavel 'excesso' pegando 'velocidade' e subtraindo por 80 pra gente achar valor de quantos km ultrapassou alem de permitido;
 outra chamada 'multa' fazendo uma operacao de multiplicacao por 7 que e o valor da multa por km;
 depois vai printar as duas 'mensagens' caso passe dos 80km;
 se nao vai pro 'else' que printa na tela string'Boa viagem! Dirija com segurança'; )_

---

## Resposta à Pergunta Obrigatória

> Por que usamos `elif` e não múltiplos `if` separados? Dê um exemplo concreto onde a diferença causaria um resultado errado.

_(Professor acho que agora entendi, quando se trata de 'if' indepedentes acaba conferindo todos os blocos e tem a probabilidade de cair em dois resultados. Usado mais para quando queremos mais de dois resultados;
 Já o if/elif/else a gente vai usar como condicoes e o a verdadeira sera executada.
 0 chance de ter dois resultados;
  )_

numero = 7

if numero <= 7:
    print("eu sou maior que 6")
if numero <= 9:
    print('eu sou maior que 8')


---

## Dificuldades encontradas

_(Opcional: o que foi difícil? O que você pesquisou para resolver?)_
