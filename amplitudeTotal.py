import math
ultimoElemento = input("Qual o ultimo elemento da tabela?")
primeiroElemento = input("Qual o primeiro elemento da tabela?")
nElementos = input("Quantos elementos no total?")
nElementos = int(nElementos)
ultimoElemento = float(ultimoElemento)
primeiroElemento = float(primeiroElemento)

at = ultimoElemento - primeiroElemento

k = 0
k = math.log(nElementos, 10)
# print(k)
k = k * 3.322
k = k + 1
# print(k)
k = math.ceil(k)
# print(k)
ai = at/k
provareal = ai * k
if provareal < ultimoElemento:
    ai + 0.01;
print(ai)
for i in range(k):
    print(round(primeiroElemento, 2), "|---", round(primeiroElemento + ai, 2))
    primeiroElemento = primeiroElemento + ai
# print(round(ac, 2));