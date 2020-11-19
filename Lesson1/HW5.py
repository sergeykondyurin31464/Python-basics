#рассчет прибыли и рентабельности
print('enter revenue')
rev = int(input())
print('enter costs')
costs = int(input())
if rev > costs:
    a = ((rev - costs) * 100 / rev)
    print('worked with profit ! profitability ' + str(a) + '%')
    print('enter quantity workers')
    w = int(input())
    p_w = int((rev - costs) / w)

    print('profit per worker ' + str(p_w))


else:
    print('worked with loss')