def check_grade(score):
    if 90 <= score <= 100:
        return "Отлично"
    elif 75 <= score <= 89:
        return "Хорошо"
    elif 50 <= score <= 74:
        return "Удовлетворительно"
    else:
        score < 50
        return "Неудовлетворительно"

score = 85

status = check_grade(score)

print(f"Оценка за {score} баллов: {status}.")