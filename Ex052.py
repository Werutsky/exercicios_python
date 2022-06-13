num = int(input('Digite um número:'))
tot= 0
for c in range (1, num+1):
    if num % c == 0:
        print('\033[34m {}'.format(c), end= ' ')
        tot += 1
    else:
        print('\033[33m {}'.format(c), end= ' ')
print('\n\033[mO número {} foi divisível {} vezes.'.format(num, tot))
if tot > 2:
    print('O número {} não é primo!'.format(num))
else:
    print('O número {} é primo!'.format(num))


