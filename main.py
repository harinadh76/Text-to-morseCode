import time
import winsound

freq = 550 # Hz
dotLength = 60 # milliseconds
dashLength = dotLength * 3
pauseWords = dotLength * 7

alphaToMorse = {'a': ".-", 'b': "-...", 'c': "-.-.", 'd': "-..", 'e': ".",
                'f': "..-.", 'g': "--.", 'h': "....", 'i': "..", 'j': ".---", 'k': "-.-",
                'l': ".-..", 'm': "--", 'n': "-.", 'o': "---", 'p': ".--.", 'q': "--.-",
                'r': ".-.", 's': "...", 't': "-", 'u': "..-", 'v': "...-", 'w': ".--",
                'x': "-..-", 'y': "-.--", 'z': "--..",
                '1': ".----", '2': "..---", '3': "...--", '4': "....-", '5': ".....",
                '6': "-....", '7': "--...", '8': "---..", '9': "----.", '0': "-----",
                ' ': "/", '.': ".-.-.-", ',': "--..--", '?': "..--..", "'": ".----.",
                '@': ".--.-.", '-': "-....-", '"': ".-..-.", ':': "---...", ';': "---...",
                '=': "-...-", '!': "-.-.--", '/': "-..-.", '(': "-.--.", ')': "-.--.-",
                'á': ".--.-", 'é': "..-.."}


def morsecode():
    """
    converts text to morse code.
    prints result and calls morseaudio.
    """
    while True:
        message = ' '.join(input(">").strip().split())
        # if you enter nothing, exits method
        if message == "":
            return

        # remembers characters that do not have standard morse code equivalent
        unabletoconvert = ""
        morse = ""
        for char in message.lower():
            if char in alphaToMorse:
                morse += alphaToMorse[char] + ' '
            else:
                unabletoconvert += char
        if len(unabletoconvert) != 0:
            print("These characters are unable to be converted:\n" + ' '.join(unabletoconvert))
        morse = morse[:-1]
        print(morse)
        morseaudio(morse)


def beep(dur):
    """
    makes noise for specific duration.
    :param dur: duration of beep in milliseconds
    """
    winsound.Beep(freq, dur)


def pause(dur):
    """
    pauses audio for dur milliseconds
    :param dur: duration of pause in milliseconds
    """
    time.sleep(dur / 1000)


def morseaudio(morse):
    """
    plays audio conversion of morse string using inbuilt windows module.
    :param morse: morse code string.
    """
    for char in morse:
        if char == ".":
            beep(dotLength)
        elif char == "-":
            beep(dashLength)
        elif char == "/":
            pause(pauseWords)
        else:
            # char is blank space
            pause(dashLength)


morsecode()