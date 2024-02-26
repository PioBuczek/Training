def count(list1):
    sum = 0
    for index, element in enumerate(list1):
        if index % 2 == 0:
            sum += element
    return sum


list1 = [1, 23, 454, 42, 43, 50]
print(count(list1))
