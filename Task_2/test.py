import code_2
komunikat = ''

def test():
    global komunikat
    if not code_2.radio.power:
        komunikat = 'Radio is turned off.'
        return False
    if code_2.radio.frequency != 117.354:
        komunikat = 'Radio frequency is wrong.'
        return False
    komunikat = 'Radio is tuned right!'
    return True


test()