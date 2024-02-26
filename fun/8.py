def common_list(list1, list2):
    list3 = []
    for element in list1:
        if element in list2:
            list3.append(element)
    return list3


list1 = ["slon", "owca", "krowa"]
list2 = ["slon", "kot", "pies", "krowa"]

print(common_list(list1, list2))
