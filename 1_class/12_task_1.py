latitude = float(input())
longitude = float(input())
rate = float(input())
volume = int(input())
percent = int(input())

size = latitude * longitude
amount = ((round(size, 2))/rate)*((100 + percent) / 100)
total = amount/volume
n = total % 1
if n != 0:
    total = int(amount//volume) + 1
balance = (total * volume) - amount

print(round(size, 2))
print(round(amount, 2))
print(total)
print(round(balance, 2))