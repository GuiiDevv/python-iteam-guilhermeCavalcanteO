# Desafio 04 — Tabuada Personalizada
# Aluno: (Guilherme Cavalcante)
# Data:  (29/05/2026)

# ── Escreva sua solução abaixo ──────────────────────────────────────────────

while True:
    numero_digitado = int(input('digite seu numero: '))
    if numero_digitado == 0:
        print('saindo...')
        break
    for numero in range(0, 11):
        resultado = numero_digitado + numero
        print(f'resultado de {numero_digitado} + {numero} = {resultado}')


