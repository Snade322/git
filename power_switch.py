from switch import Switch
from switch_interface import SwitchBase


class PowerSwitch(SwitchBase):
    def __init__(self, client: Switch):
        if not isinstance(client, Switch):
            raise TypeError("client should be switch")

        self.client = client
        self.on = False
        self.client.turn_off()

    def is_turned_on(self):
        return self.on

    def toggle(self):  # выключатель
        if self.on:
            self.client.turn_off()
            self.on = False  # сохранение состояния
        else:
            self.client.turn_on()
            self.on = True  # сохранение состояния
