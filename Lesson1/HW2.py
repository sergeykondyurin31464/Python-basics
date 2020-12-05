# 2 ввод времени в секундах вывод в формате чч:мм:сс.

print('enter time')
time = int(input())
hour = (time // 3600)
minute = ((time % 3600) // 60)
second = ((time % 3600) % 60)
print(str(hour) + ':' + str(minute) + ':' + str(second) + '.')