class Matrix:
    def __init__(self, val):
        self.matr = val

    def __str__(self):
        return "\n".join(" ".join(map(str, row)) for row in self.matr)

    def __iter__(self):
        return (i for i in self.matr)

    def __getitem__(self, i):
        return self.matr[i]

    def __add__(self, y):
        nm = self.matr[:]
        for ci, c in enumerate(self.matr):
            for ri, r in enumerate(c):
                nm[ci][ri] += y[ci][ri]
        return nm


m = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

m1 = Matrix([[1, 1, 1], [2, 2 , 2], [-7, -8, -9]])
print(m+m1)
