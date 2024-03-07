from radio import Radio

radio = Radio()
assert not radio.power
print(radio.channels)
radio.toggle_power()
radio.connect(radio.wanted_freq)
