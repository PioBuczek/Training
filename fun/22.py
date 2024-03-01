# def count(dict1, dict2):
#     for key, values in dict2.items():
#         if key in dict1:
#             if not isinstance(dict1[key], list):
#                 dict1[key] = [dict1[key]]
#             dict1[key].append(values)
#         else:
#             dict1[key] = [values]

#     return dict1


# dict1 = {"1": "Ania", "2": "Ulka"}
# dict2 = {"1": "Piotrek", "2": "Agata", "3": "sad"}
# print(count(dict1, dict2))


def count(dict1, dict2):
    for key, values in dict2.items():
        if key in dict1:
            dict1[key] += values
        else:
            dict1[key] = values
    return dict1


dict1 = {"1": 1, "2": 2}
dict2 = {"1": 3, "2": 4, "3": 5}
print(count(dict1, dict2))
