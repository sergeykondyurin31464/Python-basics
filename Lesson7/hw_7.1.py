# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса
# (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы

class Matrix(object):
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join([''.join(['%d\t' % i for i in row]) for row in self.matrix])

    def __add__(self, other):
        answer = ''
        if len(self.matrix) == len(other.matrix):
            for line_1, line_2 in zip(self.matrix, other.matrix):
                if len(line_1) != len(line_2):
                    return 'Problems with shape'

                summed_line = [x + y for x, y in zip(line_1, line_2)]
                answer += ' '.join([str(i) for i in summed_line]) + '\n'
        else:
            return 'Problems with shape'
        return answer

matrix_1 = Matrix([[1, 2], [3, 4], [5, 6], [7, 8]])
matrix_2 = Matrix([[2, 3], [4, 5], [6, 7], [10, 20]])
print(matrix_1)
print()
print(matrix_1.__add__(matrix_2))