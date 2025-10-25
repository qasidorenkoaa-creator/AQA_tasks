def count_items(*args):
    count = len(args)
    return count

result1 = count_items(1, 2, 3, 4, 5)
result2 = count_items("apple", "banana", "cherry")

print(f"Количество переданных элементов: {result1}.")
print(f"Количество переданных элементов: {result2}.")