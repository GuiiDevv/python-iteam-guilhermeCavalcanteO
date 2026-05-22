# Desafio 02 — Calculadora de IMC
# Aluno: (Guilherme Cavalcante)
# Data:  (22/05/2026)

# ── Escreva sua solução abaixo ──────────────────────────────────────────────

nome = input('Digite seu nome: ')
peso = int(input('Digite seu peso:'))
altura = int(input('digite sua altura:'))

altura_final = altura ** 2
valor_imc = peso / altura_final

print(f"Ola {nome}, seu IMC é {valor_imc:.2f}.")