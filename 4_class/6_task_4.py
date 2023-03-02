# Zadacha "Loterya skidok"
price = float(input())
sum = float(0)
while price != 0:
    sum += price
    price = float(input())
if sum%2 == 0:
    while sum%2 != 1:
        sum = sum/2
    print('K oplate: ', sum)
else:
    print('K oplate: ', sum * 0.75)
