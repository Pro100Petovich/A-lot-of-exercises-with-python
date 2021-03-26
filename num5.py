class Stationery:
    def __init__(self, t):
        self.title = t

    def draw(self):
        return 'Запуск отрисовки'

class Pen(Stationery):
    def draw(self):
        return 'Рисуем ручкой'

class Pencill(Stationery):
    def draw(self):
        return 'Рисуем корандашом'
class Handle(Stationery):
    def draw(self):
        return "Рисуем handle'ом"

Stationery('Здесь мог быть ваш заголовок')
s = Stationery('Здесь мог быть ваш заголовок')
print(s.draw())

p = Pen('Здесь мог быть ваш заголовок')
print(p.draw())

p_2 = Pencill('Здесь мог быть ваш заголовок')
print(p_2.draw())

h = Handle('Здесь мог быть ваш заголовок')
print(h.draw())
