def dict(slownik):
    dictiona = {}
    for key, values in slownik.items():
        dictiona[values] = key
    return dictiona


slownik = {"apple": 5, "orange": 6}
print(dict(slownik))
