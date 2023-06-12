import customtkinter as ctk
from Online.Codigo.Colors import *
from Online.Codigo.DataBase import hasDuplicated, setOneData,getInfoQuiz,getQtdQuestoes,getPerAltQuiz, getUserRanking,getRankingTop,getRnkgAll, getAllQuizesProf
from Online.Codigo.Images import (ImageCheckEdit, ImageRnkgLogo, ImageEdit, ImageLogoNEscrita,ImageGoBack,ImageExcel)
from Online.Codigo.Account import *
from Online.Codigo.ChecksInputs import check_user_operation
from Online.Codigo.CtkFunc import createQuizBox, InfoRnkBox, chngQuizBoxData
from Online.Codigo.Quiz import Quiz
from Online.Codigo.QuizScreen import QuizScreen
from Online.Codigo.CreateQuizWindow import CreateQuizScreen

Width = 1920
Height = 1020
class MainScreen(ctk.CTk):
    def __init__(self,Account):
        super().__init__()
        self.geometry("1920x1020")
        self.maxsize(Width, Height)
        self.config(bg="white")
        self.myframe=Menu(self,Account)

    def setFrame(self, frame):
        self.myframe=frame

    def getQuiz(self):
        return self.Quiz
    
    def setQuiz(self,Quiz):
        self.Quiz=Quiz

