# 2. Создать текстовый файл (не программно),
# сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.
my_f = open(r"D:/PyProjekt/First/Python-basics/Lesson5/test_1.txt")
ln = my_f.readlines()
with open('test_1.txt', 'r') as f:
    for index, value in enumerate(ln):
        number_of_words = len(value.split())
print('Line number {} has {} words.\n'.format(index + 1, number_of_words))
my_f.close()
