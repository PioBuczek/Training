def count(lista1):
    lista2 = []
    for element in lista1:
        if isinstance(element, list):
            lista2.extend(count(element))
        else:
            lista2.append(element)
    return lista2


lista1 = ["Ania", "Piotrek", ["Aga", "Basia"]]
print(count(lista1))
