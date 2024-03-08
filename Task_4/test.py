from decrypt import decrypt

def test():
    try:
        is_right = decrypt() == 'podczas_robot_centrum'
        if is_right:
            print('Prawidłowe hasło:', decrypt())
        else:
            print('Nieprawidłowe hasło:', decrypt())

        return is_right
    
    except:
        print('Wystąpił błąd')
        return False
