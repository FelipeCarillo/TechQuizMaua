import customtkinter as ctk

class MainScreen(ctk.CTk):
    def __init__(self,mainFrame,Account):
        Width = 1920
        Height = 1020
        super().__init__()
        self.geometry("1920x1020")
        self.maxsize(Width, Height)
        self.config(bg="white")
        self.myframe=mainFrame(self,Account)
    
    def setFrame(self, frame):
        self.myframe=frame
