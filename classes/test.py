import code
from radio import Radio

def test():
    issues = []
    if chosen_one != code.radio.id:
        issues.append('Incorrect radio ID!')
    if not code.radio.power:
        issues.append('Radio is turned off!')
    if code.radio.frequency != wanted_freq:
        issues.append(('Incorrect radio frequency!', code.radio.frequency))
    if chosen_one != current_radio:
        issues.append('Connected to the wrong radio!')
    return issues


print(test())
