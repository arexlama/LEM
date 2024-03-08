import code, walking
komunikat = ''

wanted_journey = ['fw', 'fw', 'tr', 'tl', 'tl']

def test():
    global komunikat
    for wj, cj in zip(wanted_journey, walking.journey):
        if wj != cj:
            komunikat = '''Hm, it seem you've took a wrong turn...'''
            return False
    komunikat = '''You've came to the right spot!'''
    return True

print(test(), komunikat)