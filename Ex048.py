cont = 0
soma = 0
for c in range (1,501, 2):
    if c % 3 == 0:
        cont = cont + 1
        soma = soma + c
print('A quantidade de valore é {}, e a soma do valor é {}'.format(cont, soma))
