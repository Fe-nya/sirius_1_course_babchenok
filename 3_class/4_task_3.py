# Задача "Рекомендации товаров"
n = input('Vvedite kategoriy tovarov: ').lower()
if n == 'продукты':
    c = int(input('Skol`ko y vas deneg: '))
    if c < 100:
        print('Poprobyite nashy vypechky!')
    elif 100 <= c < 500:
        print('Kak naschet orexov v shokolade?')
    elif c <= 500:
        print('Poprobyite ekzoticheskie tovary!')
else:
    print('Zaglyanite v tovary dlya doma')
