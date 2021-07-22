class Worker:
    def __init__(self, n, s, p, wag, bon):
        self.name = n
        self.surname = s
        self.position = p
        self._income = {'wage': wag, 'bonus': bon}


class position(Worker):
    def get_full_name(self):
        self.fullname = f'{self.name} {self.surname}'
        return f'Его имя: {self.fullname}'

    def get_total_income(self):
        self._sum = self._income['wage'] + self._income['bonus']
        return f'Полная прибыль: {self._sum}'


b = position('John', 'Watson', 'It-specialist', 29000, 5000)
print(b.get_full_name())
print(b.get_total_income())