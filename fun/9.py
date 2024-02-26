def start(list1):
    dict1 = {}
    for element in list1:
        if element[0] not in dict1:
            dict1[element[0]] = [element]
        else:
            dict1[element[0]].append(element)
    return dict1


list1 = ["Piotr", "Michał", "Ania", "Paweł", "Anita", "Ala"]
print(start(list1))
