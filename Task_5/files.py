file = str()
password = str()

data = {
    'plik_004': 'kiciakocia123',
    'plik_005': 'pingpong888',
    'plik_006': 'panwiesio4eva',
    'plik_044': 'nevagonagivslonup13',
    'plik_213': 'alamakota516',
    'plik_278': 'torbapifpaf10',
    'plik_042': 'bombateraz1',
    'plik_057': 'poteznekaloryfery718',
    'plik_003': 'sudokureference108',
    'plik_017': 'jojojajo240',
    'plik_059': 'dmymiter2120',
    'plik_110': 'gombkawiktorii168',
    'plik_012': 'wafleczekoladowe14',

}

def open_file(f: int, p: str) -> None:
    global file, password
    f = str(f)
    zeros = '' if len(f) == 3 else '0' if len(f) == 2 else '00'
    file = 'plik_' + zeros + f
    password = p