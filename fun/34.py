def count(zmienna):
    zmienna = zmienna.split()
    zmienna1 = zmienna[::-1]
    return " ".join(zmienna1)


zmienna = "Cos tam ktos tam"
print(count(zmienna))
