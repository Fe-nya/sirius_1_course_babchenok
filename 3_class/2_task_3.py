# Задача "Счастливые часы" в магазине "Долголетие"
hour = float(input('Сумма к оплате: '))
time = int(input('Какой сейчас час: '))
if 10 <= time <= 12:
    print(hour / 2)
elif 20 <= time <= 22:
    print(hour / 4)
elif time < 8 or time > 22:
    print('"Долголетие" сейчас не работает! Часы работы с 8 до 22')
else:
    print(hour)
