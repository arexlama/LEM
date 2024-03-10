import code

komunikat = ''
password = 612

def test():
    global komunikat
    if code.data.connect < password:
        komunikat = 'Password is bigger!'
        return False
    if code.data.connect > password:
        komunikat = 'Password is smaller!'
        return False
    komunikat = 'Password is right!'
    for key in code.data.data:
        print(key + ': ' + code.data.data[key])
    return True

test()
