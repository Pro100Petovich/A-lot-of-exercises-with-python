from itertools import chain
class cell:
    def __init__(self, num_cell, n_c_r):
        self.num_cell = num_cell
        self.num_cell_row = n_c_r

    def __sub__(self, other):
        if self.num_cell > other.num_cell:
            return f'Количество ячеек клеток после разности:{self.num_cell - other.num_cell}'
        elif self.num_cell < other.num_cell:
            return f'Количество ячеек клеток после разности:{other.num_cell - self.num_cell}'
        else:
            return 'Вычитание не нужно'

    def __mul__(self, other):
        return f'Количество ячеек клеток после умножения:{self.num_cell * other.num_cell}'

    def __floordiv__(self, other):
        if self.num_cell > other.num_cell:
            return f'Количество ячеек клеток после деления:{self.num_cell // other.num_cell}'
        else:
            return f'Количество ячеек клеток после разности:{other.num_cell // self.num_cell}'

    def __add__(self, other):
        return f'Количество ячеек клеток после суммы:{self.num_cell + other.num_cell}'

    def make_order(self):
        stroka = []
        for i in range(1, self.num_cell):
            if (i % self.num_cell_row) != 0:
                stroka.append('*')
            else:
                stroka.append("/n")
        return ' '.join(map(str, stroka))


b = cell(15, 5)
c = cell(25, 8)
print(b.make_order())
print(b + c)
print(b // c)
print(c - b)
print(b * c)
