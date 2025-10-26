def sum_numbers(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

n = 5
result = sum_numbers(n)
print(f"Сумма чисел от 1 до {n}: {result}")



