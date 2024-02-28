def count(lista1):
    dict1 = {}
    for element in lista1:
        if element not in dict1:
            dict1[element] = 1
        else:
            dict1[element] += 1
    zmienna = max(dict1.values())
    for key, value in dict1.items():
        if value == zmienna:
            return key


lista1 = ["Piotrek", "Ania", "Ania", "Piotrek", "Agata"]
print(count(lista1))
