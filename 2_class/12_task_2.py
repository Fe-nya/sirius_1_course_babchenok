n = input()
n = n.replace('&nbsp;', '')
one = n.find('>')
two = n.rfind('<')
n = n[one + 1:two - 1]
print(int(n) + 1)
