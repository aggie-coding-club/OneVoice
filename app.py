import wx
import wav2txt
#import voiceRec

class AppFrame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, parent=None, title="OneVoice")
        # sizer controls where things are placed horozontally along the top of the application
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)

        # fileLoc and transcript start as empty texts and are filled when a file is loaded in
        self.fileLoc = wx.StaticText(self, -1, "", pos=wx.Point(5, 75))
        self.transcript = wx.StaticText(self, -1, "", pos=wx.Point(5, 95))

        # creates the button to begin audio recording
        self.record = wx.Button(self, size=wx.Size(30, 30), label=chr(
            9210), style=wx.BORDER_NONE, pos=wx.Point(5, 35))
        self.record.Bind(wx.EVT_BUTTON, self.Record)

        # creates the button to open file explorer
        self.file = wx.Button(self, label="Open File")
        self.file.Bind(wx.EVT_BUTTON, self.GetFile)

        # creates the button to clear fileLoc and transcript
        self.clear = wx.Button(self, label="Clear")
        self.clear.Bind(wx.EVT_BUTTON, self.ClearTrans)

        # add the buttons to the sizer
        self.sizer.Add(self.file, 0, wx.ALL, 5)
        #self.sizer.Add(self.record, 0, wx.ALL, 5)
        self.sizer.Add(self.clear, 0, wx.ALL, 5)

        # sets the sizer to control the application
        self.SetSizer(self.sizer)
        self.Maximize(True)
        self.Show()

    #todo: record audio file and then stop recording when pressed again
    def Record(self, event):
        if self.record.GetLabel() == chr(9210):
            self.record.SetLabel(chr(9209))
        else:
            self.record.SetLabel(chr(9210))
        #voiceRec.audioToWAV()

    # code for creating the file explorer and filtering out any non .wav files
    def GetFile(self, event):
        fileExplorer = wx.FileDialog(
            frame, "Open", "", "", "WAV File (*.wav)|*.wav",
            wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        fileExplorer.ShowModal()
        self.WriteTrans(fileExplorer.GetPath())

    # sets fileLoc and transcript to be empty strings
    def ClearTrans(self, event):
        self.fileLoc.SetLabel("")
        self.transcript.SetLabel("")

    # gets the pythorch code in wav2txt to create the transcript and prints the transcripts and file location
    def WriteTrans(self, folder_path):
        # trans rights
        self.fileLoc.Label = folder_path
        self.transcript.Label = wav2txt.transcript(folder_path)


# launches the application
app = wx.App(False)
frame = AppFrame()
app.MainLoop()
