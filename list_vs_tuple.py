some_numbers_l = [4, 7, 9, 2, 5]
print("Исходный список:", some_numbers_l)
some_numbers_t = (4, 7, 9, 2, 5)
print("Исходный кортеж:", some_numbers_t)

some_numbers_l[1] = 10
print("Измененный список:", some_numbers_l)
try:
    some_numbers_t[1] = 10
except TypeError:
    print("Ошибка: Кортеж нельзя изменить!")

some_numbers_l.append(6)
print("Добавленный элемент в список:", some_numbers_l)
try:
    some_numbers_t.append(6)
except AttributeError:
    print("Ошибка: В кортеж нельзя добавить элемент!")