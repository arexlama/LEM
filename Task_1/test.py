import code_1
komunikat = ''

def test():
    global komunikat
    if code_1.radio.id == 42:
        komunikat = 'Radio ID is set right'
        return True
    komunikat = 'Radio ID is incorrect. Think about it again.'
    return False