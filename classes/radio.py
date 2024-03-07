from random import randint, choice

channels_count = 7

class Radio:
    def __init__(self) -> None:
        self.power = False
        self.current_channel = None
        self.channels = sorted([randint(9, 300000) / 1000 for _ in range(channels_count)])
        self.wanted_freq = choice(self.channels)

    def toggle_power(self) -> None:
        self.power = not self.power
        print(f'Power is turned {"ON" if self.power else "OFF"}')

    def connect(self, freq: float) -> None:
        if not self.power:
            raise "Power is not on"
        if not freq in self.channels:
            raise "Channel not found"
        # self.current_channel = freq
        print(f'Connected to {freq}')
