import data
komunikat = ''

def test():
    global komunikat
    if data.Connect != int():
        komunikat = 'Nieprawidłowe hasło!'
        return False
    else:
        print(data.data.keys())

    if data.File != 'plik_57':
        komunikat = 'Nieprawidłowy plik!'
        return False
    if data.Password != 'poteznekaloryfery718':
        komunikat = 'Nieprawidłowy klucz dostępu do pliku!'
        return False
    komunikat = 'Dostałeś dane'
    return True

test()
