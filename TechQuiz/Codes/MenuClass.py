import customtkinter as ctk
from Colors import *
from DataBase import hasDuplicated, setOneData
from Images import (ImageCheckEdit, ImageRnkgLogo, ImageEdit, ImageLogoNEscrita,ImageGoBack)
from Account import *
from checkValidation_Username_Email_Password import check_user_operation
from CtkFunc import createQuizBox
from MainScreen import MainScreen
# from RnkngClass import Ranking

Width = 1920
Height = 1020

class Menu(ctk.CTkFrame):
    def __init__(self, parent, Account):
        Cargo = Account.getCargo()
        parent.config(bg=white)
        parent.title('TechQuiz - Menu')
        
        RankPng = ImageRnkgLogo([203, 166])
        confInfosPng = ImageEdit([54, 54])
        checkInfosPng = ImageCheckEdit()
        imageLogoNPng = ImageLogoNEscrita([300, 280])
        
        # Informações
        gridInfo = ctk.CTkCanvas(
            parent, background="#5271FF", width=400, height=Height, highlightthickness=0
        )
        gridInfo.grid(column=0, row=0, sticky=ctk.W)
        gridInfo.create_rectangle(0, 0, 400, 50, fill=darkBlue, outline=darkBlue)
        gridInfo.create_rectangle(0, 970, 400, 970 + 50, fill=darkBlue, outline=darkBlue)

        ctk.CTkButton(gridInfo,image=imageLogoNPng,fg_color=mainBlue,state='disable',text='').place(x=50,y= 180)


        # Opções
        gridOpcoes = ctk.CTkCanvas(
            parent,
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

        # gridInfo.create_image(205, 320, image=imageLogoPng)

        # Botões
        def GoRanking():
            apagarRegisters(parent)
            MainScreen.setFrame(self,frame=Ranking(parent,Account))

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

        def getPesquisa(event=None):
            if len(QuizSearch.get()) == 4:
                texto = QuizSearch.get()
 
                return texto
            
        def limitar_caracteres(entry, tamanho):
            entry.configure(validate="key", validatecommand=(entry.register(lambda texto: len(texto) <= tamanho), '%P'))

        QuizSearch = ctk.CTkEntry(master=gridOpcoes,placeholder_text="XXXX",placeholder_text_color=white,font=("Roboto", 30, "bold"),
                width=800,height=32,bg_color=white,fg_color=lightGray2,border_color=lightGray2,text_color=white,border_width=1,justify="center", corner_radius=20
            )
        QuizSearch.place(x=90, y=120)
        limitar_caracteres(QuizSearch, 4)
        QuizSearch.bind('<Key>',getPesquisa)
        createQuizBox(gridOpcoes,1000,50,white,None,None,'Teste',0,GoRanking)


class Ranking(ctk.CTkFrame):
    def __init__(self, parent, Account):

        parent.title('Techquiz - Ranking')
        parent.config(bg=mainBlue)

        window = ctk.CTkCanvas(parent, background=white, width=1716, height=816, highlightthickness=0)
        window.place(x=102,y=102)

        createQuizBox(window,145,260,white,'Felipe','FELIPE',None,None,None)
        
        def getPesquisa(event=None):
            if len(QuizSearch.get()) == 4:
                texto = QuizSearch.get()
                return texto
            
        def limitar_caracteres(entry, tamanho):
            entry.configure(validate="key", validatecommand=(entry.register(lambda texto: len(texto) <= tamanho), '%P'))

        QuizSearch = ctk.CTkEntry(master=window,placeholder_text="Busque pelo ID do Jogo",placeholder_text_color=white,font=("Roboto", 30, "bold"),
                width=383.3,height=64.8,bg_color=white,fg_color=lightGray2,border_color=lightGray2,text_color=white,border_width=1,justify="center", corner_radius=20, 
            )
        QuizSearch.place(x=35+70, y=35+100)
        limitar_caracteres(QuizSearch, 4)
        QuizSearch.bind('<Key>', getPesquisa)

        ctk.CTkLabel(parent,text='RANKING',font=("Roboto", 72, "bold")).place(x=1200,y=125.4)

        


        def apagarRegisters(window):
            for item in window.grid_slaves():
                item.grid_forget()

        def GoMenu():
            apagarRegisters(parent)
            MainScreen.setFrame(self,Menu(parent,Account))
            
        buttonGoBack=ctk.CTkButton(parent,text='M\nE\nN\nU',font=("Roboto", 32, "bold"), text_color=black,fg_color=mainBlue,hover_color=white,bg_color=mainBlue,width=50.7,height=Height,corner_radius=0,command=GoMenu)
        buttonGoBack.place(x=0,y=0)
Usuario = Account(4,'11133', 'Felipe','Felpim123-','felipe@gamil.com','CIC', '02',3,0,"1")
MainScreen(Menu,Usuario).mainloop()