def count(lista1, lista2):
    lista3 = []
    for element in lista1:
        if element in lista2:
            lista3.append(element)
    return lista3


lista1 = ["Ania", "Piotrek", "Agata"]
lista2 = ["Ania", "Piotrek", "Agata", "Andrzej"]
print(count(lista1, lista2))
