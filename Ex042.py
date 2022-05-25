print('\033[33m-=\033[m'*20)
print('\033[34mANALISADOR DE TRIÂNGULOS\033[m')
print('\033[33m-=\033[m'*20)
r1 = float(input('Primeiro segmento:'))
r2 = float(input('Segundo segmento:'))
r3 = float(input('Tereceiro segmento:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos podem formar um triângulo')
    if r1 == r2 == r3:
        print('O triângulo é EQUILÁTERO')
    elif r1 != r2 and r1 != r3 and r2 != r3:
        print('O triângulo é ESCALENO')
    else:
        print('O triângulo é ISÓCELES')
else:
    print('Os segmentos não podem formar um triângulo')