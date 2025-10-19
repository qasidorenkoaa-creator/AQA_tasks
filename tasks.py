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
GRAMS = 12345
kilograms = GRAMS // 1000
full_kilograms = f"В {GRAMS} граммах содержится {kilograms} полных килограмм."
print(full_kilograms)

# Задача 2
SOME_NUMBER = 1234
last_digit = SOME_NUMBER - 1230
last_digit = SOME_NUMBER % 10
solution = f"Последняя цифра числа {SOME_NUMBER}: {last_digit}"
print(solution)

# Задача 3
SOME_NUMBER1 = 14
print(SOME_NUMBER1 > 0 and SOME_NUMBER1 % 2 == 0)
SOME_NUMBER2 = -4
print(SOME_NUMBER2 > 0 and SOME_NUMBER2 % 2 == 0)
SOME_NUMBER3 = 15
print(SOME_NUMBER3 > 0 and SOME_NUMBER3 % 2 == 0)

if SOME_NUMBER1 > 0 and SOME_NUMBER1 % 2 == 0:
    print(f"Число {SOME_NUMBER1} является положительным и четным")
else:
    print(f"Число {SOME_NUMBER1} не подходит под условия")
if SOME_NUMBER2 > 0 and SOME_NUMBER2 % 2 == 0:
    print(f"Число {SOME_NUMBER2} является положительным и четным")
else:
    print(f"Число {SOME_NUMBER2} не подходит под условия")
if SOME_NUMBER3 > 0 and SOME_NUMBER3 % 2 == 0:
    print(f"Число {SOME_NUMBER3} является положительным и четным")
else:
    print(f"Число {SOME_NUMBER3} не подходит под условия")

# Задача 4
SOME_NUMBER1 = 150
SOME_NUMBER2 = 50
SOME_NUMBER3 = -20
if SOME_NUMBER1 >= 0 and SOME_NUMBER1 <= 100:
    print(f"Число {SOME_NUMBER1} находится в пределах диапазона от 0 до 100")
else:
    print(f"Число {SOME_NUMBER1} выходит за пределы диапазона от 0 до 100")
if SOME_NUMBER2 >= 0 and SOME_NUMBER2 <= 100:
    print(f"Число {SOME_NUMBER2} находится в пределах диапазона от 0 до 100")
else:
    print(f"Число {SOME_NUMBER2} выходит за пределы диапазона от 0 до 100")
if SOME_NUMBER3 >= 0 and SOME_NUMBER3 <= 100:
    print(f"Число {SOME_NUMBER3} находится в пределах диапазона от 0 до 100")
else:
    print(f"Число {SOME_NUMBER3} выходит за пределы диапазона от 0 до 100")

# Задача 5
SOME_NUMBER1 = 10
SOME_NUMBER2 = 9
if SOME_NUMBER1 % 3 == 0:
    print(f"Число {SOME_NUMBER1} кратно 3")
else:
    print(f"Число {SOME_NUMBER1} не кратно 3")
if SOME_NUMBER2 % 3 == 0:
    print(f"Число {SOME_NUMBER2} кратно 3")
else:
    print(f"Число {SOME_NUMBER2} не кратно 3")

# 6. Коллекции данных
