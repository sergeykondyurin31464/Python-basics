# 3. Реализовать базовый класс Worker (работник),
# в котором определить атрибуты: name, surname,
# position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь,
# содержащий элементы: оклад и премия, например,
# {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = wage
        self.bonus = bonus
        __income = {"wage": self.wage, "bonus": self.bonus}

class Position(Worker):
            def get_full_name(self):
                print(self.name, self.surname, self.position)

            def get_total_income(self):
                __income = {"wage": self.wage, "bonus": self.bonus}
                print(sum(__income.values()))

my_worker1 = Position('Иван', 'Иванов', 'рабочий', 1000, 100)
my_worker1.get_full_name()
my_worker1.get_total_income()











