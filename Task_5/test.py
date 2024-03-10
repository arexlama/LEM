import code
komunikat = ''

def test():
    global komunikat

    if code.files.file != 'plik_057':
        komunikat = 'Wrong file!'
        return False
    if code.files.password != 'poteznekaloryfery718':
        komunikat = 'Wrong password!'
        return False

    komunikat = 'File opened!'
    print('Dnia 15.11 o 00:00, bomba zostanie zdetonowana pod 52.231838,21.006000')
    return True


print(test(), komunikat)
