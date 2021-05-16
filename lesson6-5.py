class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Start drawing...", end="")
        print(type(self).__name__, end="")


class Pen(Stationary):
    def draw(self):
        super().draw()
        print(" (pen line)")


class Pencil(Stationary):
    def draw(self):
        super().draw()
        print(" (pencil line)")


class Handle(Stationary):
    def draw(self):
        super().draw()
        print(" (handle line)")


for st in [Pen, Pencil, Handle]:
    inst = st("png1")
    inst.draw()
