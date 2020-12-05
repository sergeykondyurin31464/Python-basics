# 5. Создать (программно) текстовый файл,
# записать в него программно набор чисел,
# разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open("D:/PyProjekt/First/Python-basics/Lesson5/5.5.txt", 'w', encoding='utf-8') as f:
    numbers = input(' enter numbers ')
    f.write(' enter numbers: ' + numbers + '\n')
    a = map(int, numbers.split())
    s_nums = sum(a)
    f.write('sum of numbers: ' + str(s_nums))
    print('sum of entered numbers:', s_nums)

