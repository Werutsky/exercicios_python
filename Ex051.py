print("="*20)
print('10 TERMOS DE UMA PA')
print('='*20)
primeiro = int(input('Primeiro número:'))
razao = int(input('Razão:'))
decimo = primeiro + (10 - 1) * razao
for c in range (primeiro, decimo + razao, razao):
    print('{}'.format(c), end= ' -> ')
print('ACABOU')