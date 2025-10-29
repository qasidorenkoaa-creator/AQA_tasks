def merge_lists(list1, list2):
    return [number1 + number2 for number1, number2 in zip(list1, list2)]


print(merge_lists([1, 2, 3], [4, 5, 6]))

# второй способ
def merge_lists(list1, list2):
    return [list1[i] + list2[i] for i in range(len(list2))]


print(merge_lists([1, 2, 3], [4, 5, 6]))


# третий способ
def merge_lists(list1, list2):
    element1 = list1[0] + list2[0]
    element2 = list1[1] + list2[1]
    element3 = list1[2] + list2[2]
    new_list = element1, element2, element3
    return list(new_list)


print(merge_lists([1, 2, 3], [4, 5, 6]))