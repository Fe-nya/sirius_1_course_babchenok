start = input()
while start != 'off':
    print('Vvedite "game"')
    start = input()
    if start == 'game':
        for i in range(3):
            num = input('Vvedite chislo: ')
            if num == '5':
                print('Vy vyigrali bilet na koncern!')
                break
