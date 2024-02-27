def uniqly(dict1):
    counts = {}
    for values in dict1.values():
        if values not in counts:
            counts[values] = 1
        else:
            counts[values] += 1
    list1 = []
    for keys, values in counts.items():
        if values == 1:
            list1.append(keys)
    return list1


dict1 = {
    "klucz1": "wartość1",
    "klucz2": "wartość2",
    "klucz3": "wartość1",
    "klucz4": "wartość3",
    "klucz5": "wartość4",
    "klucz6": "wartość4",
}
print(uniqly(dict1))
