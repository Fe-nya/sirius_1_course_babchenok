l = input().split()
l = list(map(int, l))
c = l[0]
key = 1
if len(l) == 1:
    print('No')
else:
    for i in range(l[1], len(l)):
        if i > c and i == (c + 1):
            key += 1
        c += 1
if key == len(l):
    print('Yes')
else:
    print('No')
