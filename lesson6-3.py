class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

    @property
    def income(self):
        return self._income


class Position(Worker):

    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return sum(self.income.values())


pos = Position("Ivan", "Svetlov", "Middle", 12_000, 5_000)
print(pos.get_full_name(), pos.get_total_income())
