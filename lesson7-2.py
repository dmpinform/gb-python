from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @abstractmethod
    def calc_material(self):
        pass


class Coat(Clothes):
    def __init__(self, name, size):
        super().__init__(name)
        self._size = size

    @property
    def size(self):
        return self._size

    def calc_material(self):
        return self.size / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, name, height):
        super().__init__(name)
        self._height = height

    @property
    def height(self):
        return self._height

    def calc_material(self):
        return 2 * self.height + 0.3


clothes = [Coat("Armani", 50), Suit("Adidas", 45)]

for cl in clothes:
    print(cl.name, cl.calc_material())

print("Summary material :", sum(s.calc_material() for s in clothes))
