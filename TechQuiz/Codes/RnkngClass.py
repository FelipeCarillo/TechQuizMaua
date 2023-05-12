from typing import Optional, Tuple, Union
import customtkinter as ctk
from Colors import *
from DataBase import hasDuplicated, setOneData
from Images import (ImageCheckEdit, ImageRnkgLogo, ImageEdit, ImageGoBack)
from Account import *
from checkValidation_Username_Email_Password import check_user_operation
from CtkFunc import createQuizBox
from MenuClass import Jogo,Menu


class Ranking(ctk.CTkFrame):
    def __init__(self, parent, Account):

        parent.title('Techquiz - Ranking')
        parent.config(bg=mainBlue)

        GoBackPng = ImageGoBack([115,108])

        window = ctk.CTkCanvas(parent, background=white, width=1716, height=816, highlightthickness=0)
        window.place(x=102,y=102)
        createQuizBox(window,300,300,white,'Felipe','FELIPE',None,None,None)
        
        def getPesquisa(event=None):
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
            apagarRegisters(parent)
            Jogo.setFrame(self,Menu(parent,Account))
            

        buttonGoBack=ctk.CTkButton(window,text="",image=GoBackPng, fg_color=white,hover_color=white,bg_color=white, command=GoMenu)
        buttonGoBack.place(x=22,y=55)

        # createQuizBox(window,100.5,450,CardQuiz, None,None,None,10,None)


