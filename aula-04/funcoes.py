''' FUNÇÕES '''

'''
- FUNÇÕES SEM PARAMETROS E SEM RETORNO
- FUNÇÕES COM PARAMETROS E SEM RETORNO
- FUNÇÕES SEM PARAMETROS E COM RETORNO
- FUNÇÕES COM PARAMETROS E COM RETORNO
'''

''' 
PARA DECLARAR UMA FUNÇÃO PRECISAMOS DA PALAVRA RESERVADA DEF
UMA FUNÇÃO PRECISA SER NOMEADA COMO UMA AÇÃO A SER EXECUTADA
'''

# Criando uma função sem parametros e sem retorno
def somar_dois_numeros():
    numero1 = 80
    numero2 = 20
    print(numero1 + numero2)
    
print('-'*100)
print('Saída da função sem parametros e sem retorno')
somar_dois_numeros()

# Criando a função com parametros e sem retorno
def somar_dois_numeros(numero1, numero2):
    print(numero1 + numero2)

# print('-'*100)
# print('Saída da função com parametros e sem retorno')
# numero1 = int(input('Digite o primeiro numero da soma: '))
# numero2 = int(input('Digite o segundo numero da soma: '))
# somar_dois_numeros(numero1, numero2)

# Criando função sem parametros e com retorno
def somar_dois_numeros():
    numero1, numero2 = 10, 20
    return numero1 + numero2

resultado_da_soma_de_dois_numeros = somar_dois_numeros()
print('-'*100)
print('Saída da função sem parametros e com retorno')
print(f'o resultado é {resultado_da_soma_de_dois_numeros}')

# Criando uma função com parametros e com retorno
def somar_dois_numeros(numero1, numero2):
    return numero1 + numero2

print('-'*100)
print('Saída da função com parametros e com retorno')
resultado = somar_dois_numeros(50,50)
print(resultado)

# *args -> Recebe uma tupla como argumentos
# Essa função pode receber vários argumentos
def somar(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    return resultado
    
resultado = somar(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18)

print('-'*100)
print(f'Resultado da somatória {resultado}')