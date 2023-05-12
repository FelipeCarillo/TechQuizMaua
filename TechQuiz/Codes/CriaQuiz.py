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

    #Questão
    varquest = 1
    gridQuiz.create_image(330, 250, image=Questao)
    QuestaoNumber = ctk.CTkEntry(gridQuiz, placeholder_text=varquest, placeholder_text_color=white, font=("Roboto", 45, "bold"), width=65, height=45,
        fg_color=mainBlue, border_color=mainBlue, bg_color=mainBlue, text_color=white, border_width=1, justify="center")
    QuestaoNumber.configure(state=ctk.DISABLED)
    QuestaoNumber.place(x=296, y=222)

    QuesaoEnunci = ctk.CTkEntry(gridQuiz, placeholder_text="Insira a questão!", placeholder_text_color=black, font=("Roboto", 34, "bold"), width=1250, height=68,
        fg_color=lightGray, border_color=gray, bg_color=white, text_color=black, justify="left")
    QuesaoEnunci.place(x=380, y=215)
    
    def EscolhaInput(command, x, y,):
        anyButton = ctk.CTkEntry(
            gridQuiz,
            placeholder_text="Insira a escolha",
            placeholder_text_color=white,
            text_color=white,
            font=("Roboto", 34, "bold"),
            width=400,
            height=208,
            fg_color=lightGray,
            border_color=gray,
            border_width=3,
            corner_radius=20,
            justify = "center"
        )
        anyButton.place(x=x, y=y)

    ValorResp = 0
    def ValResp(x,y):
        def botao_False():
            buttonEditar.configure(fg_color=red, bg_color=lightGray, hover_color=red,command=botao_True)
            ValorResp = 0

        def botao_True():
            buttonEditar.configure(fg_color=green, bg_color=lightGray, hover_color=green, command=botao_False)
            ValorResp = 1

        buttonEditar = ctk.CTkButton(
            master=gridQuiz,
            width=40,
            height=25,
            command=botao_True,
            fg_color=red,
            bg_color=lightGray,
            hover_color=red,
            text="",
        )
        buttonEditar.place(x=x,y=y)

    Escolha1 = EscolhaInput(None, 434.2, 328.5)
    Escolha1B = ValResp(780, 500)
    Escolha2 = EscolhaInput(None, 1085.7, 328.5)
    Escolha1B = ValResp(1431.5, 500)
    Escolha3 = EscolhaInput(None, 432.2, 650.3)
    Escolha1B = ValResp(780, 821.8)
    Escolha4 = EscolhaInput(None, 1085.7, 650.3)
    Escolha1B = ValResp(1434.5, 821.8)

    nomes = ctk.CTkEntry(gridQuiz, placeholder_text="@Edgar, Felipe, Gabriel, Isaías", placeholder_text_color=black, font=("Roboto", 15, "bold"), width=400, height=15, bg_color=white, fg_color=white, border_color=white)
    nomes.place(x=1670, y=895)

    QuizL.mainloop()

QuizLayout()