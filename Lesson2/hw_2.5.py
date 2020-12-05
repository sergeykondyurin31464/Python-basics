# Рейтинг
my_list = [7, 5, 3, 3, 2]
print(my_list)
print('enter new number')
x = int(input())
for el in range(len(my_list)):
    if my_list[el] == x:
        my_list.insert(el+1, x)
        break
    elif my_list[0] < x:
        my_list.insert(0, x)
    elif my_list[-1] > x:
        my_list.append(x)
print(my_list)
print('enter new number')

