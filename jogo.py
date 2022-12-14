#COLORIR O TERMINAL

import random

class ANSI():   
    def color_text(code): 
        return "\33[{code}m".format(code=code)

questoes = [{'titulo': 'Qual o resultado da operação 57 + 32?',
          'nivel': 'facil',
          'opcoes': {'A': '-19', 'B': '85', 'C': '89', 'D': '99'},
          'correta': 'C'},

         {'titulo': 'Qual a capital do Brasil?',
          'nivel': 'facil',
          'opcoes': {'A': 'Brasília', 'B': 'Rio de janeiro', 'C': 'São Paulo', 'D': 'Osasco'},
          'correta': 'A'},

         {'titulo': 'Quando é o feriado da Independência do Brasil?',
          'nivel': 'facil',
          'opcoes': {'A': '21 de Abril', 'B': '12 de Outubro', 'C': '07 de Setembro', 'D': '15 de Novembro'},
          'correta': 'C'},

         {'titulo': '_________ é um conjunto de particularidades que caracterizam um grupo de pessoas, uma família ou uma sociedade. É formada por princípios morais, hábitos, costumes, histórias, manifestações religiosas, entre outros. Qual palavra melhor completa o início da frase?',
          'nivel': 'facil',
          'opcoes': {'A': 'Missão', 'B': 'Cultura', 'C': 'Curso superior', 'D': 'Culinária'},
          'correta': 'B'},

         {'titulo': 'Qual destes termos menos tem relação com o fenômeno da globalização?',
          'nivel': 'facil',
          'opcoes': {'A': 'Aculturação', 'B': 'Neoliberalismo', 'C': 'União Europeia', 'D': 'Caldeirão do Huck'},
          'correta': 'D'},

         {'titulo': 'Qual o feriado do aniversário da cidade de São Paulo?',
          'nivel': 'facil',
          'opcoes': {'A': '25 de Janeiro', 'B': '24 de Março', 'C': '9 de Julho', 'D': '12 de Novembro'},
          'correta': 'A'},

         {'titulo': 'Qual destas não é uma fruta?',
          'nivel': 'facil',
          'opcoes': {'A': 'Laranja', 'B': 'Maça', 'C': 'Tomate', 'D': 'Abacate'},
          'correta': 'B'},

         {'titulo': 'Em qual ano o TikTok atingiu 1 bilhão de usuários?',
          'nivel': 'facil',
          'opcoes': {'A': '2019', 'B': '2021', 'C': '2015', 'D': '2018'},
          'correta': 'B'},
         
         {'titulo': 'Qual destes não é um app com foco em streaming de vídeo?',
          'nivel': 'facil',
          'opcoes': {'A': 'Netflix', 'B': 'Disney Plus', 'C': 'TIDAL', 'D': 'HBO Max'},
          'correta': 'C'},

         {'titulo': 'Qual destes parques não se localiza em São Paulo?!',
          'nivel': 'facil',
          'opcoes': {'A': 'Ibirapuera', 'B': 'Parque do Carmo', 'C': 'Parque Villa Lobos', 'D': 'Morro da Urca'},
          'correta': 'D'},

         {'titulo': 'Qual destas não é uma linguagem de programação?',
          'nivel': 'facil',
          'opcoes': {'A': 'Miratdes', 'B': 'Python', 'C': 'Lua', 'D': 'C++'},
          'correta': 'A'},

         {'titulo': 'Dentre os listados, qual destes esportes é menos praticado no Brasil?',
          'nivel': 'facil',
          'opcoes': {'A': 'Natação', 'B': 'Vôlei', 'C': 'Ski Cross Country', 'D': 'Futebol'},
          'correta': 'C'},
         
         {'titulo': 'Qual o resultado da operação 5 + 2 * 3?',
          'nivel': 'medio',
          'opcoes': {'A': '21', 'B': '11', 'C': '30', 'D': '10'},
          'correta': 'B'},

         {'titulo': 'Qual destas é uma pseudociência que estuda os corpos celestes e as prováveis relações que possuem com a vida das pessoas e os acontecimentos na Terra?',
          'nivel': 'medio',
          'opcoes': {'A': 'Astronomia', 'B': 'Física quântica', 'C': 'Astrologia', 'D': 'Computação'},
          'correta': 'C'},

         {'titulo': 'Qual destas não foi considerada em 2007 uma das sete maravilhas do mundo moderno?',
          'nivel': 'medio',
          'opcoes': {'A': 'Muralha da China', 'B': 'Machu Picchu', 'C': 'Cristo Redentor', 'D': 'Torre Eiffel'},
          'correta': 'D'},

         {'titulo': 'Qual destas pessoas conduziu importantes estudos sobre radioatividade, sendo ganhadora de dois prêmios Nobel?',
          'nivel': 'medio',
          'opcoes': {'A': 'Marie Curie', 'B': 'Paul Erdős', 'C': 'Clive W.J. Granger', 'D': 'Maria Ressa'},
          'correta': 'A'},

         {'titulo': 'Quem é considerada a primeira pessoa programadora do mundo?!',
          'nivel': 'medio',
          'opcoes': {'A': 'Marie Curie', 'B': 'Alan Turing', 'C': 'Ada Lovelace', 'D': 'Edsger Dijkstra'},
          'correta': 'C'},

         {'titulo': 'Qual destes números é primo?',
          'nivel': 'medio',
          'opcoes': {'A': '259', 'B': '85', 'C': '49', 'D': '19'},
          'correta': 'D'},

         {'titulo': 'Na Conjectura de _______, escolhendo-se um número natural inicial n, onde n > 0, os seguintes critérios serão obedecidos: Se n for par o seu sucessor será a metade e se n for ímpar o seu sucessor será o triplo mais um, gerando então um novo número. Qual o nome da conjectura?',
          'nivel': 'medio',
          'opcoes': {'A': 'Collatz', 'B': 'Goldbach', 'C': 'Poincaré', 'D': 'Hodge'},
          'correta': 'A'},

         {'titulo': 'Como faço para chamar o SAMU?',
          'nivel': 'medio',
          'opcoes': {'A': 'Ligue 101', 'B': 'Ligue 192', 'C': 'Ligue 109', 'D': 'Ligue 122'},
          'correta': 'B'},

         {'titulo': 'Qual a segunda pessoa mais seguida no Instagram?',
          'nivel': 'medio',
          'opcoes': {'A': 'Cristiano Ronaldo', 'B': 'Dwayne Johnson', 'C': 'Kim Kardashian', 'D': 'Kylie Jenner'},
          'correta': 'D'},

         {'titulo': 'Qual a pessoa mais seguida no Instagram?',
          'nivel': 'medio',
          'opcoes': {'A': 'Cristiano Ronaldo', 'B': 'Dwayne Johnson', 'C': 'Kim Kardashian', 'D': 'Lionel Messi'},
          'correta': 'A'},

         {'titulo': 'A reprodução dos seres vivos é um processo biológico através do qual os organismos geram descendência. Qual desta não é uma forma de reprodução assexuada?',
          'nivel': 'dificil',
          'opcoes': {'A': 'Autogamia', 'B': 'Esporulação', 'C': 'Partenogênese', 'D': 'Divisão binária'},
          'correta': 'A'},

         {'titulo': 'Qual o resultado da operação 5 + 2 * 3 ^ 2, onde ^ representa potenciação?',
          'nivel': 'dificil',
          'opcoes': {'A': '441', 'B': '86', 'C': 'Nenhuma das outras respostas', 'D': '23'},
          'correta': 'D'},

         {'titulo': 'Quem é Oxóssi?!',
          'nivel': 'dificil',
          'opcoes': {'A': 'Rede de mercados', 'B': 'Tipo de poema Dissílabo', 'C': 'Divindade das religiões africanas', 'D': 'Trapper brasileiro'},
          'correta': 'C'},

         {'titulo': 'Qual a altura do Cristo Redentor?',
          'nivel': 'dificil',
          'opcoes': {'A': 'entre 0 e 20 metros', 'B': 'Entre 21 e 40 metros', 'C': 'Entre 41 e 60 metros', 'D': 'Mais que 60 metros'},
          'correta': 'B'},

         {'titulo': 'Em que ano faleceu Charles Babbage?',
          'nivel': 'dificil',
          'opcoes': {'A': '2022', 'B': '1791', 'C': '1935', 'D': '1871'},
          'correta': 'A'},

         {'titulo': 'Einstein foi Nobel de física em qual ano?',
          'nivel': 'dificil',
          'opcoes': {'A': '1906', 'B': '1905', 'C': '1920', 'D': '1921'},
          'correta': 'D'},

         {'titulo': 'Qual o número atômico do nitrogênio?',
          'nivel': 'dificil',
          'opcoes': {'A': '9', 'B': '7', 'C': '6', 'D': '8'},
          'correta': 'B'},

         {'titulo': 'Qual o ponto de fusão do nitrogênio?',
          'nivel': 'dificil',
          'opcoes': {'A': '120º C', 'B': '15º C', 'C': '-210º C', 'D': '-180º C'},
          'correta': 'C'},
         
         {'titulo': 'Quantos gols Pelé fez oficialmente?',
          'nivel': 'dificil',
          'opcoes': {'A': '815', 'B': '762', 'C': '1100', 'D': '1057'},
          'correta': 'B'},

         {'titulo': 'O que é Necrose?',
          'nivel': 'dificil',
          'opcoes': {'A': 'Uma banda de Rock', 'B': 'Uma marca de luxo', 'C': 'Cidade Francesa', 'D': 'Morte de tecido orgânico'},
          'correta': 'D'}
         
        ]

