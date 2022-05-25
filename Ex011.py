l=float(input('Qual é a largura da parede em metros?'))
a=float(input('Qual é a altura da parede em metros?'))
f=l*a/2
print('Sua parede tem a dimensão de {}x{} e sua área é de {:.2f}m2.\nPara pintar essa parede você precisará de {:.2f} '
      'litros de tinta'.format(l,a,l*a,f))