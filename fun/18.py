def count(lista1):
    for number in range(len(lista1) - 1):
        if lista1[number] > lista1[number + 1]:
            return False
    return True


lista1 = [1, 2, 6, 23, 1, 3, 5, 8]
print(count(lista1))