def valida_questoes (questoes):
    def valida_questao (questao):

        saida = {}
        saida_opcoes = {}
        lista_letras = ['A', 'B', 'C', 'D']
        lista_niveis = ['facil', 'medio', 'dificil']

        if len(questao.keys()) != 4: 
           saida['outro'] = 'numero_chaves_invalido' #2

        if 'titulo' not in questao.keys(): #1
            saida['titulo'] = 'nao_encontrado'
        else:
        
            if questao['titulo'].strip() == '':
                saida['titulo'] = 'vazio' #3

        if 'nivel' not in questao.keys(): #1
            saida['nivel'] = 'nao_encontrado'
        else:
            if questao['nivel'] not in lista_niveis: 
                saida['nivel'] = 'valor_errado' #4

        if 'opcoes' not in questao.keys(): #1
            saida['opcoes'] = 'nao_encontrado'
        else:
            if len(questao['opcoes'].keys()) != 4: 
                saida['opcoes'] = 'tamanho_invalido' #5 
            else:
                for letra, valor in questao['opcoes'].items():
                
                    if letra in lista_letras:
                        if valor.strip() == '':
                            saida_opcoes[letra] = 'vazia' #7
                            saida['opcoes'] = saida_opcoes
                    else:
                        saida_opcoes[letra] = 'chave_invalida_ou_nao_encontrada' #6
                        saida['opcoes'] = saida_opcoes 

        if 'correta' not in questao.keys(): #1
            saida['correta'] = 'nao_encontrado'
        else: 
            if questao['correta'] not in lista_letras:
                saida['correta'] = 'valor_errado' #8

        return saida
        
    lista_saida = []
    for i in questoes:
        lista_saida.append(valida_questao(i))
    return lista_saida

