# Desafio 05 — Gerenciador de Compras
# Aluno: (Guilherme Cavalcante)
# Data:  (29/05/2026)

# ── Escreva sua solução abaixo ──────────────────────────────────────────────

produtos = []

while True:
    nome_produto = str(input('digite nome do produto'))

    if nome_produto == 'sair':
        print('saindo...')
        break
    else:
        produtos.append(nome_produto)
        print(f'produto adicionados: {nome_produto}')


print(f'produtos cadastrados: {produtos}')
print(f'produtos cadastrados: {", ".join(produtos)}') # dessa forma passo como string a lista de produtos;
