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
    Height = 1020
    Menu = ctk.CTk()
    Menu.geometry("1920x1020")
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
    # inputNome = inputBox(gridInfo, Account.getNome(), 324, 85, 38, 500)
    # inputCurso = inputBox(gridInfo, Account.getCurso(), 324, 85, 38, 620)
    # inputAno = inputBox(gridInfo, Account.getAno(), 324, 85, 38, 740)

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
        # inputNome.configure(state=ctk.NORMAL)
        # inputCurso.configure(state=ctk.NORMAL)
        # inputAno.configure(state=ctk.NORMAL)
        #comando pra salvar informações no banco de dados
        buttonEditar.configure(image=checkInfosPng, command=botao_Confirmar)

    def botao_Confirmar():
        #Botão de Confirmar
        # inputNome.configure(state=ctk.DISABLED)
        # inputCurso.configure(state=ctk.DISABLED)
        # inputAno.configure(state=ctk.DISABLED)

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
    buttonRank.place(x=100, y=820)

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
    
    def QuizDescribe(text, width, x, y):
        descQuiz = ctk.CTkEntry(
            master=gridOpcoes,
            placeholder_text=text,
            placeholder_text_color=black,
            font=("Roboto", 20, "bold"),
            width=width,
            height=20,
            bg_color=lightGray,
            fg_color=lightGray,
            border_color=lightGray,
            text_color=black,
            border_width=1,
            justify="left",
        )
        descQuiz.configure(state=ctk.DISABLED)  # Impede de mudar o valor
        descQuiz.place(x=x, y=y)
        return descQuiz

    def QuizButton(text, x, y, command):
        Button = ctk.CTkButton(
            master=gridOpcoes,
            text=text,
            font=("Roboto", 28, "bold"),
            text_color=white,
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
    gridOpcoes.create_image(250, 600, image=CardQuiz)
    NomeQuiz = QuizBox(gridOpcoes, "Python", 200, 37, 113, 448)
    QuizDescribe("Criador: TechQuiz", 250, 113, 506)
    QuizDescribe("Nº Perguntas: 10", 250, 113, 536)
    ButtonJogar = QuizButton("Jogar", 140, 720, rank)

    #Quiz Java
    gridOpcoes.create_image(590, 600, image=CardQuiz)
    NomeQuiz = QuizBox(gridOpcoes, "Java", 200, 37, 453, 448)
    QuizDescribe("Criador: TechQuiz", 250, 453, 506)
    QuizDescribe("Nº Perguntas: 10", 250, 453, 536)
    ButtonJogar = QuizButton("Jogar", 480, 720, rank)

    #Quiz MySQL
    gridOpcoes.create_image(930, 600, image=CardQuiz)
    NomeQuiz = QuizBox(gridOpcoes, "MySQL", 200, 37, 793, 448)
    QuizDescribe("Criador: TechQuiz", 250, 793, 506)
    QuizDescribe("Nº Perguntas: 10", 250, 793, 536)
    ButtonJogar = QuizButton("Jogar", 820, 720, rank)

    #Quiz MOO
    gridOpcoes.create_image(1270, 600, image=CardQuiz)
    NomeQuiz = QuizBox(gridOpcoes, "MOO", 200, 37, 1133, 448)
    QuizDescribe("Criador: TechQuiz", 250, 1133, 506)
    QuizDescribe("Nº Perguntas: 10", 250, 1133, 536)
    ButtonJogar = QuizButton("Jogar", 1160, 720, rank)

    #Quiz Personalizado
    QuizPersonalizado = ctk.CTkEntry(master=gridOpcoes, placeholder_text="QUIZ PERSONALIZADO", placeholder_text_color=black, font=("Roboto", 42, "bold"),
            width=500, height=44, bg_color=white, fg_color=white, border_color=white, text_color=black, border_width=1, justify="left",)
    QuizPersonalizado.configure(state=ctk.DISABLED)  # Impede de mudar o valor
    QuizPersonalizado.place(x=85, y=40)

    QuizPersonalizadotxt = ctk.CTkEntry(master=gridOpcoes, placeholder_text="Caso queira jogar um quiz criado pelo seu professor insira o código de acesso a baixo:",
            placeholder_text_color=black, font=("Roboto", 18, "bold"), width=800, height=20, bg_color=white, fg_color=white, border_color=white, text_color=black,border_width=1, justify="left",)
    QuizPersonalizadotxt.configure(state=ctk.DISABLED)  # Impede de mudar o valor
    QuizPersonalizadotxt.place(x=90, y=90)

    QuizPersonalizadoSerch = ctk.CTkEntry(master=gridOpcoes,placeholder_text="XXXXX",placeholder_text_color=white,font=("Roboto", 30, "bold"),
            width=800,height=32,bg_color=white,fg_color=lightGray2,border_color=lightGray2,text_color=white,border_width=1,justify="left", corner_radius=20 
        )
    QuizPersonalizadoSerch.place(x=95, y=120)

    gridOpcoes.create_image(1150, 200, image=CardQuiz)
    NomeQuiz = QuizBox(gridOpcoes, "Pendente...", 200, 37, 1013, 48)
    QuizDescribe("Criador:", 250, 1013, 106)
    QuizDescribe("...", 172, 1100, 106)
    QuizDescribe("Nº Perguntas:", 250, 1013, 136)
    QuizDescribe("...", 110, 1163, 136)
    #ButtonJogar = QuizButton("Jogar", 990, 320, rank)

    Menu.mainloop()

Menu(1)