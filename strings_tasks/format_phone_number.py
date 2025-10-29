def format_phone_number(digits):
    digits = list(digits)
    to_insert = [(0, "("), (3, ") "), (6, "-")]

    for index, value in sorted(to_insert, reverse=True):
        digits.insert(index, value)
    return "".join(digits)


print(format_phone_number("1234567890"))
