import customtkinter as ctk
from Local.Codigo.Colors import *
from Local.Codigo.Images import ImageGoBack, ImageGoFoward, ImageEdit, ImageCheckEdit
from Local.Codigo.DataBase import createQuiz

class CreateQuizScreen(ctk.CTkToplevel):
    def __init__(self, Account):
        Width = 1920
        Height = 1020
        super().__init__()
        self.geometry("1920x1020") 
        self.maxsize(Width, Height)
        screen = ctk.CTkCanvas(self, background="#FFFFFF", width=Width, height=Height, highlightthickness=0)
        screen.pack()
        screen.create_rectangle(0, 0, Width, 50, fill=darkBlue, outline=darkBlue)
        screen.create_rectangle(0, 970, Width, Height, fill=darkBlue, outline=darkBlue)

        # Variavel das paginas/numeração
        global varChange
        varChange = 0
        #-------------------------------
        #lista de relações-------------
        listaDeQuestoes = []
        listaDeAlternativas = []
        listaGabarito = []

        i = 0
        while i < 72:
            listaDeQuestoes.append("")
            listaDeAlternativas.append(["As respostas somente podem conter 100 caracteres.","As respostas somente podem conter 100 caracteres.","As respostas somente podem conter 100 caracteres.","As respostas somente podem conter 100 caracteres."])
            listaGabarito.append([False,False,False,False])
            i += 1
        #------------------------------
        #Imagens----------------------------
        confInfosPngP = ImageEdit([35, 35])
        checkInfosPngP = ImageCheckEdit([35, 35])
        confInfosPngA = ImageEdit([28, 28])
        checkInfosPngA = ImageCheckEdit([28, 28])
        #-----------------------------------
        #Criação e configuração da pergunta--------------------------------------------------------------------------------------------------------------------
        screen.create_rectangle(200,100,1720,400,fill=mainBlue,outline=mainBlue)
        perguntaLabel = ctk.CTkLabel(screen,justify='left',text="",
                                font=("Roboto", 30, "bold"),text_color=white,fg_color=mainBlue,bg_color=mainBlue,wraplength=1720-250)
        perguntaLabel.place(x=225,y=105)
        screen.create_rectangle(200,56,250,99,fill=gray,outline=gray)
        perguntaEntry = ctk.CTkEntry(screen,placeholder_text="As questões somente podem conter um limite de 600 caracteres.", placeholder_text_color=black,
                                font=("Roboto", 30, "bold"), text_color=black, fg_color=lightGray, corner_radius=0, border_color=gray, width=1471, height=31)
        perguntaEntry.configure(state=ctk.DISABLED)
        perguntaEntry.place(x=250,y=56)
        
        def botao_Alterar_Pergunta():
            perguntaEntry.configure(state=ctk.NORMAL)
            buttonEditarPergunta.configure(image=checkInfosPngP, command=botao_Confirmar_Pergunta)

        def botao_Confirmar_Pergunta():
            pergunta = perguntaEntry.get()
            if len(pergunta) < 601:
                perguntaEntry.delete(0, 600)
                perguntaEntry.configure(state=ctk.DISABLED)
                perguntaLabel.configure(text=pergunta)
                buttonEditarPergunta.configure(image=confInfosPngP, command=botao_Alterar_Pergunta)
                listaDeQuestoes[varChange] = pergunta #adiciona a pergunta lista de perguntas
            else:
                perguntaLabel.configure(text="Seu texto é grande demais, por favor reformule a sua pergunta para que ela caiba no espaço de 600 caracteres, para seu conhecimento, o texo atual possui " + str(len(pergunta)) + " caracteres.")

        buttonEditarPergunta = ctk.CTkButton(master=screen,image=confInfosPngP,width=35,height=35,command=botao_Alterar_Pergunta,fg_color=gray,bg_color=gray,hover_color=gray,text="",)
        buttonEditarPergunta.place(x=200, y=56)
        #------------------------------------------------------------------------------------------------------------------------------------------------------
        #Criação e configuração dos botões/alternativas----------------------------------------------------------------------------------------------
        #Alternativa 1
        screen.create_rectangle(200,450,800,650,fill="#8F8F8F",outline="#8F8F8F")
        alternativa1Label = ctk.CTkLabel(screen,width=590,height=190,fg_color=lightGray,text="As respostas somente podem conter 100 caracteres.",font=("Roboto", 34, "bold"),text_color=black,corner_radius=0,wraplength=590)
        alternativa1Label.place(x=205,y=455)
        alternativa1Entry = ctk.CTkEntry(screen,placeholder_text="", placeholder_text_color=black,
                                font=("Roboto", 25, "bold"), text_color=black, fg_color=lightGray, corner_radius=0, border_color=gray, width=527, height=26)
        alternativa1Entry.configure(state=ctk.DISABLED)
        alternativa1Entry.place(x=240,y=413)
        #25 caracteres por linha 4 linhas

        def botao_Alterar_Alternativa1():
            alternativa1Entry.configure(state=ctk.NORMAL)
            buttonEditarAlternativa1.configure(image=checkInfosPngA, command=botao_Confirmar_Alternativa1)

        def botao_Confirmar_Alternativa1():
            alternativa1 = alternativa1Entry.get()
            if len(alternativa1) < 101:
                alternativa1Entry.delete(0, 600)
                alternativa1Entry.configure(state=ctk.DISABLED)
                listaDeAlternativas[varChange][0] = alternativa1 #adiciona a alternativa na lista na posição 0
                alternativa1Label.configure(text=alternativa1)
                buttonEditarAlternativa1.configure(image=confInfosPngA, command=botao_Alterar_Alternativa1)
            else:
                perguntaLabel.configure(text="Seu texto é grande demais, por favor reformule a sua\nresposta para que ela caiba no espaço de 100 caracteres.")

        buttonEditarAlternativa1 = ctk.CTkButton(master=screen,image=confInfosPngA,width=28,height=28,command=botao_Alterar_Alternativa1,fg_color=gray,bg_color=gray,hover_color=gray,text="",)
        buttonEditarAlternativa1.place(x=200, y=413)

        def valorAlternativa1(onlyshow=False):
            if onlyshow == False:
                listaGabarito[varChange][0] = not listaGabarito[varChange][0] 
            if listaGabarito[varChange][0] == False:
                buttonEditarValorAlternativa1.configure(fg_color=red,hover_color=red)
            else:
                buttonEditarValorAlternativa1.configure(fg_color=green,hover_color=green)

        buttonEditarValorAlternativa1 = ctk.CTkButton(master=screen,width=36,height=36,command=valorAlternativa1,fg_color=red,bg_color=lightGray,hover_color=red,text="",border_width=3, corner_radius=0, border_color=gray)
        buttonEditarValorAlternativa1.place(x=765,y=413)
        #-------------
        #Alternativa 2
        screen.create_rectangle(200,700,800,900,fill="#8F8F8F",outline="#8F8F8F")
        alternativa2Label = ctk.CTkLabel(screen,width=590,height=190,fg_color=lightGray,text="As respostas somente podem conter 100 caracteres.",font=("Roboto", 34, "bold"),text_color=black,corner_radius=0,wraplength=590)
        alternativa2Label.place(x=205,y=705)
        alternativa2Entry = ctk.CTkEntry(screen,placeholder_text="", placeholder_text_color=black,
                                font=("Roboto", 25, "bold"), text_color=black, fg_color=lightGray, corner_radius=0, border_color=gray, width=527, height=26)
        alternativa2Entry.configure(state=ctk.DISABLED)
        alternativa2Entry.place(x=240,y=663)
        #25 caracteres por linha 4 linhas

        def botao_Alterar_Alternativa2():
            alternativa2Entry.configure(state=ctk.NORMAL)
            buttonEditarAlternativa2.configure(image=checkInfosPngA, command=botao_Confirmar_Alternativa2)

        def botao_Confirmar_Alternativa2():
            alternativa2 = alternativa2Entry.get()
            if len(alternativa2) < 101:
                alternativa2Entry.delete(0, 600)
                alternativa2Entry.configure(state=ctk.DISABLED)
                listaDeAlternativas[varChange][1] = alternativa2 #adiciona a alternativa na lista na posição 1
                alternativa2Label.configure(text=alternativa2)
                buttonEditarAlternativa2.configure(image=confInfosPngA, command=botao_Alterar_Alternativa2)
            else:
                perguntaLabel.configure(text="Seu texto é grande demais, por favor reformule a sua resposta para que ela caiba no espaço de 100 caracteres.")

        buttonEditarAlternativa2 = ctk.CTkButton(master=screen,image=confInfosPngA,width=28,height=28,command=botao_Alterar_Alternativa2,fg_color=gray,bg_color=gray,hover_color=gray,text="",)
        buttonEditarAlternativa2.place(x=200, y=663)

        def valorAlternativa2(onlyshow=False):
            if onlyshow == False:
                listaGabarito[varChange][1] = not listaGabarito[varChange][1] 
            if listaGabarito[varChange][1] == False:
                buttonEditarValorAlternativa2.configure(fg_color=red,hover_color=red)
            else:
                buttonEditarValorAlternativa2.configure(fg_color=green,hover_color=green)

        buttonEditarValorAlternativa2 = ctk.CTkButton(master=screen,width=36,height=36,command=valorAlternativa2,fg_color=red,bg_color=lightGray,hover_color=red,text="",border_width=3, corner_radius=0, border_color=gray)
        buttonEditarValorAlternativa2.place(x=765,y=663)
        #-------------
        #Alternativa 3
        screen.create_rectangle(1120,450,1720,650,fill="#8F8F8F",outline="#8F8F8F")
        alternativa3Label = ctk.CTkLabel(screen,width=590,height=190,fg_color=lightGray,text="As respostas somente podem conter 100 caracteres.",font=("Roboto", 34, "bold"),text_color=black,corner_radius=0,wraplength=590)
        alternativa3Label.place(x=1125,y=455)
        alternativa3Entry = ctk.CTkEntry(screen,placeholder_text="", placeholder_text_color=black,
                                font=("Roboto", 25, "bold"), text_color=black, fg_color=lightGray, corner_radius=0, border_color=gray, width=527, height=26)
        alternativa3Entry.configure(state=ctk.DISABLED)
        alternativa3Entry.place(x=1160,y=413)
        #25 caracteres por linha 4 linhas

        def botao_Alterar_Alternativa3():
            alternativa3Entry.configure(state=ctk.NORMAL)
            buttonEditarAlternativa3.configure(image=checkInfosPngA, command=botao_Confirmar_Alternativa3)

        def botao_Confirmar_Alternativa3():
            alternativa3 = alternativa3Entry.get()
            if len(alternativa3) < 101:
                alternativa3Entry.delete(0, 600)
                alternativa3Entry.configure(state=ctk.DISABLED)
                listaDeAlternativas[varChange][2] = alternativa3 #adiciona a alternativa na lista na posição 2
                alternativa3Label.configure(text=alternativa3)
                buttonEditarAlternativa3.configure(image=confInfosPngA, command=botao_Alterar_Alternativa3)
            else:
                perguntaLabel.configure(text="Seu texto é grande demais, por favor reformule a sua\nresposta para que ela caiba no espaço de 100 caracteres.")

        buttonEditarAlternativa3 = ctk.CTkButton(master=screen,image=confInfosPngA,width=28,height=28,command=botao_Alterar_Alternativa3,fg_color=gray,bg_color=gray,hover_color=gray,text="",)
        buttonEditarAlternativa3.place(x=1120, y=413)

        def valorAlternativa3(onlyshow=False):
            if onlyshow == False:
                listaGabarito[varChange][2] = not listaGabarito[varChange][2] 
            if listaGabarito[varChange][2] == False:
                buttonEditarValorAlternativa3.configure(fg_color=red,hover_color=red)
            else:
                buttonEditarValorAlternativa3.configure(fg_color=green,hover_color=green)

        buttonEditarValorAlternativa3 = ctk.CTkButton(master=screen,width=36,height=36,command=valorAlternativa3,fg_color=red,bg_color=lightGray,hover_color=red,text="",border_width=3, corner_radius=0, border_color=gray)
        buttonEditarValorAlternativa3.place(x=1685,y=413)
        #-------------
        #Alternativa 4
        screen.create_rectangle(1120,700,1720,900,fill="#8F8F8F",outline="#8F8F8F")
        alternativa4Label = ctk.CTkLabel(screen,width=590,height=190,fg_color=lightGray,text="As respostas somente podem conter 100 caracteres.",font=("Roboto", 34, "bold"),text_color=black,corner_radius=0,wraplength=590)
        alternativa4Label.place(x=1125,y=705)
        alternativa4Entry = ctk.CTkEntry(screen,placeholder_text="", placeholder_text_color=black,
                                font=("Roboto", 25, "bold"), text_color=black, fg_color=lightGray, corner_radius=0, border_color=gray, width=527, height=26)
        alternativa4Entry.configure(state=ctk.DISABLED)
        alternativa4Entry.place(x=1160,y=663)
        #25 caracteres por linha 4 linhas

        def botao_Alterar_Alternativa4():
            alternativa4Entry.configure(state=ctk.NORMAL)
            buttonEditarAlternativa4.configure(image=checkInfosPngA, command=botao_Confirmar_Alternativa4)

        def botao_Confirmar_Alternativa4():
            alternativa4 = alternativa4Entry.get()
            if len(alternativa4) < 101:
                alternativa4Entry.delete(0, 600)
                alternativa4Entry.configure(state=ctk.DISABLED)
                listaDeAlternativas[varChange][3] = alternativa4 #adiciona a alternativa na lista na posição 3
                alternativa4Label.configure(text=alternativa4)
                buttonEditarAlternativa4.configure(image=confInfosPngA, command=botao_Alterar_Alternativa4)
            else:
                perguntaLabel.configure(text="Seu texto é grande demais, por favor reformule a sua\nresposta para que ela caiba no espaço de 100 caracteres.")

        buttonEditarAlternativa4 = ctk.CTkButton(master=screen,image=confInfosPngA,width=28,height=28,command=botao_Alterar_Alternativa4,fg_color=gray,bg_color=gray,hover_color=gray,text="",)
        buttonEditarAlternativa4.place(x=1120, y=663)

        def valorAlternativa4(onlyshow=False):
            if onlyshow == False:
                listaGabarito[varChange][3] = not listaGabarito[varChange][3] 
            if listaGabarito[varChange][3] == False:
                buttonEditarValorAlternativa4.configure(fg_color=red,hover_color=red)
            else:
                buttonEditarValorAlternativa4.configure(fg_color=green,hover_color=green)

        buttonEditarValorAlternativa4 = ctk.CTkButton(master=screen,width=36,height=36,command=valorAlternativa4,fg_color=red,bg_color=lightGray,hover_color=red,text="",border_width=3, corner_radius=0, border_color=gray)
        buttonEditarValorAlternativa4.place(x=1685,y=663)
        #--------------------------------------------------------------------------------------------------------------------------------------------
        #Criando showQuestionButton-----------------------
        posiQuest = 200
        i = 0
        listaBotoes = []
        while i < 72:
            placeNumQuest = ctk.CTkButton(screen,text=i+1,font=("Roboto", 10, "bold"),width=38,height=24,fg_color=lightGray,border_color="#8F8F8F", hover_color=mainBlue,
                         border_width=5, text_color=black,corner_radius=10)
            if i <=35:
                placeNumQuest.place(x=posiQuest,y=905)
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
        #-------------------------------------------------------------------
        #Passagem de paginas-----------------------------------------------------------------------
        def verificaResposta(BorF):
            if BorF == "foward":
                questaoAtual = listaBotoes[varChange]
                questaoAtual.configure(fg_color=lightGray)
                global liberaPag
                liberaPag = 0
                validaAlternativa = 0
                if listaDeQuestoes[varChange] != "":
                    for resposta in listaDeAlternativas[varChange]:
                        if resposta != "" and resposta != "As respostas somente podem conter 100 caracteres.":
                            validaAlternativa += 1
                    if validaAlternativa == 4:
                        for resposta in listaGabarito[varChange]:
                            if resposta == True:
                                liberaPag = 1
                                questaoAtual.configure(fg_color=green)
                    else:
                        AvisoFaltaAlternativa()
                else:
                    AvisoFaltaPergunta()
                return liberaPag
            else:
                questaoAtual = listaBotoes[varChange]
                questaoAtual.configure(fg_color=lightGray)
                validaAlternativa = 0
                if listaDeQuestoes[varChange] != "":
                    for resposta in listaDeAlternativas[varChange]:
                        if resposta != "" and resposta != "As respostas somente podem conter 100 caracteres.":
                            validaAlternativa += 1
                    if validaAlternativa == 4:
                        for resposta in listaGabarito[varChange]:
                            if resposta == True:
                                questaoAtual.configure(fg_color=green)
        
        def restoreButtonState():
            alternativa1Label.configure(text=listaDeAlternativas[varChange][0])
            alternativa2Label.configure(text=listaDeAlternativas[varChange][1])
            alternativa3Label.configure(text=listaDeAlternativas[varChange][2])
            alternativa4Label.configure(text=listaDeAlternativas[varChange][3])
            valorAlternativa1(True)
            valorAlternativa2(True)
            valorAlternativa3(True)
            valorAlternativa4(True)
        
        def showNumberQuestion():
            for botoes in listaBotoes:
                botoes.configure(border_color="#8F8F8F")
            questaoAtual = listaBotoes[varChange]
            questaoAtual.configure(border_color=mainBlue)
        showNumberQuestion()

        def mudaPagB():
            global varChange
            if varChange > 0:
                verificaResposta("back")
                varChange = varChange-1
                perguntaLabel.configure(text=listaDeQuestoes[varChange])
                #botoes
                restoreButtonState()
                showNumberQuestion()
                
        def mudaPagF():
            global varChange
            if varChange < 72:
                verificaResposta("foward")
                global liberaPag
                if liberaPag ==1:
                    varChange = varChange+1
                    perguntaLabel.configure(text=listaDeQuestoes[varChange])
                    #botoes
                    restoreButtonState()
                    showNumberQuestion()
                else:
                    AvisoRespostasProf()

        Seta = ImageGoBack([70, 70])
        Seta2 = ImageGoFoward([70, 70])
        ctk.CTkButton(screen,image=Seta,text=None,fg_color=white,hover=None, command=mudaPagB).place(x=60,y=890)
        ctk.CTkButton(screen,image=Seta2,text=None,fg_color=white,hover=None, command=mudaPagF).place(x=1722,y=890)
        #------------------------------------------------------------------------------------------
        #botão de sair-----------------
        global varSaida
        varSaida = 0
        def sair():
            global varSaida
            if varSaida == 0:
                varSaida = 1
                AvisoSaida()
            elif varSaida == 1:
                self.destroy()
        
        buttonBack = ctk.CTkButton(
            screen,
            text='SAIR',
            command=sair,
            bg_color=white,
            fg_color=red,
            hover_color=red
        )
        buttonBack.place(x=30, y=100)
        #------------------------------
        #botão finalizar
        def clear_frame():
            for widgets in screen.winfo_children():
                widgets.destroy()
        
        global validar
        validar = 0
        def finalizar():
        
            verificaResposta("foward")
            if liberaPag == 1:
                numQuest = 0
                for questao in listaDeQuestoes:
                    if questao != "":
                        numQuest += 1
                if numQuest >= 2:
                    global validar
                    if validar == 0:
                        validar = 1
                        ConfirmacaoProf()
                    elif validar == 1:
                        del listaDeQuestoes[numQuest:]
                        del listaDeAlternativas[numQuest:]
                        del listaGabarito[numQuest:]

                        clear_frame()
                        screen.create_rectangle(0, 0, 50, Height, fill=darkBlue, outline=darkBlue)
                        screen.create_rectangle(1870, 0, Width, Height, fill=darkBlue, outline=darkBlue)
                        screen.create_rectangle(200, 100,1720,400,fill=white,outline=white)

                        screen.create_rectangle(200,100,1720,400,fill=white,outline=white)
                        screen.create_rectangle(200,56,250,99,fill=white,outline=white)
                        screen.create_rectangle(200,450,1720,900,fill=white,outline=white)

                        nomeDoQuiz = ctk.CTkEntry(screen,placeholder_text_color=white,placeholder_text="Nome do Quiz / 100 caracteres", font=("Roboto", 35, "bold"),width=1260,height=90,fg_color=mainBlue,border_color=mainBlue,text_color=white,border_width=1,corner_radius=90,justify="center")
                        nomeDoQuiz.place(x=330,y=110)
                        categoriaDoQuiz = ctk.CTkEntry(screen,placeholder_text_color=white,placeholder_text="Categoria do Quiz / 100 caracteres", font=("Roboto", 35, "bold"),width=1260,height=90,fg_color=mainBlue,border_color=mainBlue,text_color=white,border_width=1,corner_radius=90,justify="center")
                        categoriaDoQuiz.place(x=330,y=220)
                        
                        varFinalizadora = 0
                        telaFinalX = 585.3
                        telaFinalY = 311.8 
                        while varFinalizadora < numQuest:
                            showErrosEAcertos = ctk.CTkButton(screen,text=varFinalizadora+1,font=("Roboto", 20, "bold"),width=70,height=70,fg_color=lightGray,border_color=black, hover_color=lightGray, border_width=5, text_color=black, command=None)
                            showErrosEAcertos.place(x=telaFinalX,y=telaFinalY)
                            if varFinalizadora == 8 or varFinalizadora == 17 or varFinalizadora == 26 or varFinalizadora == 35 or varFinalizadora == 44 or varFinalizadora == 53 or varFinalizadora == 62:
                                telaFinalX = 585.3
                                telaFinalY = telaFinalY+80
                            else:
                                telaFinalX = telaFinalX+85  
                            varFinalizadora = varFinalizadora+1

                        global concluir
                        concluir = 0
                        def finalizarQuiz():
                            
                                global categoriaQuiz
                                nomeQuiz = nomeDoQuiz.get()
                                categoriaQuiz = categoriaDoQuiz.get()
                                if nomeQuiz == "" or categoriaQuiz == "":
                                    AvisoNomeQuiz()
                                else:
                                    global concluir
                                    if concluir == 0:
                                        concluir = 1
                                        AvisoConclusao()
                                    elif concluir == 1:
                                        buttonBack.configure(state='disabled')
                                        dictPerguntas = {}
                                        index = 0
                                        for item in listaDeQuestoes:
                                            dictPerguntas[item] = []
                                            for alt, boolean in zip(listaDeAlternativas[index],listaGabarito[index]):
                                                dictPerguntas[item].append([alt,boolean])
                                        createQuiz(Account,nomeQuiz,categoriaQuiz,dictPerguntas)
                                        self.destroy()
                            
                        buttonBack = ctk.CTkButton(
                            screen,
                            text='Voltar ao menu',
                            command=finalizarQuiz,
                            bg_color=white,
                            fg_color=lightGray,
                            hover_color=lightGray,
                            text_color=black
                        )
                        buttonBack.place(x=100, y=915)

                else:
                    AvisoPerguntasProf()
            else:
                AvisoRespostasProf()

        buttonFinalizar = ctk.CTkButton(
            screen,
            text='FINALIZAR',
            command=finalizar,
            bg_color=white,
            fg_color=gray,
            hover_color=gray
        )
        buttonFinalizar.place(x=1750, y=100)

