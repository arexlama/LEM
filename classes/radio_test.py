import unittest
from radio import Radio

class TestRadio(unittest.TestCase):
    def setUp(self) -> None:
        self.radio = Radio()

    def test_power_should_be_off_by_default(self):
        self.assertFalse(self.radio.power)

    def test_channel_should_be_none_by_default(self):
        self.assertIsNone(self.radio.current_channel)

    def test_freq_should_be_saved(self):
        freq = self.radio.channels[0]
        self.assertRaises(self.radio.connect(freq))

        self.assertEqual(self.radio.current_channel, freq)

if __name__ == '__main__':
    unittest.main()