def transforma_base (questoes): 
    saida = {}
    for item in questoes:
        nivel = item['nivel']
        if nivel not in saida:
            saida[nivel] = []
        saida[nivel].append(item)
    return saida

lista = valida_questoes (questoes)
if lista.count({}) == len(lista): 
  quest_corretas = {}

else:
  print('Alguma pergunta não está de acordo com o esperado.')

if quest_corretas == {}:

  questoes = transforma_base (questoes)

  print("\033[31mOlá! Você está na Fortuna DesSoft e terá a oportunidade de enriquecer! Finalize o jogo e ganhe 1.000.000 de reais!!!\033[m")
  nome = input('Qual o seu nome? ')
  print('\n')
  print ('Ok {0}, serão 3 questões de cada nível (fácil, médio e dificil). \nVocê tem direito a pular 3 vezes e a pedir 2 ajudas!'.format(nome))
  print('\n')
  print ('As opções de resposta são "A", "B", "C", "D", "ajuda", "pula" e "parar"!')
  print('\n')
  input ('Aperte ENTER para continuar... ')
  print('\n')
  print('O jogo vai começar! Vamos para a primeira questão!')
  print('\n')
  print('Vamos começar pelo nível fácil!')
  print('\n')
  input ('\033[31mAperte ENTER para continuar...\033[m')

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
  
  questoes_sorteadas = []
  id = 0
  parar = 0
  ajudas = 0

  # NIVEL FÁCIL ------------------------------------------------------------------------

  x = 0
  nivel = 'facil'

  while x < 3:
    id+=1
    x += 1

    questao = sorteia_questao_inedida (questoes, nivel, questoes_sorteadas)

    print('\n')
    print (questao_para_texto(questao, id))
    resposta = input('\nQual sua resposta?! ')
    
    if resposta == 'A' or resposta == 'B' or resposta == 'C' or resposta == 'D':
      if resposta == questao['correta']:
          print ('\nParabéns, você acertou!')
      else:
        x = 3
        parar = 1
        print ('\nQue pena, você errou!')
        print('\nA resposta correta é a letra {}.'.format(questao['correta']))
        print('\nO jogo será finalizado...')

    elif resposta == 'pula':
      break

    elif resposta == 'parar':
      x = 3
      parar = 1 #tem que parar o jogo

    while resposta == 'ajuda':
      if ajudas < 2:
        ajudas+=1
        print('\n')
        print (gera_ajuda (questao)) #tem que repetir a questão
        input ('\033[31mAperte ENTER para continuar...\033[m')
        print('\n')
        print (questao_para_texto(questao, id))
        resposta = input('\nQual sua resposta?! ')
      else:
        print ('\nVocê não tem mais ajudas!')
        print('\nA resposta correta é a letra {}.'.format(questao['correta']))
        print('\nVamos para a próxima questão!')
        print ('\n')
        break

    while resposta != questao['correta'] and resposta != 'ajuda' and resposta != 'parar' and resposta != 'pula' and resposta != 'A' and resposta != 'B' and resposta != 'C' and resposta != 'D':
      print ('\nResposta inválida!')
      print('\n')
      input ('\033[31mAperte ENTER para continuar...\033[m')
      print('\n')
      print (questao_para_texto(questao, id))
      resposta = input('\nQual sua resposta?! ')

    input ('\033[31mAperte ENTER para continuar...\033[m')

  # NIVEL MÉDIO ------------------------------------------------------------------------

  if parar != 1: 

    print('\nVamos agora para as de nível médio!')
    input ('\033[31m\nAperte ENTER para continuar...\033[m')

    nivel = 'medio'
    x = 0
    
    while x < 3:
      id+=1
      x += 1

      questao = sorteia_questao_inedida (questoes, nivel, questoes_sorteadas)

      print('\n')
      print (questao_para_texto(questao, id))
      resposta = input('\nQual sua resposta?! ')
      
      if resposta == 'A' or resposta == 'B' or resposta == 'C' or resposta == 'D':
        if resposta == questao['correta']:
            print ('\nParabéns, você acertou!')
        else:
          x = 3
          parar = 1
          print ('\nQue pena, você errou!')
          print('\nA resposta correta é a letra {}.'.format(questao['correta']))
          print('\nO jogo será finalizado...')

      elif resposta == 'pula':
        break

      elif resposta == 'parar':
        x = 3
        parar = 1 #tem que parar o jogo

      while resposta == 'ajuda':
        if ajudas < 2:
          ajudas+=1
          print('\n')
          print (gera_ajuda (questao)) #tem que repetir a questão
          input ('\033[31mAperte ENTER para continuar...\033[m')
          print('\n')
          print (questao_para_texto(questao, id))
          resposta = input('\nQual sua resposta?! ')
        else:
          print ('\nVocê não tem mais ajudas!')
          print('\nA resposta correta é a letra {}.'.format(questao['correta']))
          print('\nVamos para a próxima questão!')
          print ('\n')
          break

      while resposta != questao['correta'] and resposta != 'ajuda' and resposta != 'parar' and resposta != 'pula' and resposta != 'A' and resposta != 'B' and resposta != 'C' and resposta != 'D':
        print ('\nResposta inválida!')
        print('\n')
        input ('Aperte ENTER para continuar... ')
        print('\n')
        print (questao_para_texto(questao, id))
        resposta = input('\nQual sua resposta?! ')

      input ('\033[31mAperte ENTER para continuar...\033[m')

