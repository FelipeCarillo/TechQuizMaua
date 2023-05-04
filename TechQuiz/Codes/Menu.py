import customtkinter as ctk
from Colors import *
from Images import (
    ImageCheckEdit,
    ImageRnkgLogo,
    ImageEdit,
    ImageLogoNEscrita,
    ImageCardQuiz
)


def Menu(Account):

    Width = 1920
    Height = 1040
    Menu = ctk.CTk()
    Menu.geometry("1920x1040")
    Menu.maxsize(Width, Height)
    Menu.config(bg="white")

    # Imagens dos botões

    RankPng = ImageRnkgLogo([203, 166])
    confInfosPng = ImageEdit([54, 54])
    checkInfosPng = ImageCheckEdit()
    imageLogo = ImageLogoNEscrita([300, 280])
    CardQuiz = ImageCardQuiz([300, 360])

    Menu.columnconfigure(0, weight=1)
    Menu.columnconfigure(1, weight=3)

    # Informações
    gridInfo = ctk.CTkCanvas(
        Menu, background="#5271FF", width=400, height=Height, highlightthickness=0
    )
    gridInfo.grid(column=0, row=0, sticky=ctk.W)
    gridInfo.create_rectangle(0, 0, 400, 50, fill=darkBlue, outline=darkBlue)
    gridInfo.create_rectangle(0, 990, 400, 990 + 50, fill=darkBlue, outline=darkBlue)

    # Opções
    gridOpcoes = ctk.CTkCanvas(
        Menu,
        background=white,
        width=Width - 400,
        height=Height,
        highlightthickness=0,
    )
    gridOpcoes.grid(column=1, row=0, sticky=ctk.E)

    def apagarRegisters(master):
        for items in master.place_slaves():
            items.place_forget()
        for items in master.find_all():
            master.delete(items)

    # Adição das informações

    def inputBox(master, text, width, height, x, y):
        inputBox = ctk.CTkEntry(
            master,
            placeholder_text=text,
            placeholder_text_color=white,
            font=("Roboto", 25, "bold"),
            width=width,
            height=height,
            fg_color=darkBlue,
            border_color=darkBlue,
            text_color=white,
            border_width=1,
            corner_radius=20,
            justify="center",
        )

        inputBox.configure(state=ctk.DISABLED)  # Impede de mudar o valor
        inputBox.place(x=x, y=y)
        return inputBox

    gridInfo.create_image(205, 320, image=imageLogo)
    inputNome = inputBox(gridInfo, Account.getNome(), 324, 85, 38, 500)
    inputCurso = inputBox(gridInfo, Account.getCurso(), 324, 85, 38, 620)
    inputAno = inputBox(gridInfo, Account.getAno(), 324, 85, 38, 740)

    # Pontuações
    def inputBoxPoint(master, text, width, height, x, y):
        inputBox = ctk.CTkEntry(
            master,
            placeholder_text=text,
            placeholder_text_color=black,
            font=("Roboto Mono Regular", 60),
            width=width,
            height=height,
            fg_color=mainBlue,
            border_color=mainBlue,
            text_color=black,
            border_width=1,
            corner_radius=360,
        )
        inputBox.configure(state=ctk.DISABLED)  # Impede de mudar o valor
        inputBox.place(x=x, y=y)
        return inputBox

    # Botão de edição de configurações
    varteste = 0

    def botao_Alterar():
        inputNome.configure(state=ctk.NORMAL)
        inputCurso.configure(state=ctk.NORMAL)
        inputAno.configure(state=ctk.NORMAL)
        #comando pra salvar informações no banco de dados
        buttonEditar.configure(image=checkInfosPng, command=botao_Confirmar)

    def botao_Confirmar():
        #Botão de Confirmar
        inputNome.configure(state=ctk.DISABLED)
        inputCurso.configure(state=ctk.DISABLED)
        inputAno.configure(state=ctk.DISABLED)

        buttonEditar.configure(image=confInfosPng, command=botao_Alterar)

    buttonEditar = ctk.CTkButton(
        master=gridInfo,
        image=confInfosPng,
        width=54,
        height=54,
        command=botao_Alterar,
        fg_color=mainBlue,
        bg_color=mainBlue,
        hover_color=mainBlue,
        text="",
    )
    buttonEditar.place(x=6.4, y=54)

    # Botões

    def createButtonInput(master, image, width, height, x, y, command, text):
        anyButton = ctk.CTkButton(
            master,
            image=image,
            text=text,
            text_color=white,
            width=width,
            height=height,
            fg_color=white,
            bg_color=white,
            hover_color=white,
            command=command,
        )
        anyButton.place(x=x, y=y)

    def rank():
        apagarRegisters(gridInfo)
        apagarRegisters(gridOpcoes)

    buttonRank = ctk.CTkButton(
        gridOpcoes,
        width=1320,
        height=166,
        image=RankPng,
        command=rank,
        text="",
        corner_radius=20,
        fg_color=mainBlue,
        hover=False,
    )
    buttonRank.place(x=100, y=850)

    def QuizBox(master, text, width, height, x, y):
        QuizBox = ctk.CTkEntry(
            master,
            placeholder_text=text,
            placeholder_text_color=black,
            font=("Roboto", 35, "bold"),
            width=width,
            height=height,
            bg_color=lightGray,
            fg_color=lightGray,
            border_color=lightGray,
            text_color=black,
            border_width=1,
            justify="left",
        )

        QuizBox.configure(state=ctk.DISABLED)  # Impede de mudar o valor
        QuizBox.place(x=x, y=y)
        return QuizBox

    def QuizButton(text, x, y, command):
        Button = ctk.CTkButton(
            master=gridOpcoes,
            text=text,
            font=("Roboto", 28, "bold"),
            width=200,
            height=32,
            command=command,
            fg_color=mainBlue,
            bg_color=lightGray,
            hover_color=mainBlue,
            corner_radius=360
        )
        Button.place(x=x, y=y)

    #Quiz Python
    gridOpcoes.create_image(250, 620, image=CardQuiz)
    NomeQuiz = QuizBox(gridOpcoes, "Python", 200, 37, 113, 468)
    ButtonJogar = QuizButton("Jogar", 140, 740, rank)

    #Quiz Java
    gridOpcoes.create_image(590, 620, image=CardQuiz)
    NomeQuiz = QuizBox(gridOpcoes, "Java", 200, 37, 453, 468)
    ButtonJogar = QuizButton("Jogar", 480, 740, rank)

    #Quiz MySQL
    gridOpcoes.create_image(930, 620, image=CardQuiz)
    NomeQuiz = QuizBox(gridOpcoes, "MySQL", 200, 37, 793, 468)
    ButtonJogar = QuizButton("Jogar", 820, 740, rank)

    #Quiz MOO
    gridOpcoes.create_image(1270, 620, image=CardQuiz)
    NomeQuiz = QuizBox(gridOpcoes, "MOO", 200, 37, 1133, 468)
    ButtonJogar = QuizButton("Jogar", 1160, 740, rank)

    Menu.mainloop()
