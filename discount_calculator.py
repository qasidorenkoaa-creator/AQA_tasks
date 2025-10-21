purchase_sum = input("Введите сумму покупки: ")
discount_percentage = input("Введите процент скидки: ")
saving_sum = int(purchase_sum) * int(discount_percentage) / 100
total_sum = int(purchase_sum) - int(saving_sum)
saving_sum = round(saving_sum, 2)
total_sum = round(total_sum)
print(f"Вы экономите: {saving_sum}")
print(f"Сумма к оплате (округлено): {total_sum}")