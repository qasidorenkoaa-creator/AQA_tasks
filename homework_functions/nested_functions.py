def calculator():
    while True:
        value = input("Введите первое число: ")
        try:
            number1 = int(value)
            break
        except ValueError:
            try:
                number1 = float(value)
                break
            except ValueError:
                print("Ошибка! Допускается ввод только чисел. Попробуйте ещё раз.")

    while True:
        value = input("Введите второе число: ")
        try:
            number2 = int(value)
            break
        except ValueError:
            try:
                number2 = float(value)
                break
            except ValueError:
                print("Ошибка! Допускается ввод только чисел. Попробуйте ещё раз.")

    operators = str(input("Выберите операцию (+, -, *, /):"))
    if operators == "+":
        result = number1 + number2
        print(f"Результат: {result}")
    elif operators == "-":
        result = number1 - number2
        print(f"Результат: {result}")
    elif operators == "*":
        result = number1 * number2
        print(f"Результат: {result}")
    elif operators == "/":
        if number2 != 0:
            result = number1 / number2
            if result.is_integer():
                print(f"Результат: {int(result)}")
            else:
                print(f"Результат: {result}")
        else:
            print("Ошибка! Деление на ноль не допускается.")
    else:
        print("Ошибка! Введен некорректный оператор.")
calculator()
