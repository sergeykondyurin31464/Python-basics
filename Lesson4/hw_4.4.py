#  Определить элементы списка, не имеющие повторений.
my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list = [my_list[i] for i in range(1, len(my_list))
            if my_list.count(i) == 1]
print(F"New list: {new_list} ")
