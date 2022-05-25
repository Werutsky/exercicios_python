dias=int(input('Quantos dias alugados?'))
km= float(input('Quantos km rodados?'))
p=dias*60+km*0.15
print('Você percorreu {}km e utilizou o carro por {} dias. Nesse caso, o valor a pagar é R$ {:.2f}.'.format(km, dias,p))
