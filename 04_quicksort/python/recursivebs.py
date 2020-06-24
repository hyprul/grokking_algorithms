def binarysearch(list, lo, hi, target):

    if lo < hi:
        mid = (lo+hi)//2

        if list[mid] == target:
            return mid
        elif list[mid] > target:
            return binarysearch(list, lo, mid, target)
        else:
            return binarysearch(list, mid, hi, target)

    else:
        return -1


print(binarysearch([1, 2, 3, 4, 5], 0, 5, 4))
