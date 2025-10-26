def check_number(number):
    if number > 0:
        if number % 2 == 0:
            return "положительное и четное"
        else:
            return "положительное и нечетное"
    else:
        return "отрицательное"


number1 = 8
number2 = -5

status1 = check_number(number1)
status2 = check_number(number2)

print(f"Число {number1} {status1}.")
print(f"Число {number2} {status2}.")