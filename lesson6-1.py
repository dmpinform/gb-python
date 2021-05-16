from time import sleep


class TrafficLight:
    LIGHT = {"red": 7, "yellow": 2, "green": 3}
    ORDER_LIGHT = {"red": 1, "yellow": 2, "green": 3}

    def __init__(self):
        self._color = ""

    def running(self):
        try:
            for order, (color, time) in enumerate(TrafficLight.LIGHT.items()):
                if TrafficLight.ORDER_LIGHT[color] == order + 1:
                    self._color = color
                    print(self._color)
                    sleep(time)
                else:
                    raise ExceptionLightOrder
        except ExceptionLightOrder:
            print("Order light error!")


class ExceptionLightOrder(Exception):
    pass


traffic = TrafficLight()
run = traffic.running()
