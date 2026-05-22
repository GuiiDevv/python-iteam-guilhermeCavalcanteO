# Lista 01 — Questão 06: Validador de Senha
# Aluno: (Guilherme Cavalcante)
# Data:  (21/05/2026)

# ── Enunciado ───────────────────────────────────────────────────────────────
# Escreva um programa que solicite uma senha em loop até que atenda TODOS:
#   1. Mínimo 8 caracteres.
#   2. Pelo menos um dígito (use .isdigit() em cada caractere).
#   3. Pelo menos uma letra maiúscula.
# Para cada tentativa inválida, informe qual critério não foi atendido.
# Ao aceitar: 'Senha válida após X tentativa(s).'

# ── Sua solução abaixo ──────────────────────────────────────────────────────

tentativas = 0
while True:
    senha = input('Digite sua senha: ')
    senha_valida = True
    tentativas += 1

    if len(senha) < 8:
        print('A senha deve ter no mínimo 8 caracteres.')
        senha_valida = False

    if not any(char.isdigit() for char in senha):
        print('A senha deve ter pelo menos um dígito.')
        senha_valida = False

    if not any(char.isupper() for char in senha):
        print('A senha deve ter pelo menos uma letra maiúscula.')
        senha_valida = False

    if senha_valida:
        print(f'Senha válida após {tentativas} tentativa(s).')
        break
    