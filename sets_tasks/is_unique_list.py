def is_unique_list(lst):
    return lst == list(set(lst))


print(is_unique_list([1, 2, 3, 4]))
print(is_unique_list([1, 2, 2, 3]))


# второй вариант
def is_unique_list(lst):
    return len(lst) == len(set(lst))


print(is_unique_list([1, 2, 3, 4]))
print(is_unique_list([1, 2, 2, 3]))
