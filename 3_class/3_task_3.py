# Задача "Новая акция" в магазине "Долголетие"
one = int(input('Vvedite pervyi ceny: '))
two = int(input('Vvedite vtoryi ceny: '))
three = int(input('Vvedite tretiyi ceny: '))
count = one + two + three
if one < two < three:
    count = count / 2
elif one > two > three:
    count = count / 3
print(count)
