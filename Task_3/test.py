from decode import decode

def test():
    try:
        is_right = decode() == 'miekki_slodki_chomik503'
        if is_right:
            print('Prawidłowe hasło:', decode())
        else:
            print('Nieprawidłowe hasło:', decode())

        return is_right
    
    except:
        print('Wystąpił błąd')
        return False

test()