#Classes de avisos-----------------------------------------------------------------------------------------------------------------------------------    
class AvisoRespostasProf(ctk.CTk):
     def __init__(self):
        super().__init__()
        self.geometry("500x400")
        self.minsize(500, 400) 
        self.maxsize(500, 400)
        self.config(bg="#7D9EFF")

        def ok():
            self.destroy()

        self.label = ctk.CTkLabel(self, text="Aviso\nAo menos uma das questões tem que ser verdadeira.\nPara configurar qual questão é a verdadeira click no quadrado vermelho, verde significa que a resposta é verdadeira\ne vermelho é que é falsa.", font=("Roboto", 30, "bold"), bg_color="#7D9EFF", wraplength=480)
        self.label.pack(padx=20, pady=20)
        self.botaoConfirm = ctk.CTkButton(self, text="OK", font=("Roboto", 10, "bold"), bg_color="#7D9EFF", fg_color=green,hover_color=green, command=ok)
        self.botaoConfirm.place(x=172,y=320)

        self.mainloop()

class AvisoFaltaAlternativa(ctk.CTk):
     def __init__(self):
        super().__init__()
        self.geometry("500x400")
        self.minsize(520, 400) 
        self.maxsize(520, 400)
        self.config(bg="#7D9EFF")

        def ok():
            self.destroy()

        self.label = ctk.CTkLabel(self, text="Aviso\nTodas as quatro alternativas devem possuir uma resposta caso já tenha a escrito confira se clickou no botão de confirmar.", font=("Roboto", 30, "bold"), bg_color="#7D9EFF", wraplength=480)
        self.label.pack(padx=20, pady=20)
        self.botaoConfirm = ctk.CTkButton(self, text="OK", font=("Roboto", 10, "bold"), bg_color="#7D9EFF", fg_color=green,hover_color=green, command=ok)
        self.botaoConfirm.place(x=172,y=300)

        self.mainloop()

