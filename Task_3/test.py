from decrypt import decrypt
komunikat = ''

def test():
    global komunikat
    try:
        if decrypt() == 'agencie s.m bomba masowego razenia zostanie zdetonowana w warszawie. szczegolowe informacje otrzymales w wyslanym pliku. wiadomosc nie zostanie powtorzona ani nagrana. oczekujemy raportu o sytuacji do godziny 23:30.':
            komunikat = 'Poprawnie!' # 'Correct!'
            print('agencie s.m bomba masowego razenia zostanie zdetonowana w warszawie. szczegolowe informacje otrzymales w wyslanym pliku. wiadomosc nie zostanie powtorzona ani nagrana. oczekujemy raportu o sytuacji do godziny 23:30.')
            return True
        komunikat = 'Źle!' # 'Wrong!'
        return False
    
    except:
        komunikat = 'Wystąpił błąd'
        return False

test()
