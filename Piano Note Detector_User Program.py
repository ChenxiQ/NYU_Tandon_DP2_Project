"""
This is the user program of the project "Piano Note Detector"
produced by Chenxi Qian and Weixiang Liu (Victor)

This program will display the detected keynotes on the GUI window.
"""


import pyaudio
import struct
import numpy as np
import tkinter as Tk
from scipy.fft import fft
from scipy import signal
import time


# GUI functions definition
def quitGUI():  # Quit the GUI
    global CONTINUE
    print('Quit...Goodbye')
    CONTINUE = False


def resetKeyboard():  # Reset the keyboard
    LabelC4.config(bg='white')
    LabelD4.config(bg='white')
    LabelE4.config(bg='white')
    LabelF4.config(bg='white')
    LabelG4.config(bg='white')
    LabelA4.config(bg='white')
    LabelB4.config(bg='white')
    LabelC5.config(bg='white')
    LabelD5.config(bg='white')
    LabelE5.config(bg='white')
    LabelF5.config(bg='white')
    LabelG5.config(bg='white')
    LabelA5.config(bg='white')
    LabelB5.config(bg='white')
    LabelC4Sharp.config(bg='gray60')
    LabelD4Sharp.config(bg='gray60')
    LabelF4Sharp.config(bg='gray60')
    LabelG4Sharp.config(bg='gray60')
    LabelA4Sharp.config(bg='gray60')
    LabelC5Sharp.config(bg='gray60')
    LabelD5Sharp.config(bg='gray60')
    LabelF5Sharp.config(bg='gray60')
    LabelG5Sharp.config(bg='gray60')
    LabelA5Sharp.config(bg='gray60')
    LabelTimeStatus.config(text='')
    LabelPressedKey.config(text='')


def C4Pressed():  # Indicate user that key C4 was pressed and detected
    resetKeyboard()  # Reset keyboard
    # Print keynote information
    LabelTimeStatus.config(text=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ':')
    LabelPressedKey.config(text='C4 Pressed.')
    LabelC4.config(bg='yellow')  # Highlight corresponding keynote


def D4Pressed():
    resetKeyboard()
    LabelTimeStatus.config(text=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ':')
    LabelPressedKey.config(text='D4 Pressed.')
    LabelD4.config(bg='yellow')


def E4Pressed():
    resetKeyboard()
    LabelTimeStatus.config(text=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ':')
    LabelPressedKey.config(text='E4 Pressed.')
    LabelE4.config(bg='yellow')


def F4Pressed():
    resetKeyboard()
    LabelTimeStatus.config(text=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ':')
    LabelPressedKey.config(text='F4 Pressed.')
    LabelF4.config(bg='yellow')


def G4Pressed():
    resetKeyboard()
    LabelTimeStatus.config(text=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ':')
    LabelPressedKey.config(text='G4 Pressed.')
    LabelG4.config(bg='yellow')


def A4Pressed():
    resetKeyboard()
    LabelTimeStatus.config(text=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ':')
    LabelPressedKey.config(text='A4 Pressed.')
    LabelA4.config(bg='yellow')


def B4Pressed():
    resetKeyboard()
    LabelTimeStatus.config(text=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ':')
    LabelPressedKey.config(text='B4 Pressed.')
    LabelB4.config(bg='yellow')


def C5Pressed():
    resetKeyboard()
    LabelTimeStatus.config(text=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ':')
    LabelPressedKey.config(text='C5 Pressed.')
    LabelC5.config(bg='yellow')


def D5Pressed():
    resetKeyboard()
    LabelTimeStatus.config(text=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ':')
    LabelPressedKey.config(text='D5 Pressed.')
    LabelD5.config(bg='yellow')


def E5Pressed():
    resetKeyboard()
    LabelTimeStatus.config(text=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ':')
    LabelPressedKey.config(text='E5 Pressed.')
    LabelE5.config(bg='yellow')


def F5Pressed():
    resetKeyboard()
    LabelTimeStatus.config(text=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ':')
    LabelPressedKey.config(text='F5 Pressed.')
    LabelF5.config(bg='yellow')


def G5Pressed():
    resetKeyboard()
    LabelTimeStatus.config(text=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ':')
    LabelPressedKey.config(text='G5 Pressed.')
    LabelG5.config(bg='yellow')


