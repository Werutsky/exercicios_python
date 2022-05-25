peso = float(input('Digite o seu peso em kg:'))
altura = float(input('Digite a sua altura:'))
imc = peso / (altura**2)
print('O IMC é {:.1f}.'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso!')
elif 18.5 <= imc < 25:
    print('Você está no peso ideal!')
elif 25 <= imc < 30:
    print('Você está com sobrepeso!')
elif 30 <= imc < 40:
    print('Você está com obesidade!')
elif peso > 40:
    print('Você possui obesidade mórbida!')