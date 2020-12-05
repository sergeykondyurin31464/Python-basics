# а) итератор, генерирующий целые числа, начиная с указанного.
# в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл
from itertools import count
for el in count(3):
    if el > 10:
        break
    else:
        print(el)


#C:\Users\Сергей>python D:/PyProjekt/First/Python-basics/Lesson4/hw_4.6.py
#3
#4
#5
#6
#7
#8
#9
#10

#C:\Users\Сергей>