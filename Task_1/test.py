import code
komunikat = ''

def test():
    global komunikat
    if code_1.radio.id == 42:
        komunikat = 'ID radia jest poprawnie ustawione'
        return True
    komunikat = 'ID radia jest niepoprawnie ustawione. Pomyśl jeszcze raz.'
    return False
