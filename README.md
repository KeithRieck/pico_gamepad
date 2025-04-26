# pico_gamepad

This project is a USB gamepad, implemented on a Raspberry Pi Pico, written in CircuitPython.

Buttons should be attached to [pins on the Pico](./img/pico_pinouts.png):
* `GP9` for gamepad button 1
* `GP10` for gamepad button 2
* `GP22` for gamepad button 3
* `GP21` for gamepad button 4

![Breadboard setup](./img/Gamepad.png)

## References:
* [AdaFruit_CircuitPython_HID Github repository](https://github.com/adafruit/Adafruit_CircuitPython_HID/tree/main)
* [AdaFruit_CircuitPython_HID documentation](https://docs.circuitpython.org/projects/hid/en/latest/)
* [Custom HID Devices in CircuitPython](https://learn.adafruit.com/custom-hid-devices-in-circuitpython)
