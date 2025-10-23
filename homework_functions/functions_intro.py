def greet_user():
    name = input("Введите ваше имя: ")
    print(f"Привет, {name}! Добро пожаловать в мир Python!")
greet_user()
def calculate_sum():
    a = input("Введите первое число: : ")
    b = input("Введите второе число: : ")
    sum_vars = int(a) + int(b)
    print(f"Сумма чисел: {sum_vars}")
calculate_sum ()

# второй способ
def greet_user(name):
    print(f"Привет, {name}! Добро пожаловать в мир Python!")

def calculate_sum(a, b):
    sum_vars = int(a) + int(b)
    print(f"Сумма чисел: {sum_vars}")

user_name = input("Введите ваше имя: ")
greet_user(user_name)

first = input("Введите первое число: ")
second = input("Введите второе число: ")
calculate_sum(first, second)