from decode import decode
from random import randint

def test():
    try:
        is_right = decode() == 'under construction'
        if is_right:
            print('Prawidłowe hasło:', decode())
        else:
            print('Nieprawidłowe hasło:', decode())

        return is_right
    
    except:
        print('Wystąpił błąd')
        return False