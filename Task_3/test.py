from decrypt import decrypt

def test():
    try:
        is_right = decrypt() == 'agencie s.m bomba masowego razenia zostanie zdetonowana w warszawie. szczegolowe informacje otrzymales w wyslanym pliku. wiadomosc nie zostanie powtorzona ani nagrana. oczekujemy raportu o sytuacji do godziny 23:30.'
        if is_right:
            print(decrypt())
        else:
            print(decrypt(), '\n czy to na pewno poprawna wiadomość?')

        return is_right
    
    except:
        print('Wystąpił błąd')
        return False

test()
