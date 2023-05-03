import tkinter
import customtkinter as ctk
from PIL import Image, ImageTk
import ctypes


def menu():
    Width = 1920
    Height = 1040
    Menu = ctk.CTk()
    Menu.geometry("1920x1040")
    Menu.maxsize(Width, Height)
    Menu.config(bg="white")

    # Imagens dos botões

    RankPng = Image.open("Imagens/RANKING.png")
    RankPng = ImageTk.PhotoImage(RankPng.resize(size=[203, 166]))
    confInfosPng = Image.open("Imagens/EDIT.png")
    confInfosPng = ImageTk.PhotoImage(confInfosPng.resize(size=[54, 54]))
    checkInfosPng = Image.open("Imagens/check.png")
    checkInfosPng = ImageTk.PhotoImage(checkInfosPng)
    Logo = Image.open("Imagens/LOGO_N_Escrita.png")
    Logo = ImageTk.PhotoImage(Logo.resize(size=[300, 280]))

    Menu.columnconfigure(0, weight=1)
    Menu.columnconfigure(1, weight=3)

    # Informações
    gridInfo = ctk.CTkCanvas(
        Menu, background="#5271FF", width=400, height=Height, highlightthickness=0
    )
    gridInfo.grid(column=0, row=0, sticky=ctk.W)
    gridInfo.create_rectangle(0, 0, 400, 50, fill="#304ABD", outline="#304ABD")
    gridInfo.create_rectangle(0, 990, 400, 990 + 50, fill="#304ABD", outline="#304ABD")

    # Opções
    gridOpcoes = ctk.CTkCanvas(
        Menu,
        background="#FFFFFF",
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
            placeholder_text_color="#FFFFFF",
            font=("Roboto", 25, "bold"),
            width=width,
            height=height,
            fg_color="#304ABD",
            border_color="#304ABD",
            text_color="#FFFFFF",
            border_width=1,
            corner_radius=20,
            justify="center",
        )

        inputBox.configure(state=ctk.DISABLED)  # Impede de mudar o valor
        inputBox.place(x=x, y=y)
        return inputBox

    gridInfo.create_image(205, 320, image=Logo)
    inputNome = inputBox(gridInfo, "NOME", 324, 85, 38, 500)
    inputCurso = inputBox(gridInfo, "CURSO", 324, 85, 38, 620)
    inputAno = inputBox(gridInfo, "ANO", 324, 85, 38, 740)

    # Pontuações
    def inputBoxPoint(master, text, width, height, x, y):
        inputBox = ctk.CTkEntry(
            master,
            placeholder_text=text,
            placeholder_text_color="#000000",
            font=("Roboto Mono Regular", 60),
            width=width,
            height=height,
            fg_color="#5271FF",
            border_color="#5271FF",
            text_color="#000000",
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
        # comando pra salvar informações no banco de dados
        buttonEditar.configure(image=checkInfosPng, command=botao_Confirmar)

    def botao_Confirmar():
        # Botão de Confirmar
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
        fg_color="#5271FF",
        bg_color="#5271FF",
        hover_color="#5271FF",
        text="",
    )
    buttonEditar.place(x=6.4, y=54)

    # Botões

    def createButtonInput(master, image, width, height, x, y, command, text):
        anyButton = ctk.CTkButton(
            master,
            image=image,
            text=text,
            text_color="#FFFFFF",
            width=width,
            height=height,
            fg_color="#FFFFFF",
            bg_color="#FFFFFF",
            hover_color="#FFFFFF",
            command=command,
        )
        anyButton.place(x=x, y=y)

    def quizMenu():
        Menu.withdraw()
        QuizMenu = ctk.CTk()
        QuizMenu.attributes("-fullscreen", True)
        QuizMenu.config(bg="white")
        QuizMenu.resizable(False, False)
        QuizMenu.columnconfigure(0, weight=1)

        lupaPng = Image.open("Imagens/lupa.png")
        lupaPng = ImageTk.PhotoImage(lupaPng)
        xPng = Image.open("Imagens/xPng.png")
        xPng = ImageTk.PhotoImage(xPng)

        gridQuizMenu = ctk.CTkCanvas(
            QuizMenu,
            background="#FFFFFF",
            width=1920,
            height=1080,
            highlightthickness=0,
        )
        gridQuizMenu.grid(column=0, row=0)

        def fechar():
            QuizMenu.destroy()
            menu()
            Menu.mainloop()

        def inputBox(master, text, width, height, x, y):
            inputBox = ctk.CTkEntry(
                master,
                placeholder_text=text,
                placeholder_text_color="#FFFFFF",
                font=("Roboto Mono Regular", 28),
                width=width,
                height=height,
                fg_color="#CDCDCD",
                border_color="#CDCDCD",
                text_color="#FFFFFF",
                border_width=1,
                corner_radius=360,
                justify="center",
            )
            inputBox.configure(state=ctk.DISABLED)  # Impede de mudar o valor
            inputBox.place(x=x, y=y)
            return inputBox

        inputPesquisa = inputBox(gridQuizMenu, "Pesquisar", 1310.1, 85.6, 305, 65.2)
        inputPesquisa.configure(state=ctk.NORMAL)

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
        fg_color="#5271FF",
        hover=False
        
    )
    buttonRank.place(x=100, y=850)

    Menu.mainloop()


menu()
