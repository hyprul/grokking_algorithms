def max_(lst):
    if len(lst) == 0:
        return None
    if len(lst) == 1:
        return lst[0]
    else:
        sub_max = max_(lst[1:])
        return lst[0] if lst[0] > sub_max else sub_max


def recmax(list):
    if len(list) == 0:
        return None
    if len(list) == 1:
        # print(list[0])
        return list[0]
    sub_max = recmax(list[1:])
    return list[0] if list[0] > sub_max else sub_max


def recmax2(list):
    if len(list) == 2:
        return [0] if list[0] > list[1] else list[1]
    sub_max = recmax(list[1:])
    return list[0] if list[0] > sub_max else sub_max


list = [1, 2, 2000, 20]

print(recmax2(list))
