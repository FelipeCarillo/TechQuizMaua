import customtkinter as ctk
from Colors import *
from DataBase import hasDuplicated, setOneData
from Images import (ImageCheckEdit, ImageRnkgLogo, ImageEdit, ImageLogoNEscrita, ImageCardQuiz)
from Account import *
from checkValidation_Username_Email_Password import check_user_operation
from CtkFunc import createQuizBox
# from Ranking import Ranking


def InterfaceMenu(Account):

    Cargo = Account.getCargo()
    Width = 1920
    Height = 1020
    Menu = ctk.CTk()
    Menu.title('TechQuiz - Menu')
    Menu.geometry("1920x1020")
    Menu.maxsize(Width, Height)
    Menu.config(bg="white")

    # Imagens dos botões
    RankPng = ImageRnkgLogo([203, 166])
    confInfosPng = ImageEdit([54, 54])
    checkInfosPng = ImageCheckEdit()
    imageLogo = ImageLogoNEscrita([300, 280])
    CardQuiz = ImageCardQuiz([300, 360])

    # Informações
    gridInfo = ctk.CTkCanvas(
        Menu, background="#5271FF", width=400, height=Height, highlightthickness=0
    )
    gridInfo.grid(column=0, row=0, sticky=ctk.W)
    gridInfo.create_rectangle(0, 0, 400, 50, fill=darkBlue, outline=darkBlue)
    gridInfo.create_rectangle(0, 970, 400, 970 + 50, fill=darkBlue, outline=darkBlue)

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
        for item in master.grid_slaves():
            item.grid_forget()


    # Adição das informações

    def inputBox(master, text, width, height, x, y):
        inputBox = ctk.CTkEntry(
            master,
            # placeholder_text=text,
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
        inputBox.insert(0,text)
        inputBox.configure(state=ctk.DISABLED)  # Impede de mudar o valor
        inputBox.place(x=x, y=y)
        return inputBox

    gridInfo.create_image(205, 320, image=imageLogo)
    inputNome = inputBox(gridInfo, Account.getNome(), 324, 85, 38, 500)
    if Cargo == 3:
        inputCurso = inputBox(gridInfo, Account.getCurso(), 324, 85, 38, 620)
        inputAno = inputBox(gridInfo, Account.getAno(), 324, 85, 38, 740)

    def botao_Alterar():
        inputNome.configure(state=ctk.NORMAL)
        inputCurso.configure(state=ctk.NORMAL)
        inputAno.configure(state=ctk.NORMAL)
        buttonEditar.configure(image=checkInfosPng, command=botao_Confirmar)
        

    def botao_Confirmar():
        #Botão de Confirmar
        idUser = Account.getIdUsuario()
        Nome = inputNome.get()
        if Cargo == 3:
            Curso = inputCurso.get()
            Ano = inputAno.get()
        else:
            Curso=1
            Ano = 1
        if Nome != Account.getNome():
            checkName = check_user_operation(Nome)
            continues=hasDuplicated('nomeUser', Nome)
        else:
            checkName=True
            continues=True

        if len(Curso) <= 100 and Ano.isnumeric() and int(Ano)<6 and checkName != False and continues !=False:
            if Nome != Account.getNome():
                Account.setNome(Nome)
                setOneData('usuario','nomeUser',Nome,'idUser',idUser)
            inputNome.configure(state=ctk.DISABLED)
            if Cargo == 3:
                Account.setCurso(Curso)
                setOneData('usuario','cursoUser',Curso,'idUser',idUser)
                Account.setAno(Ano)
                setOneData('usuario','anoUser',Ano,'idUser',idUser)
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
    def GoRanking():
        apagarRegisters(Menu)
        # Ranking(Menu, Account)
        

        

    buttonRank = ctk.CTkButton(
            gridOpcoes,
            image=RankPng,
            text="",
            width=1320,
            height=166,
            fg_color=mainBlue,
            bg_color=white,
            command=GoRanking,
            corner_radius=20,
            hover=False
        )
    buttonRank.place(x=100, y=810)

    createQuizBox(gridOpcoes,100,450,white,'Python',"TechQuiz",'Teste',10, GoRanking)
    createQuizBox(gridOpcoes, 440, 450,white,'Java','TechQuiz','Teste',10, GoRanking)
    createQuizBox(gridOpcoes, 780,450,white,"MySQL","TechQuiz",'Teste',10, GoRanking)
    createQuizBox(gridOpcoes, 1120, 450,white,"MOO",'TechQuiz','Teste',10, GoRanking)

    #Quiz Personalizado

    title = ctk.CTkLabel(gridOpcoes, text="QUIZ PERSONALIZADO", font=(
                "Roboto", 42, "bold"), bg_color=white, text_color=black, fg_color=white)
    title.place(x=85, y=40)
    titleDscrptn = ctk.CTkLabel(gridOpcoes, text="Caso queira jogar um quiz criado pelo seu professor insira o código de acesso a baixo:", font=(
                "Roboto", 18, "bold"), bg_color=white, text_color=black, fg_color=white)
    titleDscrptn.place(x=90, y=87.5)

    def getPesquisa():
        if len(QuizPersonalizadoSearch.get()) == 5:
            texto = QuizPersonalizadoSearch.get()
            return texto
        
    def limitar_caracteres(entry, tamanho):
        entry.configure(validate="key", validatecommand=(entry.register(lambda texto: len(texto) <= tamanho), '%P'))

    QuizPersonalizadoSearch = ctk.CTkEntry(master=gridOpcoes,placeholder_text="XXXX",placeholder_text_color=white,font=("Roboto", 30, "bold"),
            width=800,height=32,bg_color=white,fg_color=lightGray2,border_color=lightGray2,text_color=white,border_width=1,justify="center", corner_radius=20
        )
    QuizPersonalizadoSearch.place(x=90, y=120)
    limitar_caracteres(QuizPersonalizadoSearch, 4)
    QuizPersonalizadoSearch.bind('<Key>',getPesquisa)
    createQuizBox(gridOpcoes,1000,50,white,None,None,'Teste',0,GoRanking)

    Menu.mainloop()

# account = Account(4,'11133', 'Felipe','Felpim123-','felipe@gamil.com','CIC', '02',3,0,"1")
# InterfaceMenu(account)