import IPython
import matplotlib
import torch
import torchaudio
import sounddevice as sd
from scipy.io.wavfile import write
import threading
import datetime

matplotlib.rcParams["figure.figsize"] = [16.0, 4.8]

torch.random.manual_seed(0)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

print(torch.__version__)
print(torchaudio.__version__)
print(device)

fileName = str(datetime.datetime.now()) + ".wav"
rate = 44100
seconds = 15


def audioToWAV():
    recording = sd.rec(int(rate*seconds),samplerate=rate,channels=2)
    leaving = input("Press enter bring conversation to a close")
    sd.wait()
    write(fileName,rate,recording) #Return .wav file

    SPEECH_URL = fileName
    SPEECH_FILE = fileName


audioToWAV()