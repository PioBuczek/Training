def elementy(list):
    dict = {}
    for element in list:
        dict[element] = len(element)
    return dict


list = ["apple", "orange"]
print(elementy(list))
