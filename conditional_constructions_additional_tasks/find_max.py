def find_max(a, b):
    if a > b:
        return a
    else:
        return b

a = 5
b = 9

result = find_max(a, b)

print(f"Максимальное из чисел {a} и {b}: {result}")