# Вывести нумерованный список введенных слов в строке , не более 10 символов в слове.
print('enter str')
s = input()
word = []
n = 1
for el in range(s.count(' ') + 1):
    word = s.split()
    if len(str(word)) <= 10:
        print(f'{n} {word [el]}')
        n += 1
    else:
        print(f'{n} {word [el] [0:10]}')
        n += 1

