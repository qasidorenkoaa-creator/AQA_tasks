default_log = " Ошибка: тест не пройден из-за ошибки в модуле auth "
log_string = input(f"Введите строку лога ({default_log}):")
if not log_string:
    log_string = default_log
log_string = log_string.strip().replace("Ошибка", "Ошибка критическая", 1)
words_list = log_string.split()
print("Обработанная строка:", log_string)
print("Разбитый текст:", words_list)