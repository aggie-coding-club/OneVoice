import IPython
import matplotlib
import torch
import torchaudio
import sounddevice as sd
from scipy.io.wavfile import write
import threading
import keyboard
from datetime import datetime


matplotlib.rcParams["figure.figsize"] = [16.0, 4.8]

torch.random.manual_seed(0)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# print(torch.__version__)
# print(torchaudio.__version__)
# print(device)
# print("HOLD DOWN SPACE BAR FOR 20 SECONDS TO KILL PROGRAM")



def audioToWAV():
    fileName = 'speechToText.wav'

    rate = 44100
    seconds = 10
    recording = sd.rec(int(rate*seconds), samplerate=rate, channels=2)
    sd.wait()
    write(fileName, rate, recording)  # Return .wav file

    SPEECH_URL = fileName
    SPEECH_FILE = fileName


def recgonitioner(SPEECH_FILE):
    name = str(datetime.now()).replace(' ', '_').replace('.','-').replace(':','-')

    wordTranscript = open(f'{name}.txt', "w+")


    # See different pipelines
    bundle = torchaudio.pipelines.WAV2VEC2_ASR_LARGE_LV60K_960H

    #print("Sample Rate:", bundle.sample_rate)

    #print("Labels:", bundle.get_labels())

    model = bundle.get_model().to(device)

    # print(model.__class__)

    IPython.display.Audio(SPEECH_FILE)

    waveform, sample_rate = torchaudio.load(SPEECH_FILE)
    waveform = waveform.to(device)

    if sample_rate != bundle.sample_rate:
        waveform = torchaudio.functional.resample(
            waveform, sample_rate, bundle.sample_rate)

    with torch.inference_mode():
        features, _ = model.extract_features(waveform)

    with torch.inference_mode():
        emission, _ = model(waveform)

    # Get a new decoder
    class Decoder(torch.nn.Module):
        def __init__(self, labels, blank=0):
            super().__init__()
            self.labels = labels
            self.blank = blank

        def forward(self, emission: torch.Tensor) -> str:
            indices = torch.argmax(emission, dim=-1)  # [num_seq,]
            indices = torch.unique_consecutive(indices, dim=-1)
            indices = [i for i in indices if i != self.blank]
            return "".join([self.labels[i] for i in indices])

    decoder = Decoder(labels=bundle.get_labels())
    transcript = decoder(emission[0]).split("|")
    transcript = " ".join(transcript)
    wordTranscript.write(transcript)
    wordTranscript.write("\n")
    print(transcript)
    IPython.display.Audio(SPEECH_FILE)


def oneVoice():
    fileName = 'speechToText.wav'

    audioGet = threading.Thread(target=audioToWAV(), name="audioGet")
    recgonition = threading.Thread(
        target=recgonitioner(fileName), name="recgonition")

    audioGet.start()
    recgonition.start()

    audioGet.join()
    recgonition.join()


# if __name__ == "__main__":
#    while True:
#        if keyboard.is_pressed('space'):
#            wordTranscript.close()
#            exit()
#        else:
#            oneVoice()
