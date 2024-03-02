def count(lista1):
    max = lista1[0]
    min = lista1[0]
    for element in lista1[1:]:
        if element < min:
            min = element
        elif element > max:
            max = element
    return (min, max)


lista1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(count(lista1))
