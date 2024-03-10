import data
komunikat = ''

def test():
    global komunikat
    if data.Connect != int():
        komunikat = 'Wrong password!'
        return False
    else:
        print(data.data.keys())

    if data.File != 'plik_57':
        komunikat = 'Wrong file!'
        return False
    if data.Password != 'poteznekaloryfery718':
        komunikat = 'Wrong file access key!'
        return False
    komunikat = 'You`ve got the data'
    return True

test()
