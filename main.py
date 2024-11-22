from switch import Switch
from switch import LightBulb
from power_switch import PowerSwitch


def main():
    print(Switch)
    bulb = LightBulb()
    print(bulb)
    # bulb.turn_on()
    # bulb.turn_off()
    # bulb.turn_on()

    switch = PowerSwitch(bulb)
    switch.toggle()
    switch.toggle()
    switch.toggle()
    switch.toggle()
    print("is turned on?", switch.is_turned_on())
    print("is turned off?", switch.is_turned_off())
    print("is turned on?", switch.is_turned_on())
    print("is turned off?", switch.is_turned_off())
    switch.toggle()
    print("is turned on?", switch.is_turned_on())
    print("is turned off?", switch.is_turned_off())
    print("is turned on?", switch.is_turned_on())
    print("is turned off?", switch.is_turned_off())


if __name__ == "__main__":
    main()
