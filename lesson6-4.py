class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        pass

    def stop(self):
        pass

    def turn(self, direction):
        pass

    def show_speed(self):
        print(f"speed = {self.speed}")

    def __repr__(self):
        return f"name = {self.name}, color = {self.color}, speed ={self.speed}, police = {self.is_police}"


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print("Speed limit 60", end="\n")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print("Speed limit 40", end="\n")


class PoliceCar(Car):
    pass


car = TownCar(100, "red", "volvo", False)
print(car)
car.show_speed()

car = SportCar(100, "green", "opel", False)
print(car)
car.show_speed()

car = WorkCar(100, "yellow", "mazda", False)
print(car)
car.show_speed()

car = PoliceCar(100, "black", "lada", True)

print(car)
car.show_speed()
