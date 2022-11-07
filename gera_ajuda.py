import random

def gera_ajuda (questao):

  opcoes = []
  for j in questao['opcoes'].values():
    opcoes.append(j)

  opcoes.remove(questao['opcoes'][questao['correta']])

  x = random.randint(1,2)

  if x == 1:
    return '''DICA:\nOpções certamente erradas: {}'''.format(random.choice(opcoes))

  else:
    questoes_sorteadas = []
    questoes_sorteadas.append(random.choice(opcoes))
    i = True
    while i:
        questao_inedita = random.choice(opcoes)
        if questao_inedita not in questoes_sorteadas:
          questoes_sorteadas.append(questao_inedita)
          i = False
        else:
          i = i
    return '''DICA:\nOpções certamente erradas: {} | {}'''.format(questoes_sorteadas[0], questoes_sorteadas[1])