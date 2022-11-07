import random

questoes = {
  "facil": [
    {
      "titulo": "Qual o resultado da operação 57 + 32?",
      "nivel": "facil",
      "opcoes": {
        "A": "-19",
        "B": "85",
        "C": "89",
        "D": "99"
      },
      "correta": "C"
    },
    {
      "titulo": "Qual destes parques não se localiza em São Paulo?!",
      "nivel": "facil",
      "opcoes": {
        "A": "Ibirapuera",
        "B": "Parque do Carmo",
        "C": "Parque Villa Lobos",
        "D": "Morro da Urca"
      },
      "correta": "D"
    },
    {
      "titulo": "Qual destas não é uma linguagem de programação?",
      "nivel": "facil",
      "opcoes": {
        "A": "Miratdes",
        "B": "Python",
        "C": "Lua",
        "D": "C++"
      },
      "correta": "A"
    },
    {
      "titulo": "Dentre os listados, qual destes esportes é menos praticado no Brasil?",
      "nivel": "facil",
      "opcoes": {
        "A": "Natação",
        "B": "Vôlei",
        "C": "Ski Cross Country",
        "D": "Natação"
      },
      "correta": "C"
    }
  ],
  "medio": [
    {
      "titulo": "Qual destes números é primo?",
      "nivel": "medio",
      "opcoes": {
        "A": "259",
        "B": "85",
        "C": "49",
        "D": "19"
      },
      "correta": "D"
    },
    {
      "titulo": "Na Conjectura de _______, escolhendo-se um número natural inicial n, onde n > 0, os seguintes critérios serão obedecidos: Se n for par o seu sucessor será a metade e se n for ímpar o seu sucessor será o triplo mais um, gerando então um novo número. Qual o nome da conjectura?",
      "nivel": "medio",
      "opcoes": {
        "A": "Collatz",
        "B": "Goldbach",
        "C": "Poincaré",
        "D": "Hodge"
      },
      "correta": "A"
    },
    {
      "titulo": "Qual a segunda pessoa mais seguida no Instagram?",
      "nivel": "medio",
      "opcoes": {
        "A": "Cristiano Ronaldo",
        "B": "Dwayne Johnson",
        "C": "Kim Kardashian",
        "D": "Kylie Jenner"
      },
      "correta": "D"
    }
  ],
  "dificil": [
    {
      "titulo": "A reprodução dos seres vivos é um processo biológico através do qual os organismos geram descendência. Qual desta não é uma forma de reprodução assexuada?",
      "nivel": "dificil",
      "opcoes": {
        "A": "Autogamia",
        "B": "Esporulação",
        "C": "Partenogênese",
        "D": "Divisão binária"
      },
      "correta": "A"
    },
    {
      "titulo": "Qual o resultado da operação 5 + 2 * 3 ^ 2, onde ^ representa potenciação?",
      "nivel": "dificil",
      "opcoes": {
        "A": "441",
        "B": "86",
        "C": "Nenhuma das outras respostas",
        "D": "23"
      },
      "correta": "D"
    }
  ]
}

print('Olá! Bem-vindo ao jogo!')
nome = input('Qual o seu nome? ')

print ('Ok {0}, serão 3 questões de cada nível (fácil, médio e dificil). \nVocê tem direito a pular 3 vezes e 2 ajudas!'.format(nome))
print ('As opções de resposta são "A", "B", "C", "D", "ajuda", "pula" e "parar"!')
input ('Aperte ENTER para continuar... ')

print('O jogo vai começar! Vamos para a primeira questão!')
print('Vamos começar pelo nível fácil!')
input ('Aperte ENTER para continuar... ')

questoes_sorteadas = []
nivel = 'facil'
id = 0
x = 0

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

def questao_para_texto (questao, id):
  
  return '----------------------------------------\nQUESTAO {}\n\n{}\n\nRESPOSTAS:\nA: {}\nB: {}\nC: {}\nD: {}'.format(id, questao['titulo'], questao['opcoes']['A'], questao['opcoes']['B'], questao['opcoes']['C'], questao['opcoes']['D'])

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

while x < 3:
  id+=1
  x += 1

  questao = sorteia_questao_inedida (questoes, nivel, questoes_sorteadas)

  print (questao_para_texto(questao, id))
  resposta = input('Qual sua resposta?! ')

  if resposta == questao['correta']:
      print ('Parabéns, você acertou!')

  elif resposta == 'ajuda':
    print (gera_ajuda (questao))

  elif resposta == 'pula':
    break

  elif resposta == 'parar':
    x = 3 

  elif resposta != questao['correta']:
      print ('Você errou!')