class Menu(ctk.CTkFrame):
    def __init__(self, parent, Account):
        MainScreen.setQuiz(self=MainScreen,Quiz=None)
        Cargo = Account.getCargo()
        idUser = Account.getIdUsuario()
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

        ctk.CTkButton(gridInfo,image=imageLogoNPng,fg_color=mainBlue,state=ctk.DISABLED,text='').place(x=50,y= 170)

        # Opções
        gridOpcoes = ctk.CTkCanvas(
            parent,
            background=white,
            width=Width - 400,
            height=Height,
            highlightthickness=0,
        )
        gridOpcoes.grid(column=1, row=0, sticky=ctk.E)

        # Adição das informações

        def inputBox(master, textLabel,textEntry, width, height, x, y):
            ctk.CTkLabel(master,text=textLabel,font=("Roboto", 30, "bold"),text_color=white).place(x=x,y=y-40)
            inputBox = ctk.CTkEntry(
                master,
                placeholder_text_color=white,
                font=("Roboto", 22, "bold"),
                width=width,
                height=height,
                fg_color=darkBlue,
                border_color=darkBlue,
                text_color=white,
                border_width=1,
                corner_radius=20,
                justify="center",
            )
            inputBox.insert(0,textEntry)
            inputBox.configure(state=ctk.DISABLED)  # Impede de mudar o valor
            inputBox.place(x=x, y=y)
            return inputBox
        
        inputNome = inputBox(gridInfo,'Username', Account.getNome(), 324, 85, 38, 500)
        if Cargo == 3:
            inputCurso = inputBox(gridInfo,'Curso', Account.getCurso(), 324, 85, 38, 640)
            inputAno = inputBox(gridInfo,'Ano', Account.getAno(), 324, 85, 38, 780)

        def botao_Alterar():
            inputNome.configure(state=ctk.NORMAL)
            inputCurso.configure(state=ctk.NORMAL)
            inputAno.configure(state=ctk.NORMAL)
            buttonEditar.configure(image=checkInfosPng, command=botao_Confirmar)
            

        def botao_Confirmar():
            #Botão de Confirmar
            buttonEditar.configure(state="disable")
            idUser = Account.getIdUsuario()
            Nome = inputNome.get()
            try:
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
            except:
                buttonEditar.configure(state="normal")
                
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

        def apagarRegisters(master):
            for item in master.grid_slaves():
                item.grid_forget()
        # Botões
        def GoRanking():
            try:
                apagarRegisters(parent)
                MainScreen.setFrame(self=MainScreen,frame=Ranking(parent,Account))
            except:
                pass

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

        # Criando os Quizes principais
        quizPython = Quiz(1,'TechQuiz','1 : Python','Lógica de Programação', getPerAltQuiz(1))
        createQuizBox(gridOpcoes,100,450,white, quizPython,10, lambda:playQuiz(quizPython))
        quizJava= Quiz(2,'TechQuiz','2 : Java','Programação Orientada a Objetos', getPerAltQuiz(2))
        createQuizBox(gridOpcoes, 440, 450,white,quizJava,10, lambda:playQuiz(quizJava))
        quizMoo = Quiz(3,'TechQuiz','3 : MOO','Modelagem Orientada a Objetos', getPerAltQuiz(3))
        createQuizBox(gridOpcoes, 780,450,white,quizMoo,10, lambda:playQuiz(quizMoo))
        quizDB = Quiz(4,'TechQuiz','4 : MySQL','Banco de Dados Relacionais', getPerAltQuiz(4))
        createQuizBox(gridOpcoes, 1120, 450,white,quizDB,10, lambda:playQuiz(quizDB))

        #Quiz Personalizado

        texto = ctk.CTkLabel(gridOpcoes, text="QUIZ PERSONALIZADO", font=(
                    "Roboto", 42, "bold"), bg_color=white, text_color=black, fg_color=white)
        texto.place(x=85, y=40)
        titleDscrptn = ctk.CTkLabel(gridOpcoes, text="Caso queira jogar um quiz criado pelo seu professor insira o código de acesso a baixo:", font=(
                    "Roboto", 18, "bold"), bg_color=white, text_color=black, fg_color=white)
        titleDscrptn.place(x=90, y=87.5)

        def limitar_caracteres(entry, tamanho):
            entry.configure(validate="key", validatecommand=(entry.register(lambda texto: len(texto) <= tamanho), '%P'))

        QuizSearch = ctk.CTkEntry(master=gridOpcoes,placeholder_text="XXXX",placeholder_text_color=white,font=("Roboto", 30, "bold"),
                width=800,height=32,bg_color=white,fg_color=lightGray2,border_color=lightGray2,text_color=white,border_width=1,justify="center", corner_radius=20
            )
        QuizSearch.place(x=90, y=120)
        limitar_caracteres(QuizSearch, 4)

        if Cargo == 2:
            ctk.CTkLabel(gridOpcoes,text="Quizes Criados:", font=("Roboto", 30, "bold"), text_color=black).place(x=90,y=225)
            ListaQuizes=getAllQuizesProf(idUser)
            if len(ListaQuizes) == 0:
                ListaQuizes.append('Crie seu primeiro Quiz.')
            QuizComboBox = ctk.CTkComboBox(gridOpcoes,values=ListaQuizes,width=440,height=75,bg_color=white,fg_color=lightGray2,border_color=lightGray2,text_color=white,button_color=mainBlue,border_width=1, corner_radius=20,font=("Roboto", 30, "bold"))
            QuizComboBox.place(x=90, y=275)
            def createQuiz():
                CreateQuizScreen(Account)
            ButtonCreateQuiz = ctk.CTkButton(gridOpcoes,text="Criar",height=75,bg_color=white,fg_color=green,corner_radius=20,font=("Roboto", 30, "bold"),command=createQuiz).place(x=550,y=275)

        def playQuiz(Quiz):
            idJogo=Quiz.get_idJogo()
            df = getPerAltQuiz(idJogo)
            Quiz.set_questoes(df)
            QuizScreen(Account,Quiz)
            
        def getQuizSearch():
            global quizSlcted
            if Cargo == 3:
                idJogo = QuizSearch.get()
            elif Cargo == 2:
                idJogo = QuizComboBox.get().split(" : ")[0]
            if len(idJogo) == 4:
                try:
                    searchButton.configure(state='disable')
                    quizSlcted=Quiz(idJogo,None,None,None,None)
                    dados = getInfoQuiz(idJogo)
                    quizSlcted.set_autor(dados[1])
                    quizSlcted.set_nome(dados[2])
                    varQtdQuestoes = getQtdQuestoes(idJogo)
                    quizSlcted.set_categoria(dados[3])
                    chngQuizBoxData(quizSlcted,varQtdQuestoes,title,autor,categoria,nquestoes,buttonjogar,searchButton)
                except:
                    searchButton.configure(state=ctk.NORMAL)

        searchButton = ctk.CTkButton(gridOpcoes,height=40,corner_radius=20,text='PESQUISAR',fg_color=mainBlue,hover_color='#1D2D74',font=("Roboto", 30, "bold"),command=getQuizSearch)
        searchButton.place(x=680,y=165)
        title, autor,categoria, nquestoes, buttonjogar = createQuizBox(gridOpcoes,1000,50,white,None,0,lambda:playQuiz(quizSlcted))
        buttonjogar.configure(state=ctk.DISABLED)



