import code
komunikat = ''

def test():
    global komunikat
    if not code.radio.power:
        komunikat = 'Radio is turned off.'
        return False
    if code.radio.frequency != 117.354:
        komunikat = 'Radio frequency is wrong.'
        return False
    komunikat = 'Radio is tuned right!'
    return True

test()
