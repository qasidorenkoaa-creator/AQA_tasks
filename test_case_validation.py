while True:
    test_cases = input("Введите количество тест-кейсов: ")
    if test_cases.isdigit() and int(test_cases) > 0:
        test_cases = int(test_cases)
        break
    else:
        print("Некорректный ввод. Введите положительное число.")
if test_cases > 10:
    print("Отличная работа!")
else:
    print("Попробуйте улучшить результат.")