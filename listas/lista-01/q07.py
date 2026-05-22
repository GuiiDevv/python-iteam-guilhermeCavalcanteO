# Lista 01 — Questão 07: Progressão e Análise
# Aluno: (Guilherme Cavalcante)
# Data:  (22/05/2026)

# ── Enunciado ───────────────────────────────────────────────────────────────
# Leia 10 notas (0.0–10.0) com validação (try/except + while para inválidas).
# Exiba: maior nota, menor nota, média, quantidade acima da média e
# classificação (Aprovado ≥ 7.0, Recuperação ≥ 5.0, Reprovado).
# Explique em comentários por que escolheu for ou while em cada parte.

# ── Sua solução abaixo ──────────────────────────────────────────────────────


notas = []
i = 0
while i < 10:  # escolhi o while pq sei que caso eu escreva uma nota ou valor nao permitido vai pedir pra digitar denovo, inumeras vezes ate eu digitar as 10 notas validas;
    try:
        nota = float(input(f"Digite a nota {i+1} (0.0 a 10.0): "))
        if 0.0 <= nota <=10.0:
            notas.append(nota)
            i += 1
        else:
            print('Nota nao permitida, tente novamente.')
    except ValueError:
        print('Valor invalido, tente novamente.')

maior = max(notas) # aqui estou pegando minha maior nota dentro da variavel 'notas';
menor = min(notas) # aqui estou pegando minha menor nota dentro da variavel 'notas';
media = sum(notas) / 10  # vi tambem que eu poderia fazer 'len(notas)', que vai pegar a quatidade de elementos dentro da variavel notas;
acima_media = 0
for nota in notas:  # já aqui usei 'for' pq ja sei a quantidade exata de nota dentro de notas, entao ideal seria for mesmo;
    if nota > media:
        acima_media += 1

if media >= 7.0:
    classificacao = 'aprovado'
elif media >= 5.0: 
    classificacao = 'recuperacao'
else:
    media = 'reprovado'

print(f"suas notas: {notas}")
print(f"Maior nota: {maior}")
print(f"Menor nota: {menor}")
print(f"Média: {media:.2f}")
print(f"Quantidade de notas acima da média: {acima_media}")
print(f"Classificação: {classificacao}")
