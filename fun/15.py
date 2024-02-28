import random


def count(n):
    lista1 = []
    for x in range(n):
        slownik = {"index": x, "value": random.randint(1, 100)}
        lista1.append(slownik)
    return lista1


print(count(5))