# NIVEL DIFÍCIL ------------------------------------------------------------------------

  if parar != 1: 

    print('\nVamos agora para as de nível difícil!')
    input ('\033[31mAperte ENTER para continuar...\033[m')

    nivel = 'dificil'
    x = 0
    
    while x < 3:
      id+=1
      x += 1

      questao = sorteia_questao_inedida (questoes, nivel, questoes_sorteadas)

      print('\n')
      print (questao_para_texto(questao, id))
      resposta = input('\nQual sua resposta?! ')
      
      if resposta == 'A' or resposta == 'B' or resposta == 'C' or resposta == 'D':
        if resposta == questao['correta']:
            print ('\nParabéns, você acertou!')
        else:
          x = 3
          parar = 1
          print ('\nQue pena, você errou!')
          print('\nA resposta correta é a letra {}.'.format(questao['correta']))
          print('\nO jogo será finalizado...')

      elif resposta == 'pula':
        break

      elif resposta == 'parar':
        x = 3
        parar = 1 #tem que parar o jogo

      while resposta == 'ajuda':
        if ajudas < 2:
          ajudas+=1
          print('\n')
          print (gera_ajuda (questao)) #tem que repetir a questão
          input ('\033[31mAperte ENTER para continuar...\033[m')
          print('\n')
          print (questao_para_texto(questao, id))
          resposta = input('\nQual sua resposta?! ')
        else:
          print ('\nVocê não tem mais ajudas!')
          print('\nA resposta correta é a letra {}.'.format(questao['correta']))
          print('\nVamos para a próxima questão!')
          print ('\n')
          break

      while resposta != questao['correta'] and resposta != 'ajuda' and resposta != 'parar' and resposta != 'pula' and resposta != 'A' and resposta != 'B' and resposta != 'C' and resposta != 'D':
        print ('\nResposta inválida!')
        print('\n')
        input ('\033[31mAperte ENTER para continuar...\033[m')
        print('\n')
        print (questao_para_texto(questao, id))
        resposta = input('\nQual sua resposta?! ')

      input ('\033[31mAperte ENTER para continuar...\033[m')

  print ('\nParabéns! Você chegou ao fim do jogo!')