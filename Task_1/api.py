class Radio:
    def toggle_power(self) -> None:
        # toggles the power of current radio (on/off)
        pass

    def mod_freq(self, amount: float) -> None:
        # change the frequency on the current radio to an amount given (0.009-300)
        pass

    def connect(self, new_radio: int) -> None:
        # connects to a radio number given (1-69). SETS OTHER RADIO DATA TO RANDOM
        pass

radio: Radio
