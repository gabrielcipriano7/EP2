import random

def sorteia_questao_inedida (questoes, nivel, questoes_sorteadas):
    
    i = True
    while i:
        questao_inedita = random.choice(questoes[nivel])
        if questao_inedita not in questoes_sorteadas:
            i = False
        else:
            i = i
        
    questoes_sorteadas.append(questao_inedita)

    return questao_inedita
