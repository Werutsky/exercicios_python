casa = float(input('Digite o valor da casa:'))
salario = float(input('Digite o valor do seu salário:'))
prazo = int(input('Digite em quantos anos pretende financiar:'))
prazom = prazo * 12
prestacao = casa / prazom
if casa / prazom > salario * 30 / 100:
    print('Sua prestação é de R${:.2f}. Empréstimo foi \033[31mNEGADO\033[m!'.format(prestacao))
else:
    print('Sua prestação mensal é de R${:.2f}. Empréstimo foi \033[32mAPROVADO\033[m!'.format(prestacao))