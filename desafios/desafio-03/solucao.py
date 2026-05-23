# Desafio 03 — Sistema de Multas
# Aluno: (Guilherme Cavalcante)
# Data:  (23/05/2026)

# ── Escreva sua solução abaixo ──────────────────────────────────────────────


velocidade = int(input('Digite a velocidade atual: '))

if velocidade > 80:
    excesso = velocidade - 80
    multa = excesso * 7
    print("Multado! Você excedeu o limite de 80km/h")
    print(f"Valor de multa: R$ {multa:.2f}")
else:
    print("Boa viagem! Dirija com segurança")




numero = 7

if numero <= 7:
    print("eu sou maior que 6")
if numero <= 9:
    print('eu sou maior que 9')
