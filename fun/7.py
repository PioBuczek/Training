"""solution 1 :"""

# def uniqly(list1):
#     list2 = []
#     for element in list1:
#         if element not in list2:
#             list2.append(element)
#         else:
#             continue
#     return list2


# list1 = ["owca", "owca", "krowa", "slon"]

# print(uniqly(list1))
"""solution 2 :"""


def uniqly(list1):
    set1 = list(set(list1))
    return set1


list1 = ["owca", "owca", "krowa", "slon"]

print(uniqly(list1))