class AvisoFaltaPergunta(ctk.CTk):
     def __init__(self):
        super().__init__()
        self.geometry("500x400")
        self.minsize(520, 400) 
        self.maxsize(520, 400)
        self.config(bg="#7D9EFF")

        def ok():
            self.destroy()

        self.label = ctk.CTkLabel(self, text="Aviso\nAinda falta declarar qual é a questão, caso já tenha a escrito confira se clickou no botão de confirmar.", font=("Roboto", 30, "bold"), bg_color="#7D9EFF", wraplength=480)
        self.label.pack(padx=20, pady=20)
        self.botaoConfirm = ctk.CTkButton(self, text="OK", font=("Roboto", 10, "bold"), bg_color="#7D9EFF", fg_color=green,hover_color=green, command=ok)
        self.botaoConfirm.place(x=172,y=300)

        self.mainloop()

class ConfirmacaoProf(ctk.CTk):
     def __init__(self):
        super().__init__()
        self.geometry("500x400")
        self.minsize(520, 400) 
        self.maxsize(520, 400)
        self.config(bg="#7D9EFF")

        def ok():
            self.destroy()

        self.label = ctk.CTkLabel(self, text="Aviso\nApós clickar no botão finalizar novamente, o quiz sera encerrado e criado para os alunos poderem jogar, logo recomendamos que revise o quiz um ultima fez antes de finaliza-lo.", font=("Roboto", 30, "bold"), bg_color="#7D9EFF", wraplength=480)
        self.label.pack(padx=20, pady=20)
        self.botaoConfirm = ctk.CTkButton(self, text="OK", font=("Roboto", 10, "bold"), bg_color="#7D9EFF", fg_color=green,hover_color=green, command=ok)
        self.botaoConfirm.place(x=172,y=300)

        self.mainloop()

