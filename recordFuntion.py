"""
-------------------------------
Welcome to the recording series
-------------------------------





This program records audio and creates wav files
Make sure to have a folder named "Wave_Files" in the same directory as this script





"""

import sounddevice as sd
from scipy.io.wavfile import write
import os


### Store wav files in new folder ###
main_path = os.getcwd()
wave_file_path = main_path + "/Wave_Files"


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
        file_name = file_name + ".wav"
        
        
        os.chdir(wave_file_path)            # Move to wav file folder
        write(file_name, fs, myrecording)   # Save as WAV file 
        
        
        os.chdir(main_path)                 # Move back to main folder
        
        with open("wave_files_log.txt", "a") as wave_files_log: # Record WAV file creation
            wave_files_log.write(file_name + "\n")
    
    
        print(file_name, "has been created!")
        
        



record("Foopy")







