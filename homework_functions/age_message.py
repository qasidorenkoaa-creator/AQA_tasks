def user_bio ():
    year_birth = input("Введите год вашего рождения: ")
    from datetime import datetime
    current_year = datetime.now().year
    age = int(current_year) - int(year_birth)
    print(f"Ваш возраст: {age}")
    if age < 18:
        print("Вы еще молоды, учеба — ваш путь!")
    if 18 <= age <= 65:
        print("Отличный возраст для карьерного роста!")
    if age > 65:
        print("Пора наслаждаться заслуженным отдыхом!")
user_bio()
