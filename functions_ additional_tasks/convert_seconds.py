import math
def convert_seconds (seconds):
    hours = seconds // 3600
    remaining_seconds = seconds % 3600
    minutes = math.ceil(remaining_seconds / 60)
    if minutes == 60:
        hours += 1
        minutes = 0
    return hours, minutes

seconds = 3672
hours, minutes = convert_seconds(seconds)

print(f"В {seconds} секундах содержится {hours} час(ов) и {minutes} минут(ы).")