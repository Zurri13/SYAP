import time

class TrafficLight:
    def __init__(self):
        self.__color = None

    def running(self):
        colors = ['красный', 'жёлтый', 'зелёный']
        for color in colors:
            self.__color = color
            self.__display_color()
            time.sleep(7 if color == 'красный' else 2)

    def __display_color(self):
        print(f"Светофор: {self.__color}")


traffic_light = TrafficLight()
traffic_light.running()
traffic_light.__display_color()
