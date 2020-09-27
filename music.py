import time

from machine import Pin, ADC, PWM
from clear_screen import clear_screen

pwm = PWM(Pin(5, Pin.OUT)) # Assign GPIO 5 to a pwm object
pwm.deinit() # Turn off sound on init

# TODO: Add the rest of the notes to expand functionality
E3 = 164.81
G3 = 196.00
A4 = 440.00
Ab4 = 415.30
C4 = 261.63
D4 = 293.66
E4 = 329.63
F4 = 349.23
G4 = 392.00
C5 = 523.25
E5 = 659.25
F5 = 698.46
G5 = 783.99

quarter_note = 0.5 # generate note durations
dotted_quarter_note = 0.75
eighth_note = 0.25
half_note = 1.0
whole_note = 2.0


def play_note(pwn, note, note_duration):
    """Plays a single note on a passive buzzer

    Parameters
    ----------
    pwn : class 'PWM'
        Class instance of PWM
    note : float
        Note to be played which is cast to int to fit freq
    note_duration : float
        Note duration of the note being played

    Returns
    -------
    None
    """
    try:
        pwm.init()
        pwm.freq(int(note))
        pwm.duty(512)
        time.sleep(note_duration)
        pwm.deinit()
    except:
        return False


def play_dc_540_theme():
    """Play the DC540 theme 

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    play_note(pwm, D4, dotted_quarter_note)
    play_note(pwm, C4, eighth_note)
    play_note(pwm, C4, half_note)
    play_note(pwm, D4, eighth_note)
    play_note(pwm, C4, eighth_note)
    play_note(pwm, D4, quarter_note)
    play_note(pwm, E4, whole_note)


def play_imperial_march():
    """Play the first three measures of the Imperial March theme 

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    play_note(pwm, A4, quarter_note) # [SOURCE: https://www.musicnotes.com/sheetmusic/mtd.asp?ppn=MN0133739]
    play_note(pwm, A4, quarter_note)
    play_note(pwm, A4, quarter_note)
    play_note(pwm, F4, eighth_note)
    play_note(pwm, C5, eighth_note)
    play_note(pwm, A4, quarter_note)
    play_note(pwm, F4, eighth_note)
    play_note(pwm, C5, eighth_note)
    play_note(pwm, A4, half_note)
    play_note(pwm, E5, quarter_note)
    play_note(pwm, E5, quarter_note)
    play_note(pwm, E5, quarter_note)
    play_note(pwm, F5, eighth_note)
    play_note(pwm, C5, eighth_note)
    play_note(pwm, Ab4, quarter_note)
    play_note(pwm, F4, eighth_note)
    play_note(pwm, C5, eighth_note)
    play_note(pwm, A4, half_note)
