import requests
import json
from DataBase import getDescribe, operationGPT
import customtkinter as ctk

def chatGPT(Message):
    try:
        API_KEY = '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'
        url = "https://api.openai.com/v1/chat/completions"
        Headers={"Authorization": f"Bearer {API_KEY}","Content-Type":"application/json"}
        id_model = "gpt-3.5-turbo"
        tables = getDescribe()
        roles_content = f"""
        Forneça em apenas 1 linha comandos MySQL, que correspondem para o seguinte DataBase:
        {tables}
        Jamais exclua o Banco de Dados.
        """
        data = {
            "model":id_model,
            "messages":[
                {"role": "system", "content":f"Você é um assistente de DBA do meu projeto. {roles_content}"},
                {"role": "user", "content":f"{Message}"}
            ]
        }
        data = json.dumps(data)
        r=requests.post(url,headers=Headers,data=data)
        answer = r.json()
        message = answer['choices'][0]['message']['content']
        return message
    except:
        return "Erro, tente novamente mais tarde."

Width = 1920
Height = 1020

class Administrador(ctk.CTk):
    def __init__ (self,Account):
        super().__init__()
        self.title("TechQuiz - Administrador")
        self.geometry("1920x1020")
        self.maxsize(Width, Height)
        self.config(bg="white")
        InputBox = ctk.CTkTextbox(self,width=900,height=500,)
        InputBox.place(x=0,y=200)
        AnswerBox = ctk.CTkTextbox(self,width=900,height=500)
        AnswerBox.place(x=1000,y=200)
        
        def makeQuery():
            Message = InputBox.get("0.0","end")
            Query = chatGPT(Message)
            print(Query)
            if Query != "Erro, tente novamente mais tarde.":
                try:
                    result=operationGPT(Query)
                except:
                    result="Erro, tente novamente mais tarde."
                AnswerBox.insert(index="0.0",text=result)
                # print(result)
            else:
                AnswerBox.insert(index="0.0",text="Erro, tente novamente mais tarde.")

        a = ctk.CTkButton(self,width=100,height=100,command=makeQuery).place(x=0,y=500)


Administrador(1).mainloop()
