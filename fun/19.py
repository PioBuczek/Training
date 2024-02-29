def count(dict1, dict2):
    for key, values in dict2.items():
        dict1[key] = values
    return dict1


dict1 = {"imie": "Ania", "nazwisko": "Buczek"}
dict2 = {"imie": "Piotr", "nazwisko1": "Buczek"}
print(count(dict1, dict2))
