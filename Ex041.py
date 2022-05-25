from datetime import date
ano = int(input('Digite o ano do nascimento:'))
atual = date.today().year
idade = atual - ano
if idade <= 9:
    print('O atleta tem {} anos.\nClassificação: JUNIOR'.format(idade))
elif idade > 9 and idade <= 14:
    print('O atleta tem {} anos.\nClassificação: INFANTIL'.format(idade))
elif idade > 14 and idade <= 19:
    print('O atleta tem {} anos.\nClassificação: JUNIOR'.format(idade))
elif idade > 19 and idade <= 20:
    print('O atleta tem {} anos.\nClassificação: SÊNIOR'.format(idade))
else:
    print('O atleta tem {} anos.\nClassificação: MASTER'.format(idade))
