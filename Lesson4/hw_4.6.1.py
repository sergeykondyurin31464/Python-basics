# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
from itertools import cycle
my_list = []
с = 0
for el in cycle(my_list):
    if с >= len(my_list):
        break
    print(el)
    с += 1
