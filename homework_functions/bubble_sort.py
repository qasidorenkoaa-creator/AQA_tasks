def bubble_sort(numbers):
    num_elements = len(numbers)
    for num_iteration in range(num_elements):
        for index in range(0, num_elements - num_iteration - 1):
            if numbers[index] > numbers[index + 1]:
                numbers[index], numbers[index + 1] = numbers[index + 1], numbers[index]
    return numbers

input_str = input("Введите числа через запятую: ")
numbers = [int(num.strip()) for num in input_str.split(",")]
sorted_numbers = bubble_sort(numbers)
print("Отсортированный список:", ", ".join(str(num) for num in sorted_numbers))