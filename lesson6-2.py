class Road:

    dens = 25
    thick = 5

    def __init__(self, length=1, width=1):
        self._length = length
        self._width = width

    def massa(self):
        return self._length * self._width * Road.dens * Road.thick/1000

    def __str__(self):
        return f"Road massa = {self.massa()} (т)"


road = Road(length=20, width=5000)
print(road)
