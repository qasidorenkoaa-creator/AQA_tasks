tester_statistics = {
    "Artur": 15,
    "Liam": 10,
    "Ben": 12
}
print(f"Исходные данные: {tester_statistics}")
tester_name = input("Введите имя тестировщика:")
if tester_name not in tester_statistics:
    tester_statistics[tester_name] = 1
else:
    tester_statistics[tester_name] += 1
print(f"Обновленные данные: {tester_statistics}")
tester_name = input("Введите имя тестировщика:")
if tester_name not in tester_statistics:
    tester_statistics[tester_name] = 1
else:
    tester_statistics[tester_name] += 1
print(f"Обновленные данные: {tester_statistics}")