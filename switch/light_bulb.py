from switch import Switch


class LightBulb(Switch):
    def turn_on(self):
        print(self.__class__.__name__, "turned on")

    def turn_off(self):
        print(self.__class__.__name__, "turned off")
