import random
from time import sleep
print('Vou pensar em um número de 0 a 5. Tente adivinhar...')
numpc=random.randint(0,5)
numhum=int(input('Em que número eu pensei?'))
print('Processando...')
sleep(2)
if numpc == numhum:
    print('Você ganhou! Eu pensei no número {} mesmo!'.format(numpc))
else:
    print('Eu ganhei! Eu pensei no número {} e não no número {}.'.format(numpc, numhum))

'''método guanabara'''

