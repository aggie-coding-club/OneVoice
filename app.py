import tkinter
from tkinter import ttk
import time
import VoiceRecorder
import multiprocessing
from pynput import keyboard


class App:
    def __init__(self):
        self._thread = self.CreateThread()


        self.main = tkinter.Tk()
        self.main.title("OneVoice")
        self.main.geometry('600x400+250+250')
        self.main.resizable(False, False)

        self.recordButton = ttk.Button(self.main,text="Record", command=self.RunThread)
        self.recordButton.pack(ipadx=5,ipady=5,expand=True)

        self.main.mainloop()

    def Task(event=""):
        while True:
            VoiceRecorder.oneVoice()

    def RunThread(self):
        if self._thread.is_alive():
            self._thread.terminate()
        else:
            self._thread = multiprocessing.Process(target=self.Task)
            self.recordButton['text'] = "Stop Recording"
            self._thread.start()

    
    def CreateThread(self):
        return multiprocessing.Process(target=self.Task)
        
    



instance = App()
