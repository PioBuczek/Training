def count(lista1):
    lista2 = []
    for element in lista1:
        if element % 2 == 0:
            lista2.append(element)
    return lista2


lista1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(count(lista1))
