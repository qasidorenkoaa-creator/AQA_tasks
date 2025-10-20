print("Добро пожаловать в систему управления багами!")
bug_reports = ["Ошибка 3 - Medium", "Ошибка 1 - Highest", "Ошибка 2 - High",  "Ошибка 4 - Low", "Ошибка 5 - Lowest"]
print("Список баг-репортов:")
for bug in bug_reports:
    print("*", bug)

bug_reports.append("Ошибка 6 - Trivial")
print("Дополненный список баг-репортов:")
for bug in bug_reports:
    print("*", bug)

priority_order = ["Highest", "High", "Medium", "Low", "Lowest", "Trivial"]
sorted_bugs = []

for priority in priority_order:
    for i in range(len(bug_reports)):
        if priority in bug_reports[i]:
            if bug_reports[i] not in sorted_bugs:
                sorted_bugs.append(bug_reports[i])

print("Обновленный список багов, отсортированный по приоритетам:")
for bug in sorted_bugs:
    print("*", bug)

sorted_bugs.remove("Ошибка 4 - Low")
sorted_bugs.remove("Ошибка 5 - Lowest")
sorted_bugs.remove("Ошибка 6 - Trivial")
print("Обновленный список баг-репортов без низких приоритетов:")
for bug in sorted_bugs:
    print("*", bug)



