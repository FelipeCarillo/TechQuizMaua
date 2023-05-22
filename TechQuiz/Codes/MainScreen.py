import customtkinter as ctk
from Colors import *
from DataBase import hasDuplicated, setOneData,getInfoQuiz,getQtdQuestoes,getPerAltQuiz, getUserRanking,getRankingTop,getRnkgAll 
from Images import (ImageCheckEdit, ImageRnkgLogo, ImageEdit, ImageLogoNEscrita,ImageGoBack,ImageExcel)
from Account import *
from checkValidation_Username_Email_Password import check_user_operation
from CtkFunc import createQuizBox, InfoRnkBox, chngQuizBoxData
from Quiz import Quiz

Width = 1920
Height = 1020
class MainScreen(ctk.CTkToplevel):
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

        ctk.CTkButton(gridInfo,image=ImageLogoNEscrita([300, 280]),fg_color=mainBlue,state='disable',text='').place(x=50,y= 180)

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
                buttonEditar.configure(state="enable")
                
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
            apagarRegisters(parent)
            MainScreen.setFrame(self=MainScreen,frame=Ranking(parent,Account))

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
        quizPython = Quiz(1,'TechQuiz','Python','Lógica de Programação', getPerAltQuiz(1))
        createQuizBox(gridOpcoes,100,450,white, quizPython,10, GoRanking)
        quizJava= Quiz(2,'TechQuiz','Java','POO', getPerAltQuiz(2))
        createQuizBox(gridOpcoes, 440, 450,white,quizJava,10, GoRanking)
        quizMoo = Quiz(3,'TechQuiz','Modelagem','MOO', getPerAltQuiz(3))
        createQuizBox(gridOpcoes, 780,450,white,quizMoo,10, GoRanking)
        quizDB = Quiz(4,'TechQuiz','DataBase','Banco de Dados', getPerAltQuiz(4))
        createQuizBox(gridOpcoes, 1120, 450,white,quizDB,10, GoRanking)

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

        def playQuiz():
            idJogo=slctQuiz.get_idJogo()
            df = getPerAltQuiz(idJogo)
            slctQuiz.set_questoes(df)
            MainScreen.setQuiz(self=MainScreen,Quiz=slctQuiz)
            parent.destroy()
            
        def getQuizSearch():
            global slctQuiz
            idJogo = QuizSearch.get()
            if len(idJogo) == 4:
                try:
                    searchButton.configure(state='disabled')
                    slctQuiz=Quiz(idJogo,None,None,None,None)
                    dados = getInfoQuiz(idJogo)
                    slctQuiz.set_autor(dados[1])
                    slctQuiz.set_nome(dados[2])
                    varQtdQuestoes = getQtdQuestoes(idJogo)
                    slctQuiz.set_categoria(dados[3])
                    chngQuizBoxData(slctQuiz,varQtdQuestoes,title,autor,categoria,nquestoes,buttonjogar,searchButton)
                except:
                    searchButton.configure(state='enable')

        searchButton = ctk.CTkButton(gridOpcoes,height=40,corner_radius=20,text='PESQUISAR',fg_color=mainBlue,hover_color='#1D2D74',font=("Roboto", 30, "bold"),command=getQuizSearch)
        searchButton.place(x=680,y=165)
        title, autor,categoria, nquestoes, buttonjogar = createQuizBox(gridOpcoes,1000,50,white,None,0,playQuiz)
        buttonjogar.configure(state='disabled')



class Ranking(ctk.CTkFrame):
    def __init__(self, parent, Account):

        cargoUser = Account.getCargo()

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
                getRnkgAll(Account,idJogo, nomeJogo)
            autor = Account.getNome()
            if autor == Autor: 
                ctk.CTkButton(quizBox, width= 580,text=None,image=excelPng,height=150,corner_radius=20,bg_color=green,fg_color=green,command=setExExcelRnkng).place(x=40,y=250)
        


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
        
        def getQuizSearch():
            global slctQuiz
            idJogo = QuizSearch.get()
            if len(idJogo) == 4 or len(idJogo) == 1:
                try:
                    searchButton.configure(state='disabled')
                    slctQuiz=Quiz(idJogo,None,None,None,None)
                    dados = getInfoQuiz(idJogo)
                    slctQuiz.set_autor(dados[1])
                    slctQuiz.set_nome(dados[2])
                    varQtdQuestoes = getQtdQuestoes(idJogo)
                    slctQuiz.set_categoria(dados[3])
                    chngQuizBoxData(slctQuiz,varQtdQuestoes,title,autor,categoria,nquestoes,None,searchButton)
                    for item in quizBox.place_slaves():
                        item.place_forget()
                    if cargoUser == 3:
                        setRnking(idJogo)
                    elif cargoUser ==2:
                        buttonExcel(idJogo,slctQuiz.get_nome(),slctQuiz.get_autor())
                except:
                    searchButton.configure(state='enable')
                searchButton.configure(state='enable')

        QuizSearch = ctk.CTkEntry(master=parent,placeholder_text="Busque pelo ID do Jogo",placeholder_text_color=white,font=("Roboto", 30, "bold"),
                width=440,height=75,bg_color=white,fg_color=lightGray2,border_color=lightGray2,text_color=white,border_width=1,justify="center", corner_radius=20
            )
        QuizSearch.place(x=200, y=250)
        limitar_caracteres(QuizSearch, 4)

        searchButton = ctk.CTkButton(parent,height=40,corner_radius=20,text='PESQUISAR',fg_color=mainBlue,bg_color=white,hover_color='#1D2D74',font=("Roboto", 30, "bold"),command=getQuizSearch)
        searchButton.place(x=430,y=330)
        title, autor,categoria, nquestoes, nothing = createQuizBox(parent,260,400,white,None,0,None)

        #  Retorno para o Menu.

        def apagarRegisters(window):
            for item in window.grid_slaves():
                item.grid_forget()

        def GoMenu():
            apagarRegisters(parent)
            MainScreen.setFrame(self=MainScreen,frame=Menu(parent,Account))
            
        buttonGoBack=ctk.CTkButton(parent,image=goBackPng,anchor='nw',fg_color=white,bg_color=white,hover=None,text=None,corner_radius=0,command=GoMenu)
        buttonGoBack.place(x=25,y=25)

# Usuario = Account(11,'11133', 'TechQuiz','Felpim123-','felipe@gamil.com','CIC', '02',2,0,"1")
# MainScreen(Usuario).mainloop()