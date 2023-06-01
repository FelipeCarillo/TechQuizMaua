import requests
import json
from Local.Codigo.DataBase import getDescribe, operationGPT
import customtkinter as ctk
from Local.Codigo.Colors import *
from Local.Codigo.Images import (ImageLogoNEscrita,ImageDataBase)
from Local.Codigo.Account import *
import customtkinter as ctk


def chatGPT(Funcao,Comando):
    try:
        API_KEY = 'API_KEY_AQUI'
        url = "https://api.openai.com/v1/chat/completions"
        Headers={"Authorization": f"Bearer {API_KEY}","Content-Type":"application/json"}
        id_model = "gpt-3.5-turbo"
        tables = getDescribe()
        roles_content = f"""
        Forneça em apenas 1 linha comandos MySQL, que correspondem ao seguinte DataBase:
        {tables}
        """
        data = {
            "model":id_model,
            "messages":[
                {"role": "system", "content":f"Você é um assistente de DBA do meu projeto. {roles_content}"},
                {"role": "user", "content":f"{Funcao}: {Comando}"}
            ]
        }
        data = json.dumps(data)
        r=requests.post(url,headers=Headers,data=data)
        answer = r.json()
        message = answer['choices'][0]['message']['content']
        return message
    except:
        return "Erro, tente novamente mais tarde. Verifique a API KEY."


class AdminMainScreen(ctk.CTk):
    def __init__ (self,Account):
        super().__init__()
        Width = 1920
        Height = 1020
        self.geometry("1920x1020")
        self.maxsize(Width, Height)
        self.config(bg="white")
        self.config(bg=white)
        self.title('TechQuiz - Administrador')
        
        imageLogoNPng = ImageLogoNEscrita([300, 280])
        
        # Informações
        gridInfo = ctk.CTkCanvas(
            self, background="#5271FF", width=400, height=Height, highlightthickness=0
        )
        gridInfo.grid(column=0, row=0, sticky=ctk.W)
        gridInfo.create_rectangle(0, 0, 400, 50, fill=darkBlue, outline=darkBlue)
        gridInfo.create_rectangle(0, 970, 400, 970 + 50, fill=darkBlue, outline=darkBlue)

        ctk.CTkButton(gridInfo,image=imageLogoNPng,fg_color=mainBlue,state='disable',text='').place(x=50,y= 180)

        # Opções
        gridOpcoes = ctk.CTkCanvas(
            self,
            background=white,
            width=Width - 400,
            height=Height,
            highlightthickness=0,
        )
        gridOpcoes.grid(column=1, row=0, sticky=ctk.E)

        # Adição das informações
        nome = ctk.CTkEntry(
            gridInfo,
            # placeholder_text=text,
            placeholder_text_color=white,
            font=("Roboto", 25, "bold"),
            width=324,
            height=85,
            fg_color=darkBlue,
            border_color=darkBlue,
            text_color=white,
            border_width=1,
            corner_radius=20,
            justify="center",
        )
        nome.insert(0,Account.getNome())
        nome.configure(state=ctk.DISABLED)  # Impede de mudar o valor
        nome.place(x=38, y=500)

        Crud = ["CONSULTAR","INSERIR","ATUALIZAR","DELETAR"] 
        gridOpcoes.create_text(165,58,text="Função:",font=("Roboto", 25, "bold"))
        chooseCrud = ctk.CTkComboBox(gridOpcoes,state='readonly',font=("Roboto", 25, "bold"),width=355,height=80,values=Crud,fg_color=darkBlue, text_color=white,bg_color=white, corner_radius=20, justify="center",)
        chooseCrud.place(x=100,y=85)
        gridOpcoes.create_text(578,58,text="Comando:",font=("Roboto", 25, "bold"))
        writeCode = ctk.CTkEntry(gridOpcoes,font=("Roboto", 25, "bold"),width=920,height=80,fg_color=white, border_color=darkBlue, text_color=black,bg_color=white, border_width=6, corner_radius=20, justify="left")
        writeCode.place(x=500,y=85)
        outputBox = ctk.CTkTextbox(gridOpcoes, width=1320,height=600,font=("Roboto", 25, "bold"))
        outputBox.place(x=100,y=220)

        # Botões
        def processData():
            global Funcao, Comando
            
            buttonProcessar.configure(state='disabled')
            outputBox.delete('0.0','end')
            
            Funcao = chooseCrud.get()
            Comando = writeCode.get()

            if Funcao:
                output = chatGPT(Funcao,Comando)
                outputBox.insert('0.0',text=output)
                buttonExecute.configure(state='normal')
                buttonProcessar.configure(state='normal')
            else:
                outputBox.insert('0.0',text='Selecione uma Função.')
                buttonProcessar.configure(state='normal')

        def showTables():
            showTable()

        def executeQuery():
            outputBox.configure(font=("Roboto", 25, "bold"))
            buttonExecute.configure(state='disabled')
            Query = outputBox.get('0.0','end')
            try:
                retorno = operationGPT(Funcao,Query)
                outputBox.delete('0.0','end')
                if Funcao == "CONSULTAR":
                    outputBox.configure(font=("Roboto", 15, "bold"))
                outputBox.insert('0.0',text=retorno)
                buttonExecute.configure(state='normal')
            except:
                outputBox.insert('end',text=f'\n\n\n\n{"ERRO":_^107}')
                buttonExecute.configure(state='normal')
                
            


        buttonProcessar = ctk.CTkButton(gridOpcoes,command=processData ,font=("Roboto", 25, "bold"), text="PROCESSAR",width=350, height=100,fg_color=darkBlue, border_color=white, text_color=white,bg_color=white,hover_color=hoverColor, border_width=1, corner_radius=20)
        buttonProcessar.place(x=100, y=850)
        buttonTables = ctk.CTkButton(gridOpcoes,command=showTables,font=("Roboto", 25, "bold"), text="TABLES",width=350, height=100,fg_color=darkBlue, border_color=white, text_color=white,bg_color=white,hover_color=hoverColor, border_width=1, corner_radius=20)
        buttonTables.place(x=585, y=850)
        buttonExecute = ctk.CTkButton(gridOpcoes,command=executeQuery,state='disabled',font=("Roboto", 25, "bold"), text="EXECUTAR",width=350, height=100,fg_color=darkBlue, border_color=white, text_color=white,bg_color=white,hover_color=hoverColor, border_width=1, corner_radius=20)
        buttonExecute.place(x=1070, y=850)

class showTable (ctk.CTkToplevel):
    def __init__ (self):
        super().__init__()
        Width = 880
        Height = 600
        self.title("TechQuiz - DataBase Tables")
        self.maxsize(Width, Height)
        PNGDataBase=ImageDataBase([Width,Height])
        ctk.CTkButton(self,width=1920,height=1020,state='disabled',image=PNGDataBase,text=None,bg_color=white,fg_color=white).pack()