import customtkinter as ctk
from Local.Codigo.Colors import *
from Local.Codigo.DataBase import setProgress
from Local.Codigo.Images import ImageGoBack, ImageGoFoward
from random import shuffle

class QuizScreen(ctk.CTkToplevel):
    def __init__(self, Account, Quiz):
        Width = 1920
        Height = 1020
        super().__init__()
        self.geometry("1920x1020") 
        self.title("TechQuiz - Quiz")
        self.maxsize(Width, Height)
        screen = ctk.CTkCanvas(self, background="#FFFFFF", width=Width, height=Height, highlightthickness=0)
        screen.pack()
        screen.create_rectangle(0, 0, Width, 50, fill=darkBlue, outline=darkBlue)
        screen.create_rectangle(0, 970, Width, Height, fill=darkBlue, outline=darkBlue)
        questoes = Quiz.get_questoes()

        global varChange
        varChange = 0
        
        listaQuiz = []
        for questao in questoes:
            listaQuiz.append(questao)
        shuffle(listaQuiz)
        numQuest = len(listaQuiz)

        listaDeAlternativas = []
        listaValoresDasAlternativas = []
        listaDasRepostasDasAlternativas = []
        conjAlternativas = 0
        while conjAlternativas < numQuest:
            alt = questoes[listaQuiz[conjAlternativas]]
            shuffle(alt)
            alt1 = alt[0][0]
            alt2 = alt[1][0]
            alt3 = alt[2][0]
            alt4 = alt[3][0]
            alt1V = alt[0][1]
            alt2V = alt[1][1]
            alt3V = alt[2][1]
            alt4V = alt[3][1]
            listaDeAlternativas.append([alt1,alt2,alt3,alt4])
            listaValoresDasAlternativas.append([alt1V,alt2V,alt3V,alt4V])
            listaDasRepostasDasAlternativas.append([False,False,False,False])
            conjAlternativas +=1


        def chamaQuest(valor):
            None

        posiQuest = 200
        i = 0
        listaBotoes = []
        while i < numQuest:
            placeNumQuest = ctk.CTkButton(screen,text=i+1,font=("Roboto", 10, "bold"),width=38,height=24,fg_color=lightGray,border_color="#8F8F8F", hover_color=mainBlue,
                         border_width=5, text_color=black,corner_radius=10, command=chamaQuest)
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
                if len(linha + palavra + " ") >= 25:
                    linha += '\n'
                    frase += linha
                    linha = ""
                linha += palavra + " "
            frase += linha
            return frase

        def botao1_precionado(onlyshow=False):
            if onlyshow == False:
                listaDasRepostasDasAlternativas[varChange][0] = not listaDasRepostasDasAlternativas[varChange][0] 
            if listaDasRepostasDasAlternativas[varChange][0] == False:
                opcao1.configure(fg_color=lightGray)
            else:
                opcao1.configure(fg_color=mainBlue)
            opcao1.configure(text=formata_texto(listaDeAlternativas[varChange][0]))

        def botao2_precionado(onlyshow=False):
            if onlyshow == False:
                listaDasRepostasDasAlternativas[varChange][1] = not listaDasRepostasDasAlternativas[varChange][1] 
            if listaDasRepostasDasAlternativas[varChange][1] == False:
                opcao2.configure(fg_color=lightGray)
            else:
                opcao2.configure(fg_color=mainBlue)
            opcao2.configure(text=formata_texto(listaDeAlternativas[varChange][1]))
            
        def botao3_precionado(onlyshow=False):
            if onlyshow == False:
                listaDasRepostasDasAlternativas[varChange][2] = not listaDasRepostasDasAlternativas[varChange][2] 
            if listaDasRepostasDasAlternativas[varChange][2] == False:
                opcao3.configure(fg_color=lightGray)
            else:
                opcao3.configure(fg_color=mainBlue)
            opcao3.configure(text=formata_texto(listaDeAlternativas[varChange][2]))

        def botao4_precionado(onlyshow=False):
            if onlyshow == False:
                listaDasRepostasDasAlternativas[varChange][3] = not listaDasRepostasDasAlternativas[varChange][3] 
            if listaDasRepostasDasAlternativas[varChange][3] == False:
                opcao4.configure(fg_color=lightGray)
            else:
                opcao4.configure(fg_color=mainBlue)
            opcao4.configure(text=formata_texto(listaDeAlternativas[varChange][3]))

        opcao1 = ctk.CTkButton(screen,width=600,height=200,fg_color=lightGray,hover_color=mainBlue,text="frase1",font=("Roboto", 34, "bold"),text_color=black,corner_radius=45,border_color="#8F8F8F",border_width=4, command=botao1_precionado)
        opcao1.place(x=200,y=450)
        opcao2 = ctk.CTkButton(screen,width=600,height=200,fg_color=lightGray,hover_color=mainBlue,text="frase2",font=("Roboto", 34, "bold"),text_color=black,corner_radius=45,border_color="#8F8F8F",border_width=4, command=botao2_precionado)
        opcao2.place(x=200,y=670)
        opcao3 = ctk.CTkButton(screen,width=600,height=200,fg_color=lightGray,hover_color=mainBlue,text="frase3",font=("Roboto", 34, "bold"),text_color=black,corner_radius=45,border_color="#8F8F8F",border_width=4, command=botao3_precionado)
        opcao3.place(x=1120,y=450)
        opcao4 = ctk.CTkButton(screen,width=600,height=200,fg_color=lightGray,hover_color=mainBlue,text="frase4",font=("Roboto", 34, "bold"),text_color=black,corner_radius=45,border_color="#8F8F8F",border_width=4, command=botao4_precionado)
        opcao4.place(x=1120,y=670)

        def restoreButtonState():
            botao1_precionado(True)
            botao2_precionado(True)
            botao3_precionado(True)
            botao4_precionado(True)
        
        def showNumberQuestion():
            for botoes in listaBotoes:
                botoes.configure(border_color="#8F8F8F")
            questaoAtual = listaBotoes[varChange]
            questaoAtual.configure(border_color=mainBlue)
        
        def verificaResposta():
            questaoAtual = listaBotoes[varChange]
            questaoAtual.configure(fg_color=lightGray)
            for resposta in listaDasRepostasDasAlternativas[varChange]:
                if resposta == True:
                    questaoAtual.configure(fg_color=green)


        def mudaPagB():
            global varChange
            if varChange > 0:
                verificaResposta()
                varChange = varChange-1
                pergunta.configure(text=listaQuiz[varChange])
                #botoes
                restoreButtonState()
                showNumberQuestion()
                
                
        def mudaPagF():
            global varChange
            if varChange < numQuest-1:
                verificaResposta()
                varChange = varChange+1
                pergunta.configure(text=listaQuiz[varChange])
                #botoes
                restoreButtonState()
                showNumberQuestion()
                

        Seta = ImageGoBack([70, 70])
        Seta2 = ImageGoFoward([70, 70])
        ctk.CTkButton(screen,image=Seta,text=None,fg_color=white,hover=None, command=mudaPagB).place(x=60,y=890)
        ctk.CTkButton(screen,image=Seta2,text=None,fg_color=white,hover=None, command=mudaPagF).place(x=1720,y=890)

        questaoAtual = listaBotoes[varChange]
        questaoAtual.configure(border_color=mainBlue)

        botao1_precionado(True)
        botao2_precionado(True)
        botao3_precionado(True)
        botao4_precionado(True)

        def clear_frame():
            for widgets in screen.winfo_children():
                widgets.destroy()

        def sair():
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

        global validar
        validar = 0
        def finalizar():
            global validar
            verificaQuiz = 0
            for resposta in listaDasRepostasDasAlternativas:
                if resposta[0]==True or resposta[1]==True or resposta[2] == True or resposta[3]==True:
                    verificaQuiz +=1
            if verificaQuiz == numQuest:
                if validar == 0:
                    validar = 1
                    Confirmacao()
                elif validar == 1:
                    clear_frame()
                    screen.create_rectangle(0, 0, 50, Height, fill=darkBlue, outline=darkBlue)
                    screen.create_rectangle(1870, 0, Width, Height, fill=darkBlue, outline=darkBlue)
                    screen.create_rectangle(200, 100,1720,400,fill=white,outline=white)

                    nome = ctk.CTkEntry(screen,placeholder_text_color=white,placeholder_text=Account.getNome(), font=("Roboto", 35, "bold"),width=1260,height=90,fg_color=mainBlue,border_color=mainBlue,text_color=white,border_width=1,corner_radius=90,justify="center")
                    nome.configure(state=ctk.DISABLED)
                    nome.place(x=330,y=110)

                    acertos = 0
                    varFinalizadora = 0
                    telaFinalX = 585.3
                    telaFinalY = 311.8 
                    while varFinalizadora < numQuest:
                        if listaDasRepostasDasAlternativas[varFinalizadora] == listaValoresDasAlternativas[varFinalizadora]:
                            acertos += 1

                            showErrosEAcertos = ctk.CTkButton(screen,text=varFinalizadora+1,font=("Roboto", 20, "bold"),width=70,height=70,fg_color='#36D437',border_color=black, hover_color='#36D437', border_width=5, text_color=black, command=None)
                            showErrosEAcertos.place(x=telaFinalX,y=telaFinalY)
                            if varFinalizadora == 8 or varFinalizadora == 17 or varFinalizadora == 26 or varFinalizadora == 35 or varFinalizadora == 44 or varFinalizadora == 53 or varFinalizadora == 62:
                                telaFinalX = 585.3
                                telaFinalY = telaFinalY+80
                            else:
                                telaFinalX = telaFinalX+85
                        else:
                            showErrosEAcertos = ctk.CTkButton(screen,text=varFinalizadora+1,font=("Roboto", 20, "bold"),width=70,height=70,fg_color="#D43636",border_color=black, hover_color="#D43636", border_width=5, text_color=black, command=None)
                            showErrosEAcertos.place(x=telaFinalX,y=telaFinalY)
                            if varFinalizadora == 8 or varFinalizadora == 17 or varFinalizadora == 26 or varFinalizadora == 35 or varFinalizadora == 44 or varFinalizadora == 53 or varFinalizadora == 62:
                                telaFinalX = 585.3
                                telaFinalY = telaFinalY+80
                            else:
                                telaFinalX = telaFinalX+85  
                        varFinalizadora = varFinalizadora+1
                    descAcertos = ctk.CTkButton(screen,text="",font=("Trocchi", 20, "bold"),width=70,height=70,fg_color='#36D437',border_color=black, hover_color='#36D437', border_width=5, text_color=black, command=None).place(x=1404.7,y=791.8)
                    textoAcertos = ctk.CTkLabel(screen,justify='left',text="Acertos",font=("Roboto", 18),text_color=black,fg_color=white,bg_color=white,wraplength=1720-250).place(x=1487.7,y=812.7)
                    descErros = ctk.CTkButton(screen,text="",font=("Trocchi", 20, "bold"),width=70,height=70,fg_color="#D43636",border_color=black, hover_color="#D43636", border_width=5, text_color=black, command=None).place(x=1404.7,y=871.8)
                    textoErros = ctk.CTkLabel(screen,justify='left',text="Erros",font=("Roboto", 18),text_color=black,fg_color=white,bg_color=white,wraplength=1720-250).place(x=1487.7,y=892.7)
                    resultado = f'{acertos/numQuest * 100:.2f}'
                    setProgress(Quiz.get_idJogo(),Account.getIdUsuario(),resultado)
                    resultado = f"Resultado: {resultado}%"
                    

                    pontuacao = ctk.CTkEntry(screen,placeholder_text_color=black,placeholder_text=resultado, font=("Roboto", 32.5, "bold"),width=320,height=52,fg_color=white,border_color=white,text_color=black,border_width=1,justify="center")
                    pontuacao.configure(state=ctk.DISABLED)
                    pontuacao.place(x=800,y=230)

                    buttonBack = ctk.CTkButton(
                        screen,
                        text='Voltar ao menu',
                        command=sair,
                        bg_color=white,
                        fg_color=lightGray,
                        hover_color=lightGray,
                        text_color=black
                    )
                    buttonBack.place(x=100, y=915)
            else:
                AvisoRespostas()

        buttonFinalizar = ctk.CTkButton(
            screen,
            text='FINALIZAR',
            command=finalizar,
            bg_color=white,
            fg_color=gray,
            hover_color=gray
        )
        buttonFinalizar.place(x=1750, y=100)

