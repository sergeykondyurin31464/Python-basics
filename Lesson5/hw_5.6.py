# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.
my_dict = dict()
with open("D:/PyProjekt/First/Python-basics/Lesson5/5.6.txt", 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        splitted_line = line.split()
        subject = splitted_line[0]
        sum_lessons = sum([int(x[:x.find('(')]) for x in splitted_line[1:] if '(' in x])
        my_dict[subject[:-1]] = sum_lessons
    print(my_dict)