def A5Pressed():
    resetKeyboard()
    LabelTimeStatus.config(text=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ':')
    LabelPressedKey.config(text='A5 Pressed.')
    LabelA5.config(bg='yellow')


def B5Pressed():
    resetKeyboard()
    LabelTimeStatus.config(text=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ':')
    LabelPressedKey.config(text='B5 Pressed.')
    LabelB5.config(bg='yellow')


def C4SharpPressed():
    resetKeyboard()
    LabelTimeStatus.config(text=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ':')
    LabelPressedKey.config(text='C#4 Pressed.')
    LabelC4Sharp.config(bg='yellow')


def D4SharpPressed():
    resetKeyboard()
    LabelTimeStatus.config(text=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ':')
    LabelPressedKey.config(text='D#4 Pressed.')
    LabelD4Sharp.config(bg='yellow')


def F4SharpPressed():
    resetKeyboard()
    LabelTimeStatus.config(text=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ':')
    LabelPressedKey.config(text='F#4 Pressed.')
    LabelF4Sharp.config(bg='yellow')


def G4SharpPressed():
    resetKeyboard()
    LabelTimeStatus.config(text=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ':')
    LabelPressedKey.config(text='G#4 Pressed.')
    LabelG4Sharp.config(bg='yellow')


def A4SharpPressed():
    resetKeyboard()
    LabelTimeStatus.config(text=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ':')
    LabelPressedKey.config(text='A#4 Pressed.')
    LabelA4Sharp.config(bg='yellow')


def C5SharpPressed():
    resetKeyboard()
    LabelTimeStatus.config(text=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ':')
    LabelPressedKey.config(text='C#5 Pressed.')
    LabelC5Sharp.config(bg='yellow')


def D5SharpPressed():
    resetKeyboard()
    LabelTimeStatus.config(text=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ':')
    LabelPressedKey.config(text='D#5 Pressed.')
    LabelD5Sharp.config(bg='yellow')


def F5SharpPressed():
    resetKeyboard()
    LabelTimeStatus.config(text=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ':')
    LabelPressedKey.config(text='F#5 Pressed.')
    LabelF5Sharp.config(bg='yellow')


def G5SharpPressed():
    resetKeyboard()
    LabelTimeStatus.config(text=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ':')
    LabelPressedKey.config(text='G#5 Pressed.')
    LabelG5Sharp.config(bg='yellow')


def A5SharpPressed():
    resetKeyboard()
    LabelTimeStatus.config(text=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ':')
    LabelPressedKey.config(text='A#5 Pressed.')
    LabelA5Sharp.config(bg='yellow')


# GUI setting
CONTINUE = True

# Define Tk root
root = Tk.Tk()
root.geometry('800x600')

