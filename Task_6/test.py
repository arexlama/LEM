from walking import journey
komunikat = ''

wanted_journey = [
    'fw',
    'tr',
    'wi',
    'wo',
    'tr',
    'fw',
    'fw',
    'tl',
    'tl',
    'tr',
    'tl',
    'tr',
    'tr',
    'tl',
    'tr',
    'fw',
    'tr',
    'tl',
    'wi',

]

def test():
    global komunikat
    for wj, j in zip(wanted_journey, journey):
        if wj != j:
            komunikat = '''Hm, it seem you've took a wrong turn...'''
            return False
    komunikat = '''You've came to the right spot!'''
    return True

test()
