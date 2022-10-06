"""
-------------------------------
Welcome to the recording series
-------------------------------





This program records audio and creates wav files
Make sure to have a folder named "Wave_Files" in the same directory as this script





"""

import sounddevice as sd
import scipy.io.wavfile as wavefile
import os
import numpy as np
import matplotlib.pyplot as plt



# ### Store wav files in new folder ###
# main_path = os.getcwd()
# wave_file_path = main_path + "/Wave_Files"


fs = 44100  # Sample rate in Hz
duration = 1  # Length of recording in seconds



def record(file_name):
    
    
    ### User input to start recording ###
    user_input = input("Start recording? (y/n) ")
    if user_input == "y":
        
        ### Recording happens ###
        myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
        sd.wait()  
        
        
        ### Create a file name ###
        if ".wav" not in file_name:
            file_name = file_name + ".wav"
        
        
        wavefile.write(file_name, fs, myrecording)   # Save as WAV file 
        
        print(file_name, "has been created!")
        
        


file_name = "Foopy.wav"
record(file_name)

# Fs, aud = wavefile.read(file_name)
# aud = aud[:,0]
# powerSpectrum, frequenciesFound, time, imageAxis = plt.specgram(aud, Fs=Fs)
# plt.show()










