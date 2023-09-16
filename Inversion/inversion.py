from abc import ABC, abstractmethod


class Switchable(ABC):
    @abstractmethod
    def switch_off(self):
        pass

    @abstractmethod
    def turn_on(self):
        pass


class LightBulb(Switchable):
    def switch_off(self):
        print("turned off")

    def turn_on(self):
        print("turned on")


class Fan(Switchable):
    def switch_off(self):
        print("Switched off")

    def turn_on(self, client):
        print(f"{client.__class__.__name__} turned on")


class PowerSwitch:
    def __init__(self, c) -> None:
        self.client = c
        self.on = False

    def press(self):
        if self.on:
            self.client.switch_off()

        else:
            self.client.turn_on(self.client)
            self.on = True


if __name__ == "__main__":
    l = LightBulb()
    fan = Fan()
    switch = PowerSwitch(fan)
    switch.press()
