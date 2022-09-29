


def sum(list):
    sum = 0
    x = 0
    for x in range(len(list)):
        sum += list[x]
    return print(sum)

def average(list):
    number = 0
    sum = 0
    x = 0
    y = 0
    for x in range(len(list)):
        number += x
        sum += list[x]
    return print(sum/number)
