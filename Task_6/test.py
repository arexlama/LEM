from walking import journey
komunikat = ''

wanted_journey = [
    'wo',
    'tr',
    'tl',
    'fw',
    'tl',
    'tr',
    'tl',
    'tl',
    'tr',
    'tl',
    'tr',
    'tr',
    'fw',
    'tl',
    'wi',
    'flying_tiger',
    'wo',
    'tl',
    'wi',
    'palac_kultury',

]

def test():
    global komunikat
    for wj, j in zip(wanted_journey, journey):
        if wj != j:
            komunikat = 'Hm, it seem you`ve took a wrong turn somewhere...'
            return False
    komunikat = 'You`ve came to the right spot!'
    return True

test()
