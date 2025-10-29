def is_sorted(lst):
    if lst == sorted(lst):
        return True
    else:
        return False


print(is_sorted([1, 2, 3, 4, 5]))
print(is_sorted([1, 3, 2, 4, 5]))


# вариант 2
def is_sorted(lst):
    return lst == sorted(lst)


print(is_sorted([1, 2, 3, 4, 5]))
print(is_sorted([1, 3, 2, 4, 5]))
