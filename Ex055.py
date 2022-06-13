maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Digite o peso da {}a. pessoa:'.format(p)))
    if p == 1:
        maior = p
        menor = p
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi {} kg.\nO menor peso lido foi {} kg'.format(maior, menor))