lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def average(lista1):
    avg = sum(lista1) / len(lista1)
    lista2 = []
    for number in lista1:
        if number > avg:
            lista2.append(number)
    return lista2


lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(average(lista1))
