import math
a=float(input('Digite um ângulo:'))
s=float(math.sin(math.radians(a)))
c=float(math.cos(math.radians(a)))
print('O ângulo de {:.2f} possui seno {:.2f} e coseno {:.2f}'.format(a, s, c))

