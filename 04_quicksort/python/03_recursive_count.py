def count(list):
    if list == []:
        return 0
    return 1 + count(list[1:])


def count2(list):
    if len(list) == 1:
        return 1
    return 1 + count2(list[1:])


print(count2([1,2,3]))