# in place selection sort


def selection_sort(list):

    for i in range(len(list)):
        min_index = i
        for j in range(i+1, len(list)):
            if list[min_index] > list[j]:
                min_index = j

        list[i], list[min_index] = list[min_index], list[i]
        # print(list)
    return list


test = [5, 1, 3, -1, 10, 2, 5, 20]
print(selection_sort(test))
