pv = int(input('Primeiro valor:'))
sv = int(input('Segundo valor:'))
tv = int(input('Terceiro valor:'))
#descobrindo valor menor
if pv<sv and pv<tv:
    menor = pv
if sv<pv and sv<tv:
    menor = sv
if tv<pv and tv<sv:
    menor = tv
#descobrindo valor maior
if pv>sv and pv>tv:
    maior = pv
if sv>pv and sv>tv:
    maior = sv
if tv>pv and tv>sv:
    maior = tv
print('O menor número é {} e o maior número é {}.'.format(menor, maior))
