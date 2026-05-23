# Lista 01 — Questão 10: Análise Crítica de Código
# Aluno: (seu nome)
# Data:  (data)

# ── Enunciado ───────────────────────────────────────────────────────────────
# Em q10.py: reescreva a função corrigindo os 3 problemas encontrados.
# 
#   def processar_alunos(alunos=[]):
#       aprovados = []
#       for i in range(len(alunos)):
#           if alunos[i]['nota'] >= 7.0:
#               aprovados = aprovados + [alunos[i]['nome']]
#       print(aprovados)
# 
# Em q10_resposta.txt: identifique cada problema e explique por que é um problema.
# Dica: há um problema em: (1) definição da função, (2) como o loop é escrito, (3) como a lista é construída.

# ── Sua solução abaixo ──────────────────────────────────────────────────────

alunos = [                   # criando uma variavel aluno com elementos dentro;
    {'nome': 'Ana', 'nota': 8.5},
    {'nome': 'Bruno', 'nota': 6.0},
    {'nome': 'Carla', 'nota': 7.2}
]

def processar_alunos(alunos=None):  # criando uma funcao processar alunos, e quando a funcao nao receber 'alunos', vai evitar de dar erro e printar apenas o [] vazio;
    if alunos is None:  # verificando se alunos vai ser None
        alunos = []
    aprovados = []
    for aluno in alunos:  # aqui vou percorer cada aluno em alunos;
        if aluno['nota'] >= 7.0: # verificar se a nota do aluno e maior ou igual a 7;
            aprovados.append(aluno['nome']) # aqui estou pegando os nomes dos alunos que foram aprovados depois que passaram pela verficacao;
    print(aprovados) # aqui eu printo na telas todos os aprovados, no caso nome de cada um;


processar_alunos(alunos) # aqui estou chamando a funcao na lista de alunos;