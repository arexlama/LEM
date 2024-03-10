class Radio:
    def toggle_power(self) -> None:
        # Toggles the power of current radio (on/off)
        # Przełącza zasilanie obecnego radia (włącz./wyłącz.)
        pass

    def mod_freq(self, amount: float) -> None:
        # Change the frequency on the current radio to an amount given (0.009-300)
        # Zmienia częstotliwość obecnego radia na podaną wartość (0.009-300)
        pass

    def connect(self, new_radio: int) -> None:
        # Connects to a radio number given (1-69). SETS OTHER RADIO DATA TO RANDOM
        # Podłącza się do radia o podanym numerze (1-69). USTAWIA INNE WARTOŚCI RADIA NA LOSOWE
        pass

radio: Radio
