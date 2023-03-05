o = [5, 3, 2, 4]
ysp = o[1] + o[2] + o[3] + o[0]
ysp = ysp / 4 * 100
o = list(map(str, o))
print(' Spisok ochenok:', ', '.join(o), '\n',
'Kolichestvo ochenok:', len(o), '\n',
'Yspevaemost:', ysp, '\n')

