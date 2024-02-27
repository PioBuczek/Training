def scope(n):
    dict1 = {}
    for x in range(1, n + 1):
        dict1[x] = x * x
    return dict1


print(scope(6))
