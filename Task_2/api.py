class Radio:
    def __init__(self, id: int, power: bool, frequency: float) -> None:
        # attributes of Radio
        # atrybuty Radia
        pass

    def toggle_power(self) -> None:
        # toggles the power of current radio (on/off)
        # przełącza zasilanie aktualnego radia (włącz/wyłącz)
        pass

    def mod_freq(self, amount: float) -> None:
        # change the frequency on the current radio to an amount given (0.009-300)
        # zmienia częstotliwośc aktualnego radia na liczbę podaną (0.009 - 300)
        pass

    def connect(self, new_radio: int) -> None:
        # connects to a radio number given (1-69). SETS OTHER RADIO DATA TO RANDOM
        # podłącza do radia o numerze podanym (1 - 69). Ustawia dane innych radii na losowe
        pass

radio: Radio
