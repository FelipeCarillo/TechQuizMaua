import customtkinter as ctk
from Colors import *
from Images import ImageBack, ImageQuestao


def QuizLayout():
    Width = 1920
    Height = 1020
    QuizL = ctk.CTk()
    QuizL.geometry("1920x1020") 
    QuizL.maxsize(Width, Height)
    QuizL.config(bg="white")

    Back = ImageBack([110, 100])
    Questao = ImageQuestao([100, 100])

    gridQuiz = ctk.CTkCanvas(QuizL, background="#FFFFFF", width=Width, height=Height, highlightthickness=0)
    gridQuiz.grid(column=0, row=0, sticky=ctk.W)
    gridQuiz.create_rectangle(0, 0, Width, 50, fill=darkBlue, outline=darkBlue)
    gridQuiz.create_rectangle(0, 920, Width, 920 + 100, fill=darkBlue, outline=darkBlue)

    buttonBack = ctk.CTkButton(
        gridQuiz,
        image=Back,
        command=None,
        bg_color=white,
        fg_color=white,
        hover_color=white,
        text="",
        hover=False,
    )
    buttonBack.place(x=50, y=100)

    #contador de tentativas
    #Ainda falta fazer o sistema de contador, caso ele falhe soma 1, caso ganhe o quiz, mostra o valor e o zera.
    def contFalhas(text, x, y):
        displayF = ctk.CTkEntry(
            gridQuiz,
            placeholder_text=text,
            placeholder_text_color=black,
            font=("Roboto", 30, "bold"),
            width=200,
            height=30,
            bg_color=white,
            fg_color=white,
            border_color=white,
            text_color=black,
            border_width=1,
            justify="left",
        )
        displayF.configure(state=ctk.DISABLED)  # Impede de mudar o valor
        displayF.place(x=x, y=y)
        return displayF
    
    textoDisplay = contFalhas("Falhas: ", 1680, 125)
    numDisplay = contFalhas("00", 1790, 125)
    

    #Questão
    gridQuiz.create_image(330, 250, image=Questao)
    QuestaoNumber = ctk.CTkEntry(gridQuiz, placeholder_text="00", placeholder_text_color=white, font=("Roboto", 45, "bold"), width=65, height=45,
        fg_color=mainBlue, border_color=mainBlue, bg_color=mainBlue, text_color=white, border_width=1, justify="center")
    QuestaoNumber.configure(state=ctk.DISABLED)
    QuestaoNumber.place(x=296, y=222)

    QuesaoEnunci = ctk.CTkEntry(gridQuiz, placeholder_text="Texto teste: Qual é a melhor matéria do 1º Semestre?", placeholder_text_color=black, font=("Roboto", 34, "bold"), width=1250, height=68,
        fg_color=white, border_color=white, bg_color=white, text_color=black, justify="left")
    QuesaoEnunci.configure(state=ctk.DISABLED)
    QuesaoEnunci.place(x=380, y=215)
    
    def EscolhaQuesButton(text, command, x, y,):
        anyButton = ctk.CTkButton(
            gridQuiz,
            text=text,
            text_color=white,
            font=("Roboto", 34, "bold"),
            width=400,
            height=208,
            fg_color=lightGray,
            border_color=gray,
            border_width=3,
            corner_radius=20,
            hover_color=mainBlue,
            command=command
        )
        anyButton.place(x=x, y=y)

    Escolha1 = EscolhaQuesButton("Python", None, 434.2, 328.5)
    Escolha2 = EscolhaQuesButton("Java", None, 1085.7, 328.5)
    Escolha3 = EscolhaQuesButton("MySQL", None, 432.2, 650.3)
    Escolha4 = EscolhaQuesButton("MOO", None, 1085.7, 650.3)

    nomes = ctk.CTkEntry(gridQuiz, placeholder_text="@Edgar, Felipe, Gabriel, Isaías", placeholder_text_color=black, font=("Roboto", 15, "bold"), width=400, height=15, bg_color=white, fg_color=white, border_color=white)
    nomes.place(x=1670, y=895)

    QuizL.mainloop()

QuizLayout()