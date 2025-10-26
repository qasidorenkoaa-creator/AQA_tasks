def check_string_length(string, length):
    if len(string) > length:
        return "достаточная"
    else:
        return "слишком короткая"

string1 = '"Python"'
string2 = '"Hi"'
length = 5
result1 = len(string1)
result2 = len(string2)

status1 = check_string_length(string1, length)
status2 = check_string_length(string2, length)

print(f"Длина строки {string1} {status1}.")
print(f"Длина строки {string2} {status2}.")