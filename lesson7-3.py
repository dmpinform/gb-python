class Kletka:
    def __init__(self, cells: int):
        self.cells = cells

    def __add__(self, x):
        if type(x) == Kletka:
            return Kletka(self.cells + x.cells)
        raise Exception("Error type")

    def __sub__(self, x):
        if type(x) == Kletka and self.cells > x.cells:
            return Kletka(self.cells - x.cells)
        raise Exception("Error type or values")

    def __mul__(self, x):
         if type(x) == Kletka:
            return Kletka(self.cells * x.cells)
         raise Exception("Error type")

    def __truediv__(self, x):
         if type(x) == Kletka:
            return Kletka(self.cells // x.cells)
         raise Exception("Error type")

    def make_order(self, col):
        kletkas = ['*' for _ in range(0, self.cells)]
        return "\n".join(["".join(kletkas[i:i+col]) for i in range(0, len(kletkas), col)])


kletka1 = Kletka(30)
kletka2 = Kletka(4)

kletka3 = kletka1 + kletka2

print(kletka3.cells)
print(kletka3.make_order(7))
