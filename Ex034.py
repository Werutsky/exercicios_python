salario = float(input('Digite o salário atual:'))
aumento1 = salario + salario * 10 / 100
aumento2 = salario + salario * 15 / 100
if salario > 1250.00:
    print('Seu salário que era de R${:.2f}, passará a ser de R${:.2f}.'.format(salario, aumento1))
else:
    print('Seu salário era de R${:.2f}, passará a ser de R${:.2f}.'.format(salario, aumento2))