# Define Tk variables
Button_Quit = Tk.Button(root, text='Quit', command=quitGUI)
LabelC4 = Tk.Label(root, text='\n\n\n\n\n\n\nC4', borderwidth=3, relief='raised', width=4, height=14)
LabelD4 = Tk.Label(root, text='\n\n\n\n\n\n\nD4', borderwidth=3, relief='raised', width=4, height=14)
LabelE4 = Tk.Label(root, text='\n\n\n\n\n\n\nE4', borderwidth=3, relief='raised', width=4, height=14)
LabelF4 = Tk.Label(root, text='\n\n\n\n\n\n\nF4', borderwidth=3, relief='raised', width=4, height=14)
LabelG4 = Tk.Label(root, text='\n\n\n\n\n\n\nG4', borderwidth=3, relief='raised', width=4, height=14)
LabelA4 = Tk.Label(root, text='\n\n\n\n\n\n\nA4', borderwidth=3, relief='raised', width=4, height=14)
LabelB4 = Tk.Label(root, text='\n\n\n\n\n\n\nB4', borderwidth=3, relief='raised', width=4, height=14)
LabelC5 = Tk.Label(root, text='\n\n\n\n\n\n\nC5', borderwidth=3, relief='raised', width=4, height=14)
LabelD5 = Tk.Label(root, text='\n\n\n\n\n\n\nD5', borderwidth=3, relief='raised', width=4, height=14)
LabelE5 = Tk.Label(root, text='\n\n\n\n\n\n\nE5', borderwidth=3, relief='raised', width=4, height=14)
LabelF5 = Tk.Label(root, text='\n\n\n\n\n\n\nF5', borderwidth=3, relief='raised', width=4, height=14)
LabelG5 = Tk.Label(root, text='\n\n\n\n\n\n\nG5', borderwidth=3, relief='raised', width=4, height=14)
LabelA5 = Tk.Label(root, text='\n\n\n\n\n\n\nA5', borderwidth=3, relief='raised', width=4, height=14)
LabelB5 = Tk.Label(root, text='\n\n\n\n\n\n\nB5', borderwidth=3, relief='raised', width=4, height=14)
LabelC4Sharp = Tk.Label(root, text='C#4', borderwidth=3, relief='raised', width=4, height=8, bg='gray60')
LabelD4Sharp = Tk.Label(root, text='D#4', borderwidth=3, relief='raised', width=4, height=8, bg='gray60')
LabelF4Sharp = Tk.Label(root, text='F#4', borderwidth=3, relief='raised', width=4, height=8, bg='gray60')
LabelG4Sharp = Tk.Label(root, text='G#4', borderwidth=3, relief='raised', width=4, height=8, bg='gray60')
LabelA4Sharp = Tk.Label(root, text='A#4', borderwidth=3, relief='raised', width=4, height=8, bg='gray60')
LabelC5Sharp = Tk.Label(root, text='C#5', borderwidth=3, relief='raised', width=4, height=8, bg='gray60')
LabelD5Sharp = Tk.Label(root, text='D#5', borderwidth=3, relief='raised', width=4, height=8, bg='gray60')
LabelF5Sharp = Tk.Label(root, text='F#5', borderwidth=3, relief='raised', width=4, height=8, bg='gray60')
LabelG5Sharp = Tk.Label(root, text='G#5', borderwidth=3, relief='raised', width=4, height=8, bg='gray60')
LabelA5Sharp = Tk.Label(root, text='A#5', borderwidth=3, relief='raised', width=4, height=8, bg='gray60')
LabelTimeStatus = Tk.Label(root, text='')
LabelPressedKey = Tk.Label(root, text='')

# Place Tk variables
Button_Quit.place(x=0, y=0)
LabelC4.place(x=80, y=80)
LabelD4.place(x=120, y=80)
LabelE4.place(x=160, y=80)
LabelF4.place(x=200, y=80)
LabelG4.place(x=240, y=80)
LabelA4.place(x=280, y=80)
LabelB4.place(x=320, y=80)
LabelC5.place(x=360, y=80)
LabelD5.place(x=400, y=80)
LabelE5.place(x=440, y=80)
LabelF5.place(x=480, y=80)
LabelG5.place(x=520, y=80)
LabelA5.place(x=560, y=80)
LabelB5.place(x=600, y=80)
LabelC4Sharp.place(x=100, y=80)
LabelD4Sharp.place(x=140, y=80)
LabelF4Sharp.place(x=220, y=80)
LabelG4Sharp.place(x=260, y=80)
LabelA4Sharp.place(x=300, y=80)
LabelC5Sharp.place(x=380, y=80)
LabelD5Sharp.place(x=420, y=80)
LabelF5Sharp.place(x=500, y=80)
LabelG5Sharp.place(x=540, y=80)
LabelA5Sharp.place(x=580, y=80)
LabelTimeStatus.place(x=100, y=360)
LabelPressedKey.place(x=100, y=380)

# Detection setting
octave = 12  # A piano has 12 pitches in an octave
A4 = 440  # Standard A4 note has a frequency of 440 Hz, but each piano can be different by 0~3 Hz
total_keys = 88  # 88-key piano
true_freq = np.round(A4 * (2 ** (((np.arange(0, total_keys) + 1) - 49) / octave)), 4)  # frequencies list for each note

WIDTH = 2  # Bytes per sample
CHANNELS = 1  # Mono
RATE = int(true_freq[-1] * 2)  # Sampling Rate
DURATION = 600  # Duration (sec)
BLOCKSIZE = 700  # BLOCKSIZE is set to an appropriate value to get an appropriate bin size
NumBlocks = int(DURATION * RATE / BLOCKSIZE)  # Num of blocks = number of total samples / block size

note_list = np.array(['C4', 'C4Sharp', 'D4', 'D4Sharp', 'E4', 'F4', 'F4Sharp', 'G4', 'G4Sharp',
                      'A4', 'A4Sharp', 'B4', 'C5', 'C5Sharp', 'D5', 'D5Sharp', 'E5', 'F5',
                      'F5Sharp', 'G5', 'G5Sharp', 'A5', 'A5Sharp', 'B5'])

