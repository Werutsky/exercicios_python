from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for c in range (1,8):
    ano = int(input('Digite o {}º ano:'.format(c)))
    idade = atual - ano
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Nessa lista temos {} pessoas maiores e {} pessoas menores!'.format(totmaior, totmenor))
