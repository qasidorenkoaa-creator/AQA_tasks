table_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def multiplication_table (table_numbers):
    for multiplier in table_numbers:
        table_strings = " ".join(str(multiplier * n) for n in table_numbers)
        print(table_strings)
multiplication_table (table_numbers)