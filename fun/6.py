def count(slownik_poczatkowy):
    dict1 = {}
    for key, values in slownik_poczatkowy.items():
        dict1[key] = sum(values)
    return dict1


slownik_poczatkowy = {"klucz1": [1, 2, 3], "klucz2": [4, 5, 6], "klucz3": [7, 8, 9]}

print(count(slownik_poczatkowy))
