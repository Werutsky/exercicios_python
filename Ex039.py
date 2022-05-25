from datetime import date
nascimento = int(input('Digite seu ano de nascimento:'))
anoatual = date.today().year
idade = anoatual - nascimento
falta = 18 - idade
passou = idade - 18
print('Quem nasce em {}, completa {} anos em {}.'.format(nascimento, idade, anoatual))
if idade < 18:
    print('Ainda faltam {}anos para o alistamento.\nSeu alistamento será em {}'.format(falta, nascimento+18))
elif idade ==18:
    print('Você deve se alistar este ano!')
else:
    print('Você já deveria ter se alistado em {}. Passaram {} anos do seu ano de alistamento.'.format(nascimento + 18,passou))
