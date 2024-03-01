def count(lista1):
    temp = lista1[0]
    lista1[0] = lista1[-1]
    lista1[-1] = temp
    return lista1


lista1 = [1, 2, 3, 4, 2, 2, 3, 1, 4, 4, 4]
print(count(lista1))
