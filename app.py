import wx
import wav2txt


class AppFrame(wx.Frame):
    
    def __init__(self):
        wx.Frame.__init__(self, parent=None, title = "OneVoice")
        # sizer controls where things are placed horozontally along the top of the application
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)
        
        # fileLoc and transcript start as empty texts and are filled when a file is loaded in
        self.fileLoc = wx.StaticText(self, -1, "", pos=wx.Point(5,35))
        self.transcript = wx.StaticText(self, -1, "", pos=wx.Point(5,55))
        
        # creates the button to open file explorer
        self.file = wx.Button(self, label="Open File")
        self.file.Bind(wx.EVT_BUTTON, self.GetFile)
        
        # creates the button to clear fileLoc and transcript
        self.clear = wx.Button(self, label="Clear")
        self.clear.Bind(wx.EVT_BUTTON, self.ClearTrans)
        
        # add the buttons to the sizer
        self.sizer.Add(self.file, 0, wx.ALL, 5)
        self.sizer.Add(self.clear, 0, wx.ALL, 5)

        # sets the sizer to control the application
        self.SetSizer(self.sizer)
        self.Maximize(True)
        self.Show()
        
    # code for creating the file explorer and filtering out any non .wav files
    def GetFile(self, event):
        fileExplorer = wx.FileDialog(
            frame, "Open", "", "", "WAV File (*.wav)|*.wav", 
            wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        fileExplorer.ShowModal()
        self.WriteTrans(fileExplorer.GetPath())
    
    # sets fileLoc and transcript to be empty strings
    def ClearTrans(self, event):
        self.fileLoc.Label=""
        self.transcript.Label=""
    
    # gets the pythorch code in wav2txt to create the transcript and prints the transcripts and file location
    def WriteTrans(self, folder_path):
        # trans rights
        self.fileLoc.Label = folder_path
        self.transcript.Label = wav2txt.transcript(folder_path)
        
        

# launches the application
app = wx.App(False)
frame = AppFrame()
app.MainLoop()
