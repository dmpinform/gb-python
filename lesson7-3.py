class Cell:
    def __init__(self, cells: int):
        self.cells = cells

    def __add__(self, x):
        if type(x) == Cell:
            return Cell(self.cells + x.cells)
        raise Exception("Error type")

    def __sub__(self, x):
        if type(x) == Cell and self.cells > x.cells:
            return Cell(self.cells - x.cells)
        raise Exception("Error type or values")

    def __mul__(self, x):
        if type(x) == Cell:
            return Cell(self.cells * x.cells)
        raise Exception("Error type")

    def __truediv__(self, x):
        if type(x) == Cell:
            return Cell(self.cells // x.cells)
        raise Exception("Error type")

    def make_order(self, col):
        cells = ['*' for _ in range(0, self.cells)]
        return "\n".join(["".join(cells[i:i + col]) for i in range(0, len(cells), col)])


cell1 = Cell(30)
cell2 = Cell(4)

cell3 = cell1 + cell2

print(cell3.cells)
print(cell3.make_order(10))
