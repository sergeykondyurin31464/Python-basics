#рассчет расстояния тренировок
print('enter the first result')
first = int(input())
print('enter the end result')
end_res = int(input())
day = 0
while first < end_res:
    first = first + (first / 10)
    day += 1
if first >= end_res:
 print('result achieved at ' + str(day) + ' days')