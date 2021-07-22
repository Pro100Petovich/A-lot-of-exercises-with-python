class Car:
    def __init__(self, s, c, n, i):
        self.speed = s
        self.color = c
        self.name = n
        self.is_police = i

    def go(self):
        return 'Машина стартовала'

    def stop(self):
        return 'Машина остановилась'

    def turn(self, direction):
        dictionary = {'left':"налево", 'right': 'направо'}
        return f'Машина повернула {dictionary[direction]}'

class TownCar(Car):
    def show_speed(self):
        if self.speed >= 60:
            return 'Превышение скорости'
        else:
            return self.speed

class SportCar(Car):
    def show_speed(self):
         return self.speed


class WorkCar(Car):
    def show_speed(self):
        if self.speed >= 40:
            return 'Превышение скорости'
        else:
            return self.speed

class PoliceCar(Car):
    def information_about_car(self):
        if self.is_police == True:
            return f'Скорость в данный момент: {self.speed} и машина является полицейской'


b = Car(70, 'silver', 'Charlie', True )
print(b.turn('left'))
print(b.go())
print(b.stop())