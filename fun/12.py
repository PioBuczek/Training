import random


def choosen(lista1):
    choose = random.randint(0, len(lista1) - 1)
    return lista1[choose]


lista1 = ["Ania", "Piotrek"]
print(choosen(lista1))
