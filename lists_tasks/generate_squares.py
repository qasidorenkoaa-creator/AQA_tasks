def generate_squares(n):
    return [number ** 2 for number in range(1, n + 1)]


print(generate_squares(5))
