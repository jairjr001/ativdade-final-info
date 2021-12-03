#PROGRAMA PARA CALCULO DE PROFUNDIDADE DE ESCAREADO
#PE26118AD E PE26119AD SÃO TIPOS DE REBITES UTILIZADOS NAS FUSELAGENS
#PE26118ADX ONDE ESTÁ O X INDICA O DIÁMETRO DO REBITE 6(3/16"), 7(7/32")
#CADA DIÂMETRO TEM UMA PROFUNDIDADE MÁXIMA PERMITIDA POR NORMA TÉCNICA




def codigo1():
  c = float(input('Digite a espessura: '))
  n1 = c
  n2 = 0.666
  n3 = n1*n2
  n4 = 1.45
  print('PE26118AD6 2/3 coorresponde há:  ',n3)
  d = float(input('Digite a profundidade do escareado: '))
  if d >= n3:
     print('Profundidade aceita')
  else:
     print(' Profundidade precisa de análise da engenharia.')
  if n1 >=n4:
    print('Espessura aceita')
  if n1 < n4:
    print('Atenção espessura não aceita acionar Engenharia')              
def codigo2():
  c = float(input('Digite a espessura: '))
  n1 = c
  n2 = 0.666
  n3 = n1*n2
  n4= 1.85
  print('PE26118AD6 2/3 coorresponde há:  ',n3)
  d = float(input('Digite a profundidade do escareado: '))
  if d >= n3:
     print('Profundidade aceita')
  else:
     print(' Profundidade precisa de análise da engenharia.')
  if n1 >=n4:
    print('Espessura aceita')
  if n1 < n4:
    print('Atenção espessura não aceita acionar Engenharia')
def codigo3():
  c = float(input('Digite a espessura: '))
  n1 = c
  n2 = 0.666
  n3 = n1*n2
  n4= 2.35
  print('PE26118AD6 2/3 coorresponde há:  ',n3)
  d = float(input('Digite a profundidade do escareado: '))
  if d >= n3:
     print('Profundidade aceita')
  else:
     print(' Profundidade precisa de análise da engenharia.')
  if n1 >=n4:
    print('Espessura aceita')
  if n1 < n4:
    print('Atenção espessura não aceita acionar Engenharia')
def codigo8():

    print('Programa para profundidade de escareado para reparo.')
    print('Ao abrir o programa o usuário deve escolher qual opção ele deseja usar, colocando o valor que deseja que seja calculado')

    print('Opção 1- PE26118AD6')
 
    print('Opção 2- PE26118AD7')

    print('Opção 3- PE26119AD6')

    print('Opção 4- o programa é encerrado')
