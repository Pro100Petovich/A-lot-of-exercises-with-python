from abc import ABC
class clothes(ABC):
    def __init__(self, cloth, r):
        self.cloth = cloth
        self.razm = r


class coat(clothes):
    def size(self):
        if self.cloth == 'Пальто':
            self.V = self.razm
            self.per = (self.V / 6.5 + 0.5)
        return self.per


class costum(clothes):
    def size(self):
        if self.cloth == 'Костюм':
            self.H = self.razm
            self.per_1 = (2 * self.H + 0.3)
        return self.per_1


b = coat('Пальто', 96)
print(b.size())
c = costum('Костюм', 128)
print(c.size())
