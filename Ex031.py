distancia = float(input('Qual é a distância da sua viagem em km?'))
p1 = distancia * 0.50
p2 = distancia * 0.45
if distancia <= 200:
    print('Sua viagem é de {}km. O custo será de R${:.2f}'.format(distancia,p1))
else:
    print('Sua viagem é de {}Km. O custo será de R${:.2f}.'.format(distancia,p2))
