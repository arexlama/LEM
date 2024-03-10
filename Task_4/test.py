import code

komunikat = ''
password = 612

def test():
    global komunikat
    if code.data.connect < password:
        komunikat = 'Liczba jest większa!' # 'The number is bigger!'
        return False
    if code.data.connect > password:
        komunikat = 'Liczba jest mniejsza!' # 'The number is smaller!'
        return False
    komunikat = 'Hasło jest poprawne!' # 'Password is right!'
    for key in code.data.data:
        print(key + ': ' + code.data.data[key])
    return True

test()
