def count(list1):
    list2 = []

    for element in list1:
        if element % 2 == 0:
            list2.append(element)
    return list2


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]


print(count(list1))
