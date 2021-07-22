from itertools import chain


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        r = list(chain(*self.matrix))
        for i in range(2, 2*len(self.matrix)+1, 3):
            r.insert(i, '\n')
        k = ' '.join(map(str, r))
        return f'Матрица:\n {k}'

    def __add__(self, other):
        max_sum = [[self.matrix[l][k] + other.matrix[l][k] for k in range(len(self.matrix[0]))] for l in
                   range(len(self.matrix))]
        for i in range(1, len(self.matrix) + 1, 2):
            max_sum.insert(i, '\n')
        c = list(chain(*max_sum))
        l = ' '.join(map(str, c))
        return f'Матрица суммы:\n {l}'