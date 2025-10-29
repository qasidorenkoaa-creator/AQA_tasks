def remove_duplicates(lst):
    new_lst = []
    return [char for char in lst if not (char in new_lst or new_lst.extend([char]))]


print(remove_duplicates([1, 2, 2, 3, 4, 4]))


# вариант 2
def remove_duplicates(lst):
    unique_chars = []
    for char in lst:
        if char not in unique_chars:
            unique_chars.append(char)
    return unique_chars


print(remove_duplicates([1, 2, 2, 3, 4, 4]))
