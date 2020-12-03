#!/usr/bin/env python
# coding: utf-8

# In[1]:


# plot_microphone_input_spectrum.py

"""
Using Pyaudio, get audio input and plot real-time FFT of blocks.
Ivan Selesnick, October 2015
Based on program by Gerald Schuller
"""

import pyaudio
import struct
from matplotlib import pyplot as plt
import numpy as np


get_ipython().run_line_magic('matplotlib', 'notebook')

plt.ion()           # Turn on interactive mode so plot gets updated

WIDTH     = 2         # bytes per sample
CHANNELS  = 1         # mono
RATE      = 8000     # Sampling rate (samples/second)
BLOCKSIZE = 1024      # length of block (samples)
DURATION  = 18        # Duration (seconds)

NumBlocks = int( DURATION * RATE / BLOCKSIZE ) # num of blocks = number of total samples / block size

print('BLOCKSIZE =', BLOCKSIZE)
print('NumBlocks =', NumBlocks)
print('Running for ', DURATION, 'seconds...')

DBscale = False
# DBscale = True

# Initialize plot window:
fig = plt.figure()

f = RATE/BLOCKSIZE * np.arange(0, BLOCKSIZE) # xdata is the frequency list

ax1 = fig.gca()
line1, = ax1.plot([],[],'r')
line1.set_xdata(f)
ax1.set_title('frequency spectra of microphone input and AM output')

ax2 = fig.gca()
line2, = ax2.plot([],[],'b')
line2.set_xdata(f)


if DBscale:
    plt.ylim(0, 150)
else:
    plt.ylim(0, 20*RATE)

# Frequency axis (Hz)
plt.xlim(0, 0.5*RATE)         # set x-axis limits
# plt.xlim(0, 2000)         # set x-axis limits
plt.xlabel('Frequency (Hz)')
line1.set_label("FFT of input signal")
line2.set_label("FFT of AM output")
plt.legend()

# line, = plt.plot([], [], color = 'blue')  # Create empty line
# line.set_xdata(f)                         # x-data of plot (frequency)


# Initialize phase for AM
f0 = 400    # Modulation frequency (Hz)
om = 2*np.pi*f0/RATE
theta = 0

output_block = np.zeros(BLOCKSIZE)


# Open audio device:
p = pyaudio.PyAudio()
PA_FORMAT = p.get_format_from_width(WIDTH)

stream = p.open(
    format    = PA_FORMAT,
    channels  = CHANNELS,
    rate      = RATE,
    input     = True,
    output    = True,
#     output_device_index = 5, # hear my voice from headphone
#     input_device_index = 0) # laptop as input
    output_device_index = 1, # hear my voice from headphone
    input_device_index = 4) # laptop as input


for i in range(0, NumBlocks):
    
#     input_bytes = stream.read(BLOCKSIZE)                     # Read audio input stream
    input_bytes = stream.read(BLOCKSIZE, exception_on_overflow = False)   # BLOCKLEN = number of frames read
    
    input_tuple = struct.unpack('h' * BLOCKSIZE, input_bytes)  # Convert
    X1 = np.fft.fft(input_tuple)

    
    # Go through block
    for n in range(0, BLOCKSIZE):
        # No processing:
        # output_block[n] = input_tuple[n]  
        # OR
        # Amplitude modulation:
        theta = theta + om
        output_block[n] = input_tuple[n] * np.cos(theta)
    
    X2 = np.fft.fft(output_block)
    
    # keep theta betwen -pi and pi
    while theta > np.pi:
        theta = theta - 2*np.pi

        
    # Convert values to binary data
    output_block = output_block.astype(np.int64)
    output_bytes = struct.pack('h' * BLOCKSIZE, *output_block)
    
    # Write binary data to audio output stream
    stream.write(output_bytes)
    
    
    # Update y-data of plot
    if DBscale:
        line1.set_ydata(20 * np.log10(np.abs(X1)))
        line2.set_ydata(20 * np.log10(np.abs(X2)))
    else:
        line1.set_ydata(np.abs(X1))
        line2.set_ydata(np.abs(X2))


    plt.pause(0.00001)  # *************
    fig.canvas.draw()  # *************

    
plt.close()

stream.stop_stream()
stream.close()
p.terminate()

plt.ioff()

print('* Finished')

