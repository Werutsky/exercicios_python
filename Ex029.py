velocidade = float(input('Qual é a sua velocidade em km/h?'))
multa = (velocidade - 80) * 7
if velocidade <= 80:
    print('Sua velocidade está adequada!')
else:
    print('MULTADO! Você excedeu o limite permitido que é de 80 km/h. \nVocê deve pagar uma multa de R$ {:.2f}'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')