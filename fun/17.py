def count(lista1):
    dict1 = {}
    for element in lista1:
        key = len(element)
        if key not in dict1:
            dict1[key] = [element]
        else:
            dict1[key].append(element)
    return dict1


lista1 = ["sada", "Ania", "Ania", "Piotrek", "Agata"]
print(count(lista1))