# The frequency range for our project
low_freq_ind = 39  # 40th key -- C4 -- ~261.6Hz
high_freq_ind = 62  # 63th key -- B5 -- ~987.7Hz
total_note_num = (high_freq_ind - low_freq_ind) + 1  # +1: cuz the range is inclusive

f = (RATE / BLOCKSIZE) * np.arange(0, BLOCKSIZE)  # fft frequency list

window = signal.hamming(BLOCKSIZE)  # Hamming window to smooth input data array

num_of_fundamental = 1  # It's fixed: make the code easier to understand
num_of_harmonics = 4  # Num of harmonics to include into the sum of magnitude

# This would include the left and the right points when computing sum of magnitude
# because if any frequency is off by a bin, we can still count it in; it would not be missed
num_points_approx = 3

# For storing sum of magnitude values of each notes
note_mag_sum = np.zeros(total_note_num)

# Compute the ratio of the power at the fundamental frequency position to the total sum
powers_sum_percentage = np.zeros(total_note_num)

# Used to construct a correct "note_pos" matrix
note_pos_temp = np.zeros((total_note_num, num_of_fundamental + num_of_harmonics))

# Fundamental and harmonics' indices in f
note_pos = np.zeros((total_note_num, num_points_approx * (num_of_fundamental + num_of_harmonics)))

note_pos_temp[:, 0] = true_freq[low_freq_ind:high_freq_ind + 1]  # put the fundamental frequencies in first

# Obtain, for each note, their fundamental and harmonics frequencies
for i in range(1, num_of_fundamental + num_of_harmonics):
    note_pos_temp[:, i] = (i + 1) * note_pos_temp[:, 0]

# Compute the closest frequencies compare to FFT frequency list. But they are all in terms of indices in "f"
for i in range(total_note_num):
    for j in range(1 + num_of_harmonics):
        note_pos_temp[i, j] = np.argmin(np.abs(note_pos_temp[i, j] - f))

# Obtain all the left and right point indices for each note and their harmonics
for i in range(0, num_points_approx * (num_of_fundamental + num_of_harmonics), num_points_approx):
    for j in range(num_points_approx):
        note_pos[:, i + j] = note_pos_temp[:, int(i / num_points_approx)] + (j - 1)


# Open audio device:
p = pyaudio.PyAudio()
stream = p.open(
    format=p.get_format_from_width(WIDTH),
    channels=CHANNELS,
    rate=RATE,
    input=True,
    output=False,
    input_device_index=0)

for i in range(0, NumBlocks):

    if not CONTINUE:  # If quit is clicked, then the main for-loop will be broken and code will stop
        break

    root.update()

    # Read data
    input_bytes = stream.read(BLOCKSIZE, exception_on_overflow=False)
    input_tuple = np.asarray(struct.unpack('h' * BLOCKSIZE, input_bytes))

    # Computing FFT:
    X1 = np.abs(fft(input_tuple * window))  # Use a Hamming window to smooth current segment of signal

    if np.max(X1) > 10000:  # 10000 is used basically as an arbitrary power level for note on-set detection

        # Summing up all powers for each note at their fundamental and harmonics frequencies
        # also consider one left and one right point of each frequency in case position is off by a little
        for j in range(total_note_num):
            powers = X1[note_pos[j, :].astype(int)]  # get the powers with indices
            powers_sum = np.sum(powers)
            powers_sum_percentage[j] = np.sum(powers[:num_points_approx]) / powers_sum  # compute percentage
            note_mag_sum[j] = powers_sum

        sorted_powers_ind = np.argsort(note_mag_sum)[::-1]  # Get the sum of powers into descending order

        # Start from the largest power, if any fundamental frequency to total power ratio is > 0.1,
        # then the note that has that fundamental frequency is our best guess
        for k in range(total_note_num):
            if powers_sum_percentage[sorted_powers_ind[k]] > 0.1:
                output_note_ind = sorted_powers_ind[k]
                break

        eval(note_list[output_note_ind] + 'Pressed()')  # Call the GUI functions accordingly

stream.stop_stream()
stream.close()
p.terminate()