class AvisoPerguntasProf(ctk.CTk):
     def __init__(self):
        super().__init__()
        self.geometry("500x400")
        self.minsize(520, 400) 
        self.maxsize(520, 400)
        self.config(bg="#7D9EFF")

        def ok():
            self.destroy()

        self.label = ctk.CTkLabel(self, text="Aviso\nO quiz deve ter ao menos 10 questões.", font=("Roboto", 30, "bold"), bg_color="#7D9EFF", wraplength=480)
        self.label.pack(padx=20, pady=20)
        self.botaoConfirm = ctk.CTkButton(self, text="OK", font=("Roboto", 10, "bold"), bg_color="#7D9EFF", fg_color=green,hover_color=green, command=ok)
        self.botaoConfirm.place(x=172,y=300)

        self.mainloop()

class AvisoSaida(ctk.CTk):
     def __init__(self):
        super().__init__()
        self.geometry("500x400")
        self.minsize(520, 400) 
        self.maxsize(520, 400)
        self.config(bg="#7D9EFF")

        def ok():
            self.destroy()

        self.label = ctk.CTkLabel(self, text="Aviso\nA próxima vez que você clickar no botão sair o quiz sera fechado e tudo sera perdido.", font=("Roboto", 30, "bold"), bg_color="#7D9EFF", wraplength=480)
        self.label.pack(padx=20, pady=20)
        self.botaoConfirm = ctk.CTkButton(self, text="OK", font=("Roboto", 10, "bold"), bg_color="#7D9EFF", fg_color=green,hover_color=green, command=ok)
        self.botaoConfirm.place(x=172,y=300)

        self.mainloop()

