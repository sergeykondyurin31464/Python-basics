# Определение времени года вводимого месяца используя списки
print('enter month number')
mnt = int(input())
wnt = (12, 1, 2)
spr = (3, 4, 5)
smr = (6, 7, 8)
atm = (9, 10, 11)
if mnt in wnt:
    print('winter')
elif mnt in spr:
    print('spring')
elif mnt in smr:
    print('summer')
else:
    print('autumn')



