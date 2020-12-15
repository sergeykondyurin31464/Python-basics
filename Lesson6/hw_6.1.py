# 1. Создать класс TrafficLight (светофор)
# и определить у него один атрибут color (цвет) и метод running (запуск).
import time
class Trafficlight:
    def __init__(self, type_color):
        self._color = type_color
    def running(self):
        print(self._color, 'run')

a = Trafficlight('red')
a.running()
time.sleep(7)
b = Trafficlight('yellow')
b.running()
time.sleep(2)
c = Trafficlight('green')
c.running()
time.sleep(7)








