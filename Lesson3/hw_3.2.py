# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя
print('enter name')
n = input()
print('enter surname')
s = input()
print('enter year of birth')
y = input()
print('enter city of residence')
c = input()
print('enter email')
e = input()
print('enter phone number')
p = input()
def my_f(n,s,y,c,e,p):
    print(f"name - {n}, surname - {s}, year of birth - {y},city of residence - {c}, email - {e}, phone number - {p}")
my_f(n=n,s=s,y=y,c=c,e=e,p=p)



