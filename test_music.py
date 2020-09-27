# import unittest
# unittest.main('test_music')


import unittest
from machine import Pin, ADC, PWM

from music import play_note


class TestMusic(unittest.TestCase):
    def test_play_note(self):
        """
        test play_note
        """
        # Setup
        pwm = PWM(Pin(5, Pin.OUT))
        E3 = 164.81
        quarter_note = 0.5

        # Calls
        error_check = play_note(pwm, E3, quarter_note)
        
        # Asserts
        self.assertIsNone(error_check)
