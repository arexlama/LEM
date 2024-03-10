import code
komunikat = ''

def test():
    global komunikat
    if not code_2.radio.power:
        komunikat = 'Radio jest wyłączone.'
        return False
    if code_2.radio.frequency != 117.354:
        komunikat = 'Częstotliwość radia jest nieprawidłowa.'
        return False
    komunikat = 'Radio jest dobrze nastawione!'
    return True


test()
