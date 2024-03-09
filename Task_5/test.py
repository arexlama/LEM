import data
komunikat = ''

def test():
    global komunikat
    if data.Connect != int():
        komunikat = ''
        return False
    if data.File != 'plik_57':
        komunikat = ''
        return False
    if data.Password != 'poteznekaloryfery718':
        komunikat = ''
        return False
    komunikat = ''
    return True
