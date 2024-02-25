list1 = ["a1", "a2", "a3"]
list2 = ["b1", "b2", "b3"]
list3 = []

for x in range(len(list1)):
    list3.append(list1[x])
    list3.append(list2[x])
print(list3)
