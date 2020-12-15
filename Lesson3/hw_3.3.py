# Реализовать функцию , которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.
print('enter a')
a = int(input())
print('enter b')
b = int(input())
print('enter c')
c = int(input())
def m_1(a, b, c):
    t = [a, b, c]
    t.remove(min(t))
    return sum(t)
print(m_1(a, b, c))







