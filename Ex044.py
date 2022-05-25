preco = float(input('Digite o valor das compras: R$'))
a = preco - (preco*10/100)
b = preco - (preco*5/100)
d = preco + (preco*20/100)
print('''Formas de Pagamento:
[1] À vista em dinheiro ou cheque
[2] À vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opcao = float(input('Digite sua opção:'))
if opcao == 1:
    print('Sua compra de R${:.2f} vai custar R${:.2f}.'.format(preco, a))
elif opcao == 2:
    print('Sua compra de R${:.2f} vai custar R${:.2f}.'.format(preco, b))
elif opcao == 3:
    print('Sua compra de R${:.2f} vai custar R${:.2f}.'.format(preco, preco))
elif opcao == 4:
    print('Sua compra de R${:.2f} vai custar R${:.2f}.'.format(preco, d))