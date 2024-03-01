def count(lista1, n):
    ilosc = 0
    for x in lista1:
        if x == n:
            ilosc += 1

    return ilosc


lista1 = [1, 2, 3, 4, 2, 2, 3, 1, 4, 4, 4]
while True:
    n = int(input("Podaj cyfre znajdujaca sie w liscie: "))
    if n == -1:
        break

    print(f"Ilość wystąpienia cyfry: {n} wynosi: {count(lista1, n)}")
