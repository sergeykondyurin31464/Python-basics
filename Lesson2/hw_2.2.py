# Обмен значениями соседних элементов списка
print('Enter the data')
a = input()
print('Enter the data')
a_1 = input()
print('Enter the data')
a_2 = input()
print('Enter the data')
a_3 = input()
print('Enter the data')
a_4 = input()
d = [a, a_1, a_2, a_3, a_4]
print(d)
n = 0
for i in range(int(len(d)/2)):
    d[n], d[n + 1] = d[n + 1], d[n]
    n += 2
print(d)

