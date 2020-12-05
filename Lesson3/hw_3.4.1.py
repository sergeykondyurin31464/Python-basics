# Возведение числа в отрицательную степень при помощи цикла
print('enter x')
x = float(input())
print('enter y')
y = float(input())
def my_func(x, y):
    i = 0
    while i <= y:
        x = x * x
    else:
        return 1/x
print(my_func(x, y))