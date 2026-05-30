# Desafio 01 — Seu Primeiro Script
# Aluno: (Guilherme Cavalcante)
# Data:  (22/05/2026)

# ── Escreva sua solução abaixo ──────────────────────────────────────────────



nome = input("Digite seu nome: ") 
ano_nascimento = int(input("Digite seu ano de nascimento: "))
ano_atual = 2026
idade = ano_atual - ano_nascimento
hobbies = []
while True:
    hobbie = str(input('digite seus hobbies: '))
    if hobbie == 'sair':
        print('saindo...')
        break
    else: 
        hobbies.append(hobbie)


print(f"ola, {nome}! voce tem {idade} anos.")
print(f"seus hobbies são: {', '.join(hobbies)}") #peguei do desafio 5, pelo que entendi ele junta os elementos da minha lista tudo em so uma string, e depois separando com virgula ", ";



