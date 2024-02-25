def funk(list1):
    dict1 = {
        "niedostateczny": 0,
        "dopuszczajacy": 0,
        "dostateczny": 0,
        "dobry": 0,
        "bardzo dobry": 0,
        "celujacy": 0,
    }
    for element in list1:
        if element == 1:
            dict1["niedostateczny"] += 1
        elif element == 2:
            dict1["dopuszczajacy"] += 1
        elif element == 3:
            dict1["dostateczny"] += 1
        elif element == 4:
            dict1["dobry"] += 1
        elif element == 5:
            dict1["bardzo dobry"] += 1
        elif element == 6:
            dict1["celujacy"] += 1
    return dict1


list1 = [1, 2, 2, 4, 5, 3]

print(funk(list1))
