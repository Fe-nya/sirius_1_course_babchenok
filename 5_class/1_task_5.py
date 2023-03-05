igra = input()
l = []
while igra != '0':
    if igra in l:
        print('Eta igra yje zapisana')
    else:
        l.append(igra)
    igra = input()
l.sort()
print(l)
