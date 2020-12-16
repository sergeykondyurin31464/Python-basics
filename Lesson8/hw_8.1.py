import random


class Cell:
    def __init__(self, nums):
        self.nums = nums

    def make_order(self, rows):
        return '\n'.join(['*' * rows for _ in range(self.nums // rows)]) + '\n' + '*' * (self.nums % rows)
cell = Cell(50)

def st_ring(temp):
    nums = []
    while len(nums) < 5:
        elem = str(random.randint(1, 90))
        if elem not in temp:
            nums.append(elem)
            temp.append(elem)
    nums = list(nums) + list(' ' * 16)
    random.shuffle(nums)
    return ' '.join(nums)
def barrel(self, num):
    nums = 90
    elem = str(random.randint(1, 90))
print('Ваша карточка')
print(cell.make_order(50))
temp = []
for _ in range(3):
    print(st_ring(temp))
print(cell.make_order(50))

print('Карточка компьютера')
print(cell.make_order(50))
temp = []
for _ in range(3):
    print(st_ring(temp))
print(cell.make_order(50))

# Все что смог