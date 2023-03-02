symb = ['=', '?', '*', '^', '$', '№', '@', '_']
log = input()
for n in symb:
    for i in log:
        if n == i:
            print(n)
