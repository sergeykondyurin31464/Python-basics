# 3. Создать текстовый файл (не программно),
# построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

my_f = open("D:/PyProjekt/First/Python-basics/Lesson5/5.3.txt", "w")
str_list = ['Putin  100000\n', 'Merkel 40000\n', 'Trump 3000\n']
my_f.writelines(str_list)
my_f.close()
my_f = open("D:/PyProjekt/First/Python-basics/Lesson5/5.3.txt", "r")
ln = my_f.readlines()
print(ln)
with open("D:/PyProjekt/First/Python-basics/Lesson5/5.3.txt", 'r', encoding='utf-8') as f:
   workers = {}
   num = []
   sail = []
   for line in f:
        key, value = line.split()
        workers[key] = value
        sail.append(int(value))
        if int(value) < 20000:
         print(f'{key}: зарплата меньше 20000')
a = float(sum(sail) / len(sail))
print(f'{a}: средняя зарплата сотрудников')




