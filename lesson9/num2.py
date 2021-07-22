class Road:
    def __init__(self, p_1, p_2):
        self.length = p_1
        self.width = p_2

    def weight(self):
        self.mass = self.length * self.width * 25 * 5
        return f'Mасса дороги получается: {self.mass}'


a = Road(5, 6)
print(a.weight())
