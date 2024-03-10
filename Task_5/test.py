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
    print('''Wiadomosc o bombie~~~~~''')
    return True


print(test(), komunikat)
