user_name = input("Введите ваше имя: ")
print(f"Привет, {user_name}! Добро пожаловать в мир Python для тестировщиков.")
user_profession = input("Введите вашу профессию: ")
user_experience_period_QA = input("Сколько лет вы работаете в сфере QA?: ")
print(f"Супер! тогда проверим ваши знания)")
what_is_variable = input("Что такое переменная?: ")
if "область памяти" in what_is_variable.lower() or "имя" in what_is_variable.lower():
    print("Правильно! Переменная — это область памяти компьютера, у которой есть имя.")
else:
    print("Не совсем верно. Переменная — это область памяти компьютера, у которой есть имя.")
print("Спасибо за участие!")