from decrypt import decrypt
komunikat = ''

def test():
    global komunikat
    try:
        if decrypt() == 'agencie s.m bomba masowego razenia zostanie zdetonowana w warszawie. szczegolowe informacje otrzymales w wyslanym pliku. wiadomosc nie zostanie powtorzona ani nagrana. oczekujemy raportu o sytuacji do godziny 23:30.':
            komunikat = 'Correct!'
            print('agencie s.m bomba masowego razenia zostanie zdetonowana w warszawie. szczegolowe informacje otrzymales w wyslanym pliku. wiadomosc nie zostanie powtorzona ani nagrana. oczekujemy raportu o sytuacji do godziny 23:30.')
            return True
        komunikat = 'Wrong!'
        return False
    
    except:
        print('Wystąpił błąd')
        return False

test()