class AvisoRespostas(ctk.CTk):
     def __init__(self):
        super().__init__()
        self.geometry("400x300")
        self.minsize(400, 300) 
        self.maxsize(400, 300)
        self.config(bg="#7D9EFF")

        self.label = ctk.CTkLabel(self, text="Ainda faltam \nquestões a \nserem respondidas\n\nConfira as questões que\nnão estão em verde", font=("Roboto", 30, "bold"), bg_color="#7D9EFF")
        self.label.pack(padx=20, pady=20)

        self.mainloop()

class Confirmacao(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("460x350")
        self.minsize(480, 350) 
        self.maxsize(480, 350)
        self.config(bg="#7D9EFF")

        def ok():
            self.destroy()
            
        self.label = ctk.CTkLabel(self, text="AVISO!\n\nApós clicar no botão finalizar\nnovamente você não podera\nalterar as suas respostas, \nrecomendamos revizá-las uma\nultima vez antes de finalizar.", font=("Roboto", 30, "bold"), bg_color="#7D9EFF")
        self.label.pack(padx=20, pady=20)
        self.botaoConfirm = ctk.CTkButton(self, text="OK", font=("Roboto", 10, "bold"), bg_color="#7D9EFF", fg_color=green,hover_color=green, command=ok)
        self.botaoConfirm.place(x=172,y=300)

        self.mainloop()
