number = input()
n = int(number[-1])
ostatok = n % 2
i = 0
for u in range(n+1):
    i += u
summa = i % 3
if ostatok == 0 and summa == 0:
    print('True')
else:
    print('False')
