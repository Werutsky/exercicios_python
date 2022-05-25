import random
print('''Escolha uma opção:
[1] Pedra
[2] Papel
[3] Tesoura''')
jogada =int(input(('Qual é a sua jogada:')))
lista = ['pedra', 'papel', 'tesoura']
computador = random.choice(lista)
if jogada == 1:
    print('Você escolheu PEDRA!')
elif jogada == 2:
    print('Você escolheu PAPEL!')
elif jogada == 3:
    print('Você escolheu TESOURA!')
else:
    print('ERRO! Tente novamente!')
if computador == 'pedra':
    print('Eu escolhi PEDRA!')
elif computador == 'papel':
    print('Eu escolhi PAPEL!')
elif computador == 'tesoura':
    print('Eu escolhi TESOURA!')
if jogada == 1 and computador == 'papel':
    print('Eu ganhei!')
elif jogada == 2 and computador == 'tesoura':
    print('Eu ganhei!')
elif jogada == 3 and computador == 'pedra':
    print('Eu ganhei!')
elif jogada == 1 and computador == 'pedra':
    print('EMPATE! Vamos jogar novamente!')
elif jogada == 2 and computador == 'papel':
    print('EMPATE! Vamos jogar novamente!')
elif jogada == 3 and computador == 'tesoura':
    print('EMPATE! Vamos jogar novamente!')
else:
    print('Você ganhou!')
