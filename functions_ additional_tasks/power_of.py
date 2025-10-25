def power_of (number1, number2, exponent1, exponent2):
    exponent1 = exponent1 or 2
    exponent2 = exponent2 or 2
    result1 = number1 ** exponent1
    result2 = number2 ** exponent2
    return number1, number2, exponent1, exponent2, result1, result2

number1, number2, exponent1, exponent2, result1, result2 = power_of(3, 5, 4, None)

print(f"Число {number1} в степени {exponent1} равно {result1}.")
print(f"Число {number2} в степени {exponent2} равно {result2}.")
