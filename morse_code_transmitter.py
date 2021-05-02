from tkinter import *
import tkinter.font
import RPi.GPIO as GPIO
import time

## Hardware Definitions
TIME_UNIT = 0.25
PIN = 18

## Initialise GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(PIN, GPIO.OUT)

## GUI Definitions
win = Tk()
win.title("Morse Code Transmitter")
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")

## Morse Code Dictionary
MORSE_CODE = { 'A':'.-',
               'B':'-...',
               'C':'-.-.',
               'D':'-..',
               'E':'.',
               'F':'..-.',
               'G':'--.',
               'H':'....',
               'I':'..',
               'J':'.---',
               'K':'-.-',
               'L':'.-..',
               'M':'--',
               'N':'-.',
               'O':'---',
               'P':'.--.',
               'Q':'--.-',
               'R':'.-.',
               'S':'...',
               'T':'-',
               'U':'..-',
               'V':'...-',
               'W':'.--',
               'X':'-..-',
               'Y':'-.--',
               'Z':'--..',
               '1':'.----', '2':'..---', '3':'...--',
               '4':'....-', '5':'.....', '6':'-....',
               '7':'--...', '8':'---..', '9':'----.',
               '0':'-----', ', ':'--..--', '.':'.-.-.-',
               '?':'..--..', '/':'-..-.', '-':'-....-',
               '_': '..--.-', '(':'-.--.', ')':'-.--.-',
               ' ': ' '}

## Event Functions
def transmitMessage():
    messageString = message.get()
    for letter in messageString:
        for symbol in MORSE_CODE[letter.upper()]:
            if symbol == '.':
                dot()
                symbolDelay()
            elif symbol == '-':
                dash()
                symbolDelay()
            elif symbol == ' ':
                wordDelay()
        letterDelay()
    
def dot():
    GPIO.output(PIN, GPIO.HIGH)
    time.sleep(TIME_UNIT)

def dash():
    GPIO.output(PIN, GPIO.HIGH)
    time.sleep(3*TIME_UNIT)

def symbolDelay():
    GPIO.output(PIN, GPIO.LOW)
    time.sleep(TIME_UNIT)

def letterDelay():
    GPIO.output(PIN, GPIO.LOW)
    time.sleep(3*TIME_UNIT)

def wordDelay():
    GPIO.output(PIN, GPIO.LOW)
    time.sleep(7*TIME_UNIT)

def close():
    GPIO.cleanup()
    win.destroy()

## Widgets

transmitButton = Button(win, text = 'Transmit Message', font = myFont, command = transmitMessage, bg = 'bisque2', height = 1)
transmitButton.grid(row = 0, column = 1)

message = Entry(win, font = myFont, width = 20)
message.grid(row = 0, column = 0)

exitButton = Button(win, text = 'Exit', font = myFont, command = close, bg = 'red', height = 1, width = 6)
exitButton.grid(row = 3, column = 1, sticky = E)

win.protocol("WM_DELETE_WINDOW", close)

win.mainloop()
