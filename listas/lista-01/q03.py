# Lista 01 — Questão 03: Ficha de Cadastro
# Aluno: (seu nome)
# Data:  (data)

# ── Enunciado ───────────────────────────────────────────────────────────────
# Solicite: nome completo, CPF (str), ano de nascimento (int), altura (float).
# O programa deve:
#   1. Calcular e exibir a idade em 2026.
#   2. Exibir todos os dados com f-string e tipos corretos.
#   3. Tratar com try/except o caso em que o ano não seja um número.
# Explique em comentário: por que float para altura e não int?

# ── Sua solução abaixo ──────────────────────────────────────────────────────

nome = str(input("Digite seu nome completo:"))
cpf = str(input("Digite seu CPF: "))
anoAtual = 2026
altura = float(input("Digite sua altura: "))

while True:
    try:
        anoNascimento = int(input("Digite seu ano de nascimento: "))
        idade = anoAtual - anoNascimento
        break
    except ValueError:
        print("Por favor, digite um número válido para o ano de nascimento.")
        anoNascimento = 0
        idade = 0

print("----------------------------------")
print(f'Seu nome é: {nome}')
print(f'Seu CPF é: {cpf}')
print(f'Sua altura é: {altura} metros.')
print(f'Seu ano de nascimento é: {anoNascimento}.')
print(f'Sua idade é: {idade} anos.')
