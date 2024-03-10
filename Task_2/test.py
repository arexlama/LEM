import code
komunikat = ''

def test():
    global komunikat
    if not code.radio.power:
        komunikat = 'Radio jest wyłączone' # 'Radio is turned off.'
        return False
    if code.radio.frequency != 117.354:
        komunikat = 'Częstotliwość radia jest błędna' # 'Radio frequency is wrong.'
        return False
    komunikat = 'Radio jest nastawione poprawnie!' # 'Radio is tuned right!'
    return True

test()
