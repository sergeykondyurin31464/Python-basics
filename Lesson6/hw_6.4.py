# 4. Реализуйте базовый класс Car.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go (self):
        print('The car went')
    def stop (self):
        print('The car stopped')
    def turn (self, right, left=None):
            if left is not None:
                print('the car turned left')
            else:
                print('the car turned right')

    def show_speed (self, a):
        print('car speed is' + str(a))

class TownCar(Car):
    def show_speed(self, a):
        if a <= 60:
         print('car speed is' + str(a))
        else:
         print('overspeed!')


class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self, a):
         if a <= 40:
          print('car speed is' + str(a))
         else:
          print('overspeed!')


class PoliceCar(Car):
    pass

car_1 = TownCar(80, 'blue','ford' , True)
print(getattr(car_1, 'speed'))
print(getattr(car_1, 'color'))
print(getattr(car_1, 'name'))
print(getattr(car_1, 'is_police'))
car_1.go()
car_1.stop()
car_1.turn('left')
car_1.show_speed(40)
car_1.show_speed(80)


car_2 = WorkCar(60, 'red', 'belarus', True)
print(getattr(car_2, 'speed'))
print(getattr(car_2, 'color'))
print(getattr(car_2, 'name'))
print(getattr(car_2, 'is_police'))
car_2.go()
car_2.stop()
car_2.turn('right')
car_2.show_speed(30)
car_2.show_speed(80)

