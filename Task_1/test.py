import code
komunikat = ''

def test():
    global komunikat
    if code.radio.id == 42:
        komunikat = 'Radio ID is set right'
        return True
    komunikat = 'Radio ID is incorrect. Think about it again.'
    return False
