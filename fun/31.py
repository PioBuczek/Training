def count(zmienna):
    dict1 = {}
    for element in zmienna.split():
        if element not in dict1:
            dict1[element] = 1
        else:
            dict1[element] += 1
    return dict1


zmienna = "Cos tam sobie rosnie rosnie Cos "
print(count(zmienna))