class AvisoConclusao(ctk.CTk):
     def __init__(self):
        super().__init__()
        self.geometry("500x400")
        self.minsize(520, 400) 
        self.maxsize(520, 400)
        self.config(bg="#7D9EFF")

        def ok():
            self.destroy()

        self.label = ctk.CTkLabel(self, text="Aviso\nA próxima vez que você clickar no botão voltar ao menu\n o quiz sera encerrado e criado,\n após isso na tela inicial será\n possível de visualizar o código do quiz.", font=("Roboto", 30, "bold"), bg_color="#7D9EFF", wraplength=480)
        self.label.pack(padx=20, pady=20)
        self.botaoConfirm = ctk.CTkButton(self, text="OK", font=("Roboto", 10, "bold"), bg_color="#7D9EFF", fg_color=green,hover_color=green, command=ok)
        self.botaoConfirm.place(x=172,y=300)

        self.mainloop()

class AvisoNomeQuiz(ctk.CTk):
     def __init__(self):
        super().__init__()
        self.geometry("500x400")
        self.minsize(520, 400) 
        self.maxsize(520, 400)
        self.config(bg="#7D9EFF")

        def ok():
            self.destroy()

        self.label = ctk.CTkLabel(self, text="Aviso\nÉ necessário atribuir um nome ao Quiz e categoria ao Quiz", font=("Roboto", 30, "bold"), bg_color="#7D9EFF", wraplength=480)
        self.label.pack(padx=20, pady=20)
        self.botaoConfirm = ctk.CTkButton(self, text="OK", font=("Roboto", 10, "bold"), bg_color="#7D9EFF", fg_color=green,hover_color=green, command=ok)
        self.botaoConfirm.place(x=172,y=300)

        self.mainloop()