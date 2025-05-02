import board
import digitalio
import usb_hid
from hid_gamepad import Gamepad


class GamepadButton:
    "Represents a gamepad button, and its corresponding hardware pin."

    def __init__(self, button_num: int, pin: int, button_name: str = None):
        self.button_num = button_num
        self.pin = pin
        self.button_name = button_name
        self.dio = digitalio.DigitalInOut(pin)
        self.dio.direction = digitalio.Direction.INPUT
        self.dio.pull = digitalio.Pull.UP

    def is_pressed(self) -> bool:
        return not self.dio.value
    
    def __repr__(self) -> str:
        button_label =  f",'{button.button_name}'" if button.button_name is not None else ""
        return f"GamepadButton({self.button_num},{self.pin}{button_label})"


led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT


class ButtonSet:
    """
    Tracks the buttons that are currently pressed.
    This class exists primarily for debugging and monitoring.
    Yes, it's kind of overcomplicated for what it does.
    """

    def __init__(self):
        self.buttons_set: set[int] = set()

    def add(self, button: GamepadButton):
        if button.button_num not in self.buttons_set:
            self._log("press  ", button)
        self.buttons_set.add(button.button_num)

    def remove(self, button: GamepadButton):
        if button.button_num in self.buttons_set:
            self._log("release", button)
            self.buttons_set.remove(button.button_num)

    def _log(self, action: str, button: GamepadButton):
        global led
        print(f" {action} {button}", end="\n")
        led.value = len(self.buttons_set) == 0
    
    def __repr__(self) -> str:
        return f"ButtonSet({self.buttons_set})"


gp = Gamepad(usb_hid.devices)

button_list = [
    GamepadButton(1, board.GP9),
    GamepadButton(2, board.GP10),
    GamepadButton(3, board.GP22),
    GamepadButton(4, board.GP21),
]
button_set = ButtonSet()


while True:
    for button in button_list:
        if button.is_pressed():
            gp.press_buttons(button.button_num)
            button_set.add(button)
        else:
            gp.release_buttons(button.button_num)
            button_set.remove(button)
