def count(number):
    sum = 0
    for x in str(number):
        sum += int(x)
    return sum


number = int(input("Podaj liczbe: "))
print(count(number))
