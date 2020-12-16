# Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение

from math import factorial
print('enter n')
n = int(input())
my_list = [el for el in range(1, n + 1)]
def fact_gen():
    for el in my_list:
        yield factorial(el)

gen = fact_gen()
print(gen)
for el in gen:
    print(el)


