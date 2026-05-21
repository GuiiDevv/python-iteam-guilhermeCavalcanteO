# Lista 01 — Questão 05: Encontre o Bug
# Aluno: (Guilherme Cavalcante)
# Data:  (21/06/2026)

# ── Enunciado ───────────────────────────────────────────────────────────────
# O código abaixo tem um bug lógico — executa sem erros, mas produz resultado errado.
# Copie o código no arquivo, identifique o bug, corrija-o e explique em comentário.
# 
#   def maior_nota(notas):
#       maior = 0
#       for nota in notas:
#           if nota > maior:
#               maior == nota  # bug aqui
#       return maior
#   print(maior_nota([7.5, 9.0, 6.0, 8.5]))

# ── Sua solução abaixo ──────────────────────────────────────────────────────

def maior_nota(notas):
    maior = 0
    for nota in notas:
        if nota > maior:
            maior = nota
    return maior  
print(maior_nota([7.5, 9.0, 6.0, 8.5]))

# ao inves "==" que e uma comparacao pra ver se 'maior' e equivalente a 'nota', o correto e usar '=' para atribuir o valor de nota a maior.

