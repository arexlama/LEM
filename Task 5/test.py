from enter_password import enter_password

def test():
    try:
        is_right = enter_password() == ('plik_57', 'poteznekaloryfery718')
        if is_right:
            print('Koordynaty: 52°13\'56"N 21°00\'30"E')
        else:
            print('Corrupted data (nie był to plik, którego szukałeś)')

        return is_right
    
    except:
        print('An error has occured.')
        return False