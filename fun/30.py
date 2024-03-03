import math


def primary(n):
    if n < 2:
        return "It's not primary number"
    if n == 2:
        return True
    if n > 2:
        if n % 2 == 0:
            return "It's not primary number"
        else:
            for i in range(2, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    return "It's not primary number"

            return True


print(primary(6))
