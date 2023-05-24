import customtkinter as ctk
from Colors import *
from DataBase import getPerAltQuiz
from Images import ImageGoBack, ImageGoFoward
from Quiz import Quiz
from random import shuffle
from MainScreen import MainScreen
#from MenuClass import Menu

class QuizScreen(ctk.CTk):
    def __init__(self, Account, Quiz):
        Width = 1920
        Height = 1020
        super().__init__()
        self.geometry("1920x1020") 
        self.maxsize(Width, Height)
        screen = ctk.CTkCanvas(self, background="#FFFFFF", width=Width, height=Height, highlightthickness=0)
        screen.pack()
        screen.create_rectangle(0, 0, Width, 50, fill=darkBlue, outline=darkBlue)
        screen.create_rectangle(0, 970, Width, Height, fill=darkBlue, outline=darkBlue)
        questoes = Quiz.get_questoes()

        global varChange
        varChange = 0
        
        listaQuiz = []
        for item in questoes:
            listaQuiz.append(item)
        shuffle(listaQuiz)
        alt = questoes[listaQuiz[varChange]]
        shuffle(alt)
        alt1 = alt[0][0]
        alt2 = alt[1][0]
        alt3 = alt[2][0]
        alt4 = alt[3][0]
        alt1V = alt[0][1]
        alt2V = alt[1][1]
        alt3V = alt[2][1]
        alt4V = alt[3][1]
        valoresAlternativas = [alt1V,alt2V,alt3V,alt4V]
        print(valoresAlternativas)

        # def apagarRegisters(window):
        #     for item in window.grid_slaves():
        #         item.grid_forget()
        
        # def GoMenu():
        #     apagarRegisters(parent)
        #     MainScreen.setFrame(self=MainScreen,frame=Menu(parent,Account))

        buttonBack = ctk.CTkButton(
            screen,
            text='SAIR',
            command=None,
            bg_color=white,
            fg_color=red,
            hover_color=red
        )
        buttonBack.place(x=30, y=100)

        buttonFinalizar = ctk.CTkButton(
            screen,
            text='FINALIZAR',
            command=None,
            bg_color=white,
            fg_color=gray,
            hover_color=gray
        )
        buttonFinalizar.place(x=1750, y=100)

        def callQuest():
            None

        numQuest = len(listaQuiz)
        posiQuest = 200
        i = 0
        listaBotoes = []
        while i < numQuest:
            placeNumQuest = ctk.CTkButton(screen,text=i+1,font=("Roboto", 10, "bold"),width=38,height=24,fg_color=lightGray,border_color="#8F8F8F", hover_color=mainBlue,
                         border_width=5, text_color=black,corner_radius=10, command=callQuest)
            if i <=35:
                placeNumQuest.place(x=posiQuest,y=900)
                posiQuest += 42
            elif i == 36:
                posiQuest = 200
                placeNumQuest.place(x=posiQuest,y=937)
                posiQuest += 42
            else:
                placeNumQuest.place(x=posiQuest,y=937)
                posiQuest += 42
            i += 1
            listaBotoes.append(placeNumQuest)

        screen.create_rectangle(200, 100,1720,400,fill=mainBlue,outline=mainBlue)
        pergunta = ctk.CTkLabel(screen,justify='left',text=listaQuiz[varChange]
                     ,font=("Roboto", 30, "bold"),text_color=white,fg_color=mainBlue,bg_color=mainBlue,wraplength=1720-250)
        if len(listaQuiz[varChange]) < 81:
            pergunta.place(x=225,y=230)
        elif len(listaQuiz[varChange]) < 161:
            pergunta.place(x=225,y=230)
        elif len(listaQuiz[varChange]) < 241:
            pergunta.place(x=225,y=230)
        elif len(listaQuiz[varChange]) < 321:
            pergunta.place(x=225,y=230)
        elif len(listaQuiz[varChange]) < 401:
            pergunta.place(x=225,y=230)
        elif len(listaQuiz[varChange]) < 481:
            pergunta.place(x=225,y=230)
        elif len(listaQuiz[varChange]) < 561:
            pergunta.place(x=225,y=230)
        elif len(listaQuiz[varChange]) < 641:
            pergunta.place(x=225,y=105)

        def formata_texto(var):
            aux = var.split(" ")
            linha = ""
            frase = ""
            for palavra in aux:
                if len(linha + palavra + " ") >= 30:
                    linha += '\n'
                    frase += linha
                    linha = ""
                linha += palavra + " "
            frase += linha
            return frase
        
        def frases():
            global frase1, frase2, frase3, frase4
            frase1 = formata_texto(alt1)
            frase2 = formata_texto(alt2)
            frase3 = formata_texto(alt3)
            frase4 = formata_texto(alt4)
        frases()

        global alter1, alter2, alter3, alter4
        def botao1_precionado():
            global alter1
            if alter1 == False:
                opcao1.configure(fg_color=mainBlue)
                alter1 = True
            else:
                opcao1.configure(fg_color=lightGray)
                alter1 = False
        def botao2_precionado():
            global alter2
            if alter2 == False:
                opcao2.configure(fg_color=mainBlue)
                alter2 = True
            else:
                opcao2.configure(fg_color=lightGray)
                alter2 = False
        def botao3_precionado():
            global alter3
            if alter3 == False:
                opcao3.configure(fg_color=mainBlue)
                alter3 = True
            else:
                opcao3.configure(fg_color=lightGray)
                alter3 = False
        def botao4_precionado():
            global alter4
            if alter4 == False:
                opcao4.configure(fg_color=mainBlue)
                alter4 = True
            else:
                opcao4.configure(fg_color=lightGray)
                alter4 = False

        opcao1 = ctk.CTkButton(screen,width=600,height=200,fg_color=lightGray,hover_color=mainBlue,text=frase1,font=("Roboto", 34, "bold"),text_color=black,corner_radius=45,border_color="#8F8F8F",border_width=4, command=botao1_precionado)
        opcao1.place(x=200,y=450)
        opcao2 = ctk.CTkButton(screen,width=600,height=200,fg_color=lightGray,hover_color=mainBlue,text=frase2,font=("Roboto", 34, "bold"),text_color=black,corner_radius=45,border_color="#8F8F8F",border_width=4, command=botao2_precionado)
        opcao2.place(x=200,y=670)
        opcao3 = ctk.CTkButton(screen,width=600,height=200,fg_color=lightGray,hover_color=mainBlue,text=frase3,font=("Roboto", 34, "bold"),text_color=black,corner_radius=45,border_color="#8F8F8F",border_width=4, command=botao3_precionado)
        opcao3.place(x=1120,y=450)
        opcao4 = ctk.CTkButton(screen,width=600,height=200,fg_color=lightGray,hover_color=mainBlue,text=frase4,font=("Roboto", 34, "bold"),text_color=black,corner_radius=45,border_color="#8F8F8F",border_width=4, command=botao4_precionado)
        opcao4.place(x=1120,y=670)

        def restoreButtonState():
            global alter1, alter2, alter3, alter4
            alter1 = salvaBotoesList[varChange][0]
            alter2 = salvaBotoesList[varChange][1]
            alter3 = salvaBotoesList[varChange][2]
            alter4 = salvaBotoesList[varChange][3]
            botao1_precionado()
            botao2_precionado()
            botao3_precionado()
            botao4_precionado()
            botao1_precionado()
            botao2_precionado()
            botao3_precionado()
            botao4_precionado()
        
        def resetBottonState():
            global alter1, alter2, alter3, alter4
            alter1 = True
            alter2 = True
            alter3 = True
            alter4 = True
            botao1_precionado()
            botao2_precionado()
            botao3_precionado()
            botao4_precionado()
        resetBottonState()

        salvaBotoesList = []
        salvaBotoesVar = 0
        while salvaBotoesVar < numQuest:
            salvaBotoesList.append([False,False,False,False])
            salvaBotoesVar +=1

        def saveBottonState():
            salvaBotoesList[varChange]=[alter1, alter2, alter3, alter4]
            # print(varChange)
            # print(salvaBotoesList)

        def showNumberQuestion():
            for botoes in listaBotoes:
                botoes.configure(border_color="#8F8F8F")
            questaoAtual = listaBotoes[varChange]
            questaoAtual.configure(border_color=mainBlue)


        def mudaPagB():
            global varChange
            if varChange > 0:
                saveBottonState()
                varChange = varChange-1
                pergunta.configure(text=listaQuiz[varChange])
                #botoes
                global alt1, alt2, alt3, alt4
                alt = questoes[listaQuiz[varChange]]
                alt1 = alt[0][0]
                alt2 = alt[1][0]
                alt3 = alt[2][0]
                alt4 = alt[3][0]
                global frase1, frase2, frase3, frase4
                frase1 = formata_texto(alt1)
                frase2 = formata_texto(alt2)
                frase3 = formata_texto(alt3)
                frase4 = formata_texto(alt4)
                opcao1.configure(text=frase1)
                opcao2.configure(text=frase2)
                opcao3.configure(text=frase3)
                opcao4.configure(text=frase4)
                restoreButtonState()
                showNumberQuestion()
                
        def mudaPagF():
            global varChange
            if varChange < numQuest-1:
                saveBottonState()
                varChange = varChange+1
                pergunta.configure(text=listaQuiz[varChange])
                #botoes
                global alt1, alt2, alt3, alt4
                alt = questoes[listaQuiz[varChange]]
                alt1 = alt[0][0]
                alt2 = alt[1][0]
                alt3 = alt[2][0]
                alt4 = alt[3][0]
                global frase1, frase2, frase3, frase4
                frase1 = formata_texto(alt1)
                frase2 = formata_texto(alt2)
                frase3 = formata_texto(alt3)
                frase4 = formata_texto(alt4)
                opcao1.configure(text=frase1)
                opcao2.configure(text=frase2)
                opcao3.configure(text=frase3)
                opcao4.configure(text=frase4)
                restoreButtonState()
                showNumberQuestion()

        Seta = ImageGoBack([70, 70])
        Seta2 = ImageGoFoward([70, 70])
        ctk.CTkButton(screen,image=Seta,text=None,fg_color=white,hover=None, command=mudaPagB).place(x=60,y=890)
        ctk.CTkButton(screen,image=Seta2,text=None,fg_color=white,hover=None, command=mudaPagF).place(x=1720,y=890)

        questaoAtual = listaBotoes[varChange]
        questaoAtual.configure(border_color=mainBlue)


df = getPerAltQuiz(1)

quiz = Quiz(1,'TechQuiz','Python','Lógica de Programação',df)

QuizScreen(1,quiz).mainloop()