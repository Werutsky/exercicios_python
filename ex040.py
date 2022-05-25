n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
m = (n1+n2)/2
if m < 5:
    print('Sua média foi {}. Infelizmente você foi \033[31mREPROVADO\033[m!'.format(m))
elif m >= 7:
    print('Sua média foi {}. PARABÉNS! Você foi \033[32mAPROVADO\033[m!'.format(m))
elif m >= 5 and m < 7:
    print('Sua média foi {}. Você ficou em \033[33mRECUPERAÇÃO\033[m!'.format(m))

