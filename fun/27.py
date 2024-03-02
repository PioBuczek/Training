def count(lista1):
    lista2 = []
    for element in lista1:
        if element not in lista2:
            lista2.append(element)
    return lista2


lista1 = ["Ania", "Basia", "Ania", "Piotrek", "Basia", "Piotrek"]

print(count(lista1))
