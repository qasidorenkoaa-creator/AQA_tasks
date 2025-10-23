def some_numbers ():
    number_n = int(input(f"Введите число: "))
    print("Числа:", end=" ")
    for initial_num in range(1, number_n + 1):
        print(initial_num, end=" ")
    print()
    total = 0
    initial_num = 1
    while initial_num <= number_n:
        total += initial_num
        initial_num += 1
    print("Сумма чисел:", total)
some_numbers ()

# второй способ
def some_numbers():
    number_n = int(input("Введите число: "))
    total = 0
    print("Числа:", end=" ")
    for initial_num in range(1, number_n + 1):
        print(initial_num, end=" ")
        total += initial_num
    print(f"\nСумма чисел: {total}")
some_numbers()