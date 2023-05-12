import customtkinter as ctk
from Colors import *
from Images import ImageGoBack, ImageCardQuiz
from CtkFunc import createQuizBox
from Menu import InterfaceMenu

def Ranking(master, Account):
    master.title('Techquiz - Ranking')
    master.config(bg=mainBlue)

    GoBackPng = ImageGoBack([115,108])

    window = ctk.CTkCanvas(master, background=white, width=1716, height=816, highlightthickness=0)
    window.place(x=102,y=102)
    createQuizBox(window,300,300,white,'Felipe','FELIPE',None,None,None)
    
    def getPesquisa():
        if len(QuizPersonalizadoSearch.get()) == 4:
            texto = QuizPersonalizadoSearch.get()
            return texto
        
    def limitar_caracteres(entry, tamanho):
        entry.configure(validate="key", validatecommand=(entry.register(lambda texto: len(texto) <= tamanho), '%P'))

    QuizPersonalizadoSearch = ctk.CTkEntry(master=window,placeholder_text="Busque pelo ID do Jogo",placeholder_text_color=white,font=("Roboto", 30, "bold"),
            width=1310,height=85.5,bg_color=white,fg_color=lightGray2,border_color=lightGray2,text_color=white,border_width=1,justify="center", corner_radius=20, 
        )
    QuizPersonalizadoSearch.place(x=305, y=65)
    limitar_caracteres(QuizPersonalizadoSearch, 4)
    QuizPersonalizadoSearch.bind('<Key>',getPesquisa)

    def apagarRegisters(window):
        for item in window.grid_slaves():
            item.grid_forget()

    def GoMenu():
        apagarRegisters(master)


    buttonGoBack=ctk.CTkButton(window,text="",image=GoBackPng, fg_color=white,hover_color=white,bg_color=white, command=GoMenu)
    buttonGoBack.place(x=22,y=55)

    # createQuizBox(window,100.5,450,CardQuiz, None,None,None,10,None)
    master.mainloop()

