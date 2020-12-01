# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
my_list = [el for el in range(100, 1001)]
def my_f(num1, num2):
    return num1 * num2
from functools import reduce
print(reduce(my_f, my_list))

