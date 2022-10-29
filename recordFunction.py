import sounddevice as sd
import scipy.io.wavfile as wavefile
import os
import numpy as np
import matplotlib.pyplot as plt



def record(file_name, duration = 5, fs = 44100):
    ''' Will record audio as wave file'''
    
    
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
        
def basicPlot(file_name):
    
    Fs, audio = wavefile.read(file_name)
    
    
    time = np.linspace(0, len(audio) / Fs, num=len(audio))
    
    
    plt.plot(time, audio)
    plt.ylabel("Amplitude")
    plt.xlabel("Time (seconds)")
    plt.show()
        
       
def spectrogram(file_name):
    ''' Will display a wav file as a spectrogram'''
    
    Fs, audio = wavefile.read(file_name)
    powerSpectrum, frequenciesFound, time, imageAxis = plt.specgram(audio, Fs=Fs)
    
    plt.title(file_name)
    plt.xlabel("Time (seconds)")
    plt.ylabel("Frequency (hz)")
    plt.show()
    



file_name = "Foopy.wav"
record(file_name)
basicPlot(file_name)
spectrogram(file_name)















