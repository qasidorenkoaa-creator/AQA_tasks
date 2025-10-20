user_name = input("Введите ваше имя: ")
if not user_name:
    print("Имя не указано. Попробуйте снова!")
else:
    print(f"Привет, {user_name}!")
user_profession = input("Введите вашу профессию: ")
if not user_profession:
    print("Профессия не указана. Попробуйте снова!")
else:
    print(f"Отлично, {user_profession} - 'это интересная профессия!")
favourite_tool_fot_testing = input("Введите ваш любимый инструмент для тестирования: ")
if not favourite_tool_fot_testing:
    print("Инструмент не указан. Попробуйте снова!")
else:
    print(f"Ваш любимый инструмент: {favourite_tool_fot_testing}. Отличный выбор!")
print("Спасибо за ответы!")