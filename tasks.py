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

# Задача 1
some_numbers_list = [1, 2, 3]
some_numbers_list.append(4)
print(some_numbers_list)

# Задача 2
cities = ["Moscow", "Yerevan", "London"]
cities.remove("London")
print(cities)

# Задача 3
cities2 = ["Moscow", "Yerevan", "London", "Paris"]
print(cities2[2])

# Задача 4
some_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(some_numbers[3:7])

# Задача 5
some_colors = ["red", "green", "blue"]
some_colors[1] = "yellow"
print(some_colors)

# Задача 6
SomeAnimals = ["cat", "dog", "rabbit", "hamster"]
len_SomeAnimals = len(SomeAnimals)
print(len_SomeAnimals)
print(len(SomeAnimals))

# Задача 7
new_student = {
    "name": "Artur",
    "age": 36
}
new_student["grade"] = "A"
print(new_student)

# Задача 8
add_new_student = {
    "name": "Ben",
    "age": 20,
    "grade": "B"
}
add_new_student["grade"] = "A"
print(add_new_student)

# Задача 9
student_information = {
    "name": "Lily",
    "age": 25,
    "grade": "A"
}
del student_information["age"]
print(student_information)

# Задача 10
some_student = {
    "name": "Lily",
    "age": 25,
    "grade": "A"
}
print(some_student["name"])

# Задача 11
student_details = {
    "name": "Alex",
    "age": 25,
    "grade": "A"
}
print("grade" in student_details)
if "grade" in student_details:
    print(f'Ключ "grade" найден в словаре')
else:
    print(f'Ключ "grade" не найден в словаре')

# Задача 12
edit_student_information = {
    "name": "Masha",
    "adress": {
        "city": "Moscow",
        "street": "Nikolskaya"
    }
}
edit_student_information["adress"]["city"] = "Saint Petersburg"
print(edit_student_information)

# Задача 13
student_grade_information = {
    "name": "Kirill",
    "grades": [75, 82, 90]
}
student_grade_information["grades"][0] = 85
print(student_grade_information)

# Задача 14
new_student_list = [
    {
    "name": "Vasya",
    "age": 26
    },
    {
    "name": "Galya",
    "age": 27
    }
]
new_student_list[1]["age"] = 28
print(new_student_list)

# Задание 15
colors_list = ("red", "green", "blue")
print("green" in colors_list)
print(len(colors_list))



