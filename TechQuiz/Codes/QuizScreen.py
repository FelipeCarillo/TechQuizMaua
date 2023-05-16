import customtkinter as ctk
from Colors import *
from DataBase import getPerAltQuiz
from Images import ImageGoBack, ImageQuestao
from Quiz import Quiz
# from MainScreen import MainScreen
# from MenuClass import Menu

class QuizScreen(ctk.CTk):
    def __init__(self, Account, Quiz):
        Width = 1920
        Height = 1020
        super().__init__()
        self.geometry("1920x1020") 
        self.maxsize(Width, Height)
        screen = ctk.CTkCanvas(self, background="#FFFFFF", width=Width, height=Height, highlightthickness=0)
        screen.pack()
        screen.create_rectangle(0, 0, Width, 50, fill=darkBlue, outline=darkBlue)
        screen.create_rectangle(0, 970, Width, Height, fill=darkBlue, outline=darkBlue)
        
        def a():
            print(Quiz.get_questoes())
        
        buttonBack = ctk.CTkButton(
            screen,
            text='SAIR',
            command=a,
            bg_color=white,
            fg_color=red,
            hover_color=white
        )
        buttonBack.place(x=50, y=880)

        

        Questao = ImageQuestao([100, 100])
        ctk.CTkButton(screen,image=Questao,text='',fg_color=white,hover=None).place(x=5,y=60)
        
        screen.create_rectangle(200, 100,1720,400,fill=mainBlue,outline=mainBlue)
        ctk.CTkLabel(screen,anchor='nw',justify='left',text='a'
                     ,font=("Roboto", 30, "bold"),text_color=white,fg_color=mainBlue,bg_color=mainBlue,wraplength=1720-250).place(x=225,y=105)
        # ctk.CTkButton(screen,width=600,height=200,fg_color=lightGray,text=alt1,font=("Roboto", 34, "bold")).place(x=200,y=450)
        # ctk.CTkButton(screen,width=600,height=200,fg_color=lightGray,text=alt2,font=("Roboto", 34, "bold")).place(x=200,y=670)
        # ctk.CTkButton(screen,width=600,height=200,fg_color=lightGray,text=alt3,font=("Roboto", 34, "bold")).place(x=1120,y=450)
        # ctk.CTkButton(screen,width=600,height=200,fg_color=lightGray,text=alt4,font=("Roboto", 34, "bold")).place(x=1120,y=670)

# df = getPerAltQuiz(1)

# quiz = Quiz(1,'TechQuiz','Python','Lógica de Programação',df)

# QuizScreen(1,quiz).mainloop()