def count(string1):
    dict1 = {}
    for element in string1.lower():
        if element not in dict1:
            dict1[element] = 1
        else:
            dict1[element] += 1
    return dict1


string1 = input("Podaj ciag znakow: ")
print(count(string1))
