# Desafio 06 — Bio-Cadastro
# Aluno: (Guilherme Cavalcante)
# Data:  (29/05/2026)

# ── Escreva sua solução abaixo ──────────────────────────────────────────────


equipe = []

while True:
    nome = str(input('digite seu nome: '))
    if nome == 'sair':
        print('saindo...')
        break
    cargo = str(input('digite seu cargo'))
    if cargo == 'sair':
        print('saindo...')
        break
    equipe.append({'nome': nome, 'cargo': cargo})
    print(f'colaborador adicionado com sucesso.')
    
for funcionario in equipe:
    print(f'Funcionário: {funcionario["nome"]} | Cargo: {funcionario["cargo"]}')


# fiquei com duvida se tem alguma forma de deixar mais clean meu bloco de codigo do loop ou essa
# forma que fiz ja esta bem com essa quantidade de linhas...;