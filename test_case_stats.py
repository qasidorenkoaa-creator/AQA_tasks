print("Подсчёт статистики по тест-кейсам за неделю")
monday_tests = int(input("Сколько тест-кейсов вы выполнили в понедельник? "))
tuesday_tests = int(input("А во вторник? "))
wednesday_tests = int(input("А в среду? "))
thursday_tests = int(input("А в четверг? "))
friday_tests = int(input("А в пятницу? "))
saturday_tests = int(input("А в субботу? "))
sunday_tests = int(input("А в воскресенье? "))
total_tests = monday_tests + tuesday_tests + wednesday_tests + thursday_tests + friday_tests + saturday_tests + sunday_tests
average_tests = total_tests // 7
print(f"Общее количество тестов за неделю: {total_tests}")
print(f"Среднее количество тестов в день: {average_tests}")
if average_tests  > 10:
    print("Отличная работа!")
else:
    print("Попробуйте улучшить свой результат.")