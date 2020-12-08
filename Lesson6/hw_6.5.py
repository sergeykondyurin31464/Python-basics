# 5. Реализовать класс Stationery (канцелярская принадлежность).

class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print('Пишем конспект')

class Pencil(Stationery):
    def draw(self):
        print('Чертим чертеж')

class Handle(Stationery):
    def draw(self):
        print('Рисуем на обоях')

stationery_1 = Pen('pen')
stationery_2 = Pencil('pencil')
stationery_3 = Handle('handle')
stationery_1.draw()
stationery_2.draw()
stationery_3.draw()




