Connect: str
File: str
Password: str

data = {
    'plik_004': 'kiciakocia123',
    'plik_005': 'pingpong888',
    'plik_006': 'panwiesio4eva',
    'plik_044': 'nevagonagivslonup13',
    'plik_213': 'alamakota516',
    'plik_278': 'torbapifpaf10',
    'plik_042': 'bombateraz1',
    'plik_057': 'poteznekaloryfery718', #poprawne
    'plik_003': 'sudokureference108',
    'plik_017': 'jojojajo240',
    'plik_059': 'dmymiter2120',
    'plik_110': 'gombkawiktorii168',
    'plik_012': 'wafleczekoladowe14',

}

def connect(cn: str) -> None:
    global Connect
    Connect = cn

def file(f: int) -> None:
    global File
    File = 'plik_' + str(f)

def password(pw: str):
    global Password
    Password = pw

def hack():
    return data[File]
