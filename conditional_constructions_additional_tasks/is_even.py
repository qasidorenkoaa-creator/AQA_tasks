def is_even(number):
    return "четным" if number % 2 == 0 else "нечетным"

number1 = 4
number2 = 7

status1 = is_even(number1)
status2 = is_even(number2)

print(f"Число {number1} является {status1}.")
print(f"Число {number2} является {status2}.")
