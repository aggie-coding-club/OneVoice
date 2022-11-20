import tkinter
from tkinter import ttk
import time
import VoiceRecorder
import multiprocessing

class App:
    def __init__(self):
        #create thread to run VoiceRec on
        print('hit')
        self._thread = self.CreateThread()
        self.recording = False

        #create app
        self.main = tkinter.Tk()
        self.main.title("OneVoice")
        self.main.geometry('600x400+250+250')
        self.main.resizable(False, False)

        #create record button
        self.recordButton = ttk.Button(self.main,text="Record", command=self.RunThread)
        self.recordButton.pack(ipadx=5,ipady=5,expand=True)    

    def RunThread(self):
        if self.recording:
            self._thread.terminate()
            self.recordButton['text'] = "Record"
            self.recording = False
        else:
            self._thread = self.CreateThread()
            self.recordButton['text'] = "Stop Recording"
            self._thread.start()
            self.recording = True

    
    def CreateThread(self):
        return multiprocessing.Process(target=self.test)
    def test():
        VoiceRecorder.oneVoice()
        
    


print('hit2')
instance = App()
instance.main.mainloop()