class Ranking(ctk.CTkFrame):
    def __init__(self, parent, Account):

        cargoUser = Account.getCargo()
        idUser = Account.getIdUsuario()

        parent.title('Techquiz - Ranking')
        parent.config(bg=mainBlue)

        goBackPng = ImageGoBack([110,105])
        excelPng = ImageExcel([100,100])

        window = ctk.CTkCanvas(parent, background=white, width=Width-50, height=Height-50, highlightthickness=0)
        window.place(x=25, y=25)

        #  Construção do RankingBox

        def setRnking(idJogo):
            UserRank = getUserRanking(Account,idJogo)
            Username = UserRank[0]
            UserPgss = UserRank[3]    
            InfoRnkBox(quizBox,10,95,Username,UserPgss,'underline')
            Top10Rank = getRankingTop(idJogo)
            y=162
            for dados in Top10Rank:
                Username = dados[0]
                UserPgss = dados[3]
                InfoRnkBox(quizBox, 10, y,Username,UserPgss)
                y+=56

        def buttonExcel(idJogo, nomeJogo, Autor):
            
            def setExExcelRnkng():
                try:
                    getRnkgAll(Account,idJogo, nomeJogo)
                except:
                    pass
            autor = Account.getNome()
            if autor == Autor: 
                ctk.CTkButton(quizBox, width= 580,text=None,image=excelPng,height=150,corner_radius=20,bg_color=lightGray2,fg_color=mainBlue,hover_color=green,command=setExExcelRnkng).place(x=40,y=250)
        

        ctk.CTkLabel(parent,text='RANKING',font=("Roboto", 82, "bold",'underline'),anchor='w',fg_color=white,bg_color=white,text_color=black).place(x=1140,y=65)
        ctk.CTkButton(parent,700,750,fg_color=lightGray,bg_color=white,corner_radius=20,state='disable').place(x=960,y=180)
        quizBox = ctk.CTkCanvas(parent,background=lightGray2, width=680, height=730, highlightthickness=0)
        quizBox.place(x=970,y=190)
        if cargoUser == 3:
            ctk.CTkLabel(parent,width=660,height=60,text=None,corner_radius=20,bg_color=lightGray2,fg_color=mainBlue).place(x=980,y=200)
            ctk.CTkLabel(parent,text='USERNAME',font=("Roboto", 42, "bold"),bg_color=mainBlue,fg_color=mainBlue).place(x=1000,y=205)
            ctk.CTkLabel(parent,text='PROGRESSO',font=("Roboto", 42, "bold"),bg_color=mainBlue,fg_color=mainBlue).place(x=1380,y=205)

        # Construção da Pesquisa

        def limitar_caracteres(entry, tamanho):
            entry.configure(validate="key", validatecommand=(entry.register(lambda texto: len(texto) <= tamanho), '%P'))
        
        def getQuizChoosed():
            global Jogo
            if cargoUser == 3:
                idJogo = QuizSearch.get()
            elif cargoUser == 2:
                idJogo = QuizComboBox.get().split(" : ")[0]
            if len(idJogo) == 4 or len(idJogo) == 1:
                try:
                    searchButton.configure(state='disable')
                    Jogo=Quiz(idJogo,None,None,None,None)
                    dados = getInfoQuiz(idJogo)
                    Jogo.set_autor(dados[1])
                    Jogo.set_nome(dados[2])
                    varQtdQuestoes = getQtdQuestoes(idJogo)
                    Jogo.set_categoria(dados[3])
                    chngQuizBoxData(Jogo,varQtdQuestoes,title,autor,categoria,nquestoes,None,searchButton)
                    for item in quizBox.place_slaves():
                        item.place_forget()
                    if cargoUser == 3:
                        setRnking(idJogo)
                    elif cargoUser ==2:
                        buttonExcel(idJogo,Jogo.get_nome(),Jogo.get_autor())
                except:
                    searchButton.configure(state='normal')
                searchButton.configure(state='normal')

        if cargoUser == 3:
            QuizSearch = ctk.CTkEntry(master=parent,placeholder_text="Busque pelo ID do Jogo",placeholder_text_color=white,font=("Roboto", 30, "bold"),
                    width=440,height=75,bg_color=white,fg_color=lightGray2,border_color=lightGray2,text_color=white,border_width=1,justify="center", corner_radius=20
                )
            QuizSearch.place(x=200, y=250)
            limitar_caracteres(QuizSearch, 4)

        elif cargoUser == 2:
            ListaQuizes=getAllQuizesProf(idUser)
            QuizComboBox = ctk.CTkComboBox(parent,values=ListaQuizes,width=440,height=75,bg_color=white,fg_color=lightGray2,border_color=lightGray2,text_color=white,button_color=mainBlue,border_width=1, corner_radius=20,font=("Roboto", 30, "bold"))
            QuizComboBox.place(x=200, y=250)

        searchButton = ctk.CTkButton(parent,height=40,corner_radius=20,text='PESQUISAR',fg_color=mainBlue,bg_color=white,hover_color='#1D2D74',font=("Roboto", 30, "bold"),command=getQuizChoosed)
        searchButton.place(x=430,y=330)
        title, autor,categoria, nquestoes, nothing = createQuizBox(parent,260,400,white,None,0,None)

        #  Retorno para o Menu.

        def apagarRegisters(window):
            for item in window.grid_slaves():
                item.grid_forget()

        def GoMenu():
            try:
                apagarRegisters(parent)
                MainScreen.setFrame(self=MainScreen,frame=Menu(parent,Account))
            except:
                pass

        buttonGoBack=ctk.CTkButton(parent,image=goBackPng,anchor='nw',fg_color=white,bg_color=white,hover=None,text=None,corner_radius=0,command=GoMenu)
        buttonGoBack.place(x=25,y=25)