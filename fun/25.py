# def anagram(wyraz1, wyraz2):
#     if len(wyraz1) != len(wyraz2):
#         return False
#     return sorted(wyraz1) == sorted(wyraz2)


def anagram(wyraz1, wyraz2):
    dict1 = {}
    dict2 = {}
    if len(wyraz1) != len(wyraz2):
        return False
    for element in wyraz1:
        if element not in dict1:
            dict1[element] = 1
        else:
            dict1[element] += 1
    for element in wyraz2:
        if element not in dict2:
            dict2[element] = 1
        else:
            dict2[element] += 1
    if dict1 == dict2:
        return True
    else:
        return False


wyraz1 = input("Podaj pierwszy wyraz: ").lower()
wyraz2 = input("Podaj drugi wyraz: ").lower()
print((anagram(wyraz1, wyraz2)))
