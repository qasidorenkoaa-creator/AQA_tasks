# 4. Переменные
F = 100
C = (F-32)*5/9
C = round(C, 2)
text1 = "градусов по Фаренгейту равняется"
text2 = "по Цельсию."
print(F, text1, f"{C:.2f}", text2)
solution = f"{F} градусов по Фаренгейту равняется {C} по Цельсию."
print(solution)

# 5. Операции с данными

# Задача 1
grams = 12345
kilograms = grams // 1000
full_kilograms = f"В {grams} граммах содержится {kilograms} полных килограмм."
print(full_kilograms)

# Задача 2
number = 1234
last_digit = number - 1230
last_digit = number % 10
solution = f"Последняя цифра числа {number}: {last_digit}"
print(solution)

# Задача 3
number1 = 14
print(number1 > 0 and number1 % 2 == 0)
number2 = -4
print(number2 > 0 and number2 % 2 == 0)
number3 = 15
print(number3 > 0 and number3 % 2 == 0)

if number1 > 0 and number1 % 2 == 0:
    print(f"Число {number1} является положительным и четным")
else:
    print(f"Число {number1} не подходит под условия")
if number2 > 0 and number2 % 2 == 0:
    print(f"Число {number2} является положительным и четным")
else:
    print(f"Число {number2} не подходит под условия")
if number3 > 0 and number3 % 2 == 0:
    print(f"Число {number3} является положительным и четным")
else:
    print(f"Число {number3} не подходит под условия")

# Задача 4
num1 = 150
num2 = 50
num3 = -20
if num1 >= 0 and num1 <= 100:
    print(f"Число {num1} находится в пределах диапазона от 0 до 100")
else:
    print(f"Число {num1} выходит за пределы диапазона от 0 до 100")
if num2 >= 0 and num2 <= 100:
    print(f"Число {num2} находится в пределах диапазона от 0 до 100")
else:
    print(f"Число {num2} выходит за пределы диапазона от 0 до 100")
if num3 >= 0 and num3 <= 100:
    print(f"Число {num3} находится в пределах диапазона от 0 до 100")
else:
    print(f"Число {num3} выходит за пределы диапазона от 0 до 100")

# Задача 5
num1 = 10
num2 = 9
if num1 % 3 == 0:
    print(f"Число {num1} кратно 3")
else:
    print(f"Число {num1} не кратно 3")
if num2 % 3 == 0:
    print(f"Число {num2} кратно 3")
else:
    print(f"Число {num2} не кратно 3")

