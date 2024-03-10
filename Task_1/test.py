import code
komunikat = ''

def test():
    global komunikat
    if code.radio.id == 42:
        komunikat = 'ID radia jest prawidłowe.' # 'Radio ID is set right'
        return True
    komunikat = 'ID radia jest nieprawidłowe.' # 'Radio ID is incorrect.'
    return False

test()