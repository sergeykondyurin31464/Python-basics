# Bывести элементы исходного списка,
# значения которых больше предыдущего элемента.
my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(F"My list: {my_list}")
new_list = [my_list[i] for i in range(1, len(my_list))
            if my_list[i] > my_list[i-1]]
print(F"New list: {new_list} ")