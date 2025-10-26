# вариант 1
def find_min(numbers):
    min_number = numbers[0]
    for number in numbers:
        if number < min_number:
            min_number = number
    return min_number

numbers = [3, 1, 4, 1, 5]
result = find_min(numbers)

print(f"Минимальное число в списке {numbers}: {result} ")

# вариант 2
def find_min(numbers):
    return min(numbers)

numbers = [3, 1, 4, 1, 5]
result = find_min(numbers)
print(f"Минимальное число в списке {numbers}: {result} ")