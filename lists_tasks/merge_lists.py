def merge_lists(list1, list2):
    list1.extend(list2)
    new_list = list(set(list1))
    return new_list


print(merge_lists([1, 2, 3], [3, 4, 5]))

# вариант 2
def merge_lists(list1, list2):
    return list(set(list1) | set(list2))


print(merge_lists([1, 2, 3], [3, 4, 5]))