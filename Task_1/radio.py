from random import randint

class Radio:
    def __init__(self, num: int, power: bool, freq: float) -> None:
        self.id = num
        self.power = power
        self.frequency = freq

    def toggle_power(self) -> None:
        self.power = not self.power

    def mod_freq(self, amount: float) -> None:
        self.frequency = amount

    def connect(self, new_radio) -> None:
        self.id = new_radio
        self.power = bool(randint(0, 1))
        self.frequency = randint(9, 300000) / 1000

radio = Radio(randint(1, 69), bool(randint(0, 1)), randint(9, 300000) / 1000)
