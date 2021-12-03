#PROGRAMA PARA CALCULO DE PROFUNDIDADE DE ESCAREADO
#PE26118AD E PE26119AD SÃO TIPOS DE REBITES UTILIZADOS NAS FUSELAGENS
#PE26118ADX ONDE ESTÁ O X INDICA O DIÁMETRO DO REBITE 6(3/16"), 7(7/32")
#CADA DIÂMETRO TEM UMA PROFUNDIDADE MÁXIMA PERMITIDA POR NORMA TÉCNICA

   


import model
opcao = 0
print('PROGRAMA PARA CALCULO DE PROFUNDIDADE DE ESCAREADO')
print('PE26118AD E PE26119AD SÃO TIPOS DE REBITES UTILIZADOS NAS FUSELAGENS')
print('PE26118ADX ONDE ESTÁ O X INDICA O DIÁMETRO DO REBITE 6(3/16"), 7(7/32)')
print('CADA DIÂMETRO TEM UMA PROFUNDIDADE MÁXIMA PERMITIDA POR NORMA TÉCNICA, MANUAL DE REPARO.')
print('usar (.) para substituir a (,)')
print('Digite 1 para PE26118AD6.')
print('Digite 2 para PE26118AD7.')
print('Digite 3 para PE26119AD6.')
print('Digite 4 para fechar programa')
print('Digite 8 para ajuda')

while opcao !='4':
  opcao =input('Digite sua opção: ')

  if opcao == '1':
  
      model.codigo1()                 
  elif opcao == '2':
  
    model.codigo2()
  if opcao == '3':
  
    model.codigo3()    
  elif opcao== '8':
    model.codigo8()

  if opcao == '4':
    print('Programa encerrado')
    exit()
  
