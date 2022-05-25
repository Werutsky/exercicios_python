import math
co=float(input("Digite o cateto oposto:"))
ca=float(input('Digite o cateto adjacente:'))
h = math.hypot(ca, co)
print('Como o cateto oposto é {} e o cateto adjacente é {} , a hiopotenusa é {:.2f}'.format(co, ca, h))
