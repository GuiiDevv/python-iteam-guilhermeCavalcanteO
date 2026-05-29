# Lista 02 — Questão 03: Sistema de Inventário
# Aluno: (seu nome)
# Data:  (data)

# ── Enunciado ───────────────────────────────────────────────────────────────
# Implemente com lista de dicionários:
#   1. adicionar_produto(inventario, nome, codigo, quantidade, preco)
#   2. buscar_por_codigo(inventario, codigo)  → produto ou None
#   3. listar_abaixo_do_minimo(inventario, minimo)
#   4. valor_total(inventario)  → soma de quantidade × preço
# Use funções para cada operação. Demonstre as 4 no código principal.

# ── Sua solução abaixo ──────────────────────────────────────────────────────



produtos = [
    {"nome": "Produto A", "codigo": "001", "quantidade": 10, "preco": 5.0},
    {"nome": "Produto B", "codigo": "002", "quantidade": 3, "preco": 15.0},
]

def adicionar_produto (produtos, nome, codigo, quantidade, preco):
    produto = {"nome": nome, "codigo": codigo, "quantidade": quantidade, "preco": preco}
    produtos.append(produto)

def buscar_por_codigo (produtos, codigo):
    for produto in produtos:
        if produto["codigo"] == codigo:
            return print(f"Produto: {produto['nome']}, Código: {produto['codigo']}, Quantidade: {produto['quantidade']}, Preço: {produto['preco']} reais")
    return None

def listar_abaixo_do_minimo (produtos, minimo):
    abaixo_do_minimo = []
    for produto in produtos:
        if produto["quantidade"] < minimo:
            abaixo_do_minimo.append(produto)
    return abaixo_do_minimo

def valor_total (produtos):
    total = 0
    for produto in produtos:
        total += produto["quantidade"] * produto["preco"]
    return total

def lista_de_produtos (produtos):
    for produto in produtos:
        print(f"Produto: {produto['nome']}, Código: {produto['codigo']}, Quantidade: {produto['quantidade']}, Preço: {produto['preco']} reais")


#nome = input("Digite o nome do produto: ")
#codigo = input("Digite o código do produto: ")
#quantidade = int(input("Digite a quantidade do produto: "))
#preco = float(input("Digite o preço do produto: "))
adicionar_produto(produtos, 'ovo', '003', 5, 20.0)
adicionar_produto(produtos, 'ovoo', '004', 2, 20.0)

print('Lista de produtos:')
lista_de_produtos(produtos)
print("=====================================================")
print('Produtos abaixo da quantidade minima:')
produtos_abaixo = listar_abaixo_do_minimo(produtos, 5)
for produto in produtos_abaixo:
    print(f"Produto: {produto['nome']}, Código: {produto['codigo']}, Quantidade: {produto['quantidade']}, Preço: {produto['preco']} reais")
print("=====================================================")
buscar_por_codigo(produtos, '003')
#valor_final = valor_total(produtos)
#print(valor_final)
print(f'valor total dos produtos: {valor_total(produtos)}')




notas = [ 1, 2, 3, 4, 5]

def calcular_media(notas):
    calculo = sum(notas) / len(notas)
    return print(f'sua media foi: {calculo}')

calcular_media(notas)
