import customtkinter as ctk
from PIL import Image, ImageTk
from Colors import *
from DataBase import setOneData
from Images import ImageLogoNEscrita




def ScreenFrstTime(registro):
    global data_list
    def interface():
        global data_list
        Window = ctk.CTk()
        Window.geometry("700x700")
        Window.maxsize(700, 700)

        imageLogo = ImageLogoNEscrita([300,280])

        curso = ["", "Ciência da Computação", "Sistema da Informação"]

        ano = ["", "01", "02", "03", "04", "05"]

        fundo = ctk.CTkCanvas(
            Window, background="#5271FF", width=700, height=700, highlightthickness=0
        )
        fundo.grid(column=0, row=0)

        def check_Entry():
            global data_list
            curso = inputCurso.get()
            ano = inputAno.get()
            var_list = [inputCurso, inputAno]
            if all(var.get() for var in var_list):
                buttonSave.configure(hover=True)
                if (len(ano) == 2 or len(ano) == 1)and ano.isnumeric() and len(curso) <= 100:
                    data_list = 0, curso, ano
                    setOneData(table='usuario',chgAtribute='FirstLogin',chgValue=0, findAtribute="idUser",findValue=registro)
                    setOneData(table='usuario',chgAtribute='cursoUser',chgValue=curso, findAtribute="idUser",findValue=registro)
                    setOneData(table='usuario',chgAtribute='anoUser',chgValue=ano, findAtribute="idUser",findValue=registro)
                    Window.destroy()
                else:
                    buttonSave.configure(hover=False)

        def Entry(x, values):
            
            entry = ctk.CTkComboBox(
                fundo,
                values=values,
                width=300,
                height=82,
                bg_color=mainBlue,
                button_color=white,
                border_width=0,
                corner_radius=20,
                fg_color=white,
                font=("Roboto", 20, "bold"),
                text_color=black,
                button_hover_color="#d9d9d9",
                dropdown_text_color=black,
                dropdown_fg_color=white,
            )
            entry.place(x=x, y=540)
            return entry
        
        texto = ctk.CTkLabel(
            fundo,
            text=f"Bem Vindo Aluno!\nPelas minhas verificações está\né sua primeira vez por aqui!",
            height=120,
            corner_radius=20,
            fg_color=white,
            bg_color=mainBlue,
            font=("Roboto", 25, "bold"),
            text_color=gray,
        )
        texto.place(x=135, y=340)
        fundo.create_image(360, 170,image=imageLogo)
        fundo.create_text(
            160, 510, text="CURSO", fill="#292323", font=("Roboto", 31, "bold")
        )
        fundo.create_text(530, 510, text="ANO", fill="#292323", font=("Roboto", 31, "bold"))

        inputCurso = Entry(20, curso)
        inputAno = Entry(380, ano)

        buttonSave = ctk.CTkButton(
            fundo,
            width=92.6,
            height=43.6,
            text="SALVAR",
            text_color=mainBlue,
            font=("Roboto", 20, "bold"),
            fg_color=white,
            border_width=3,
            hover_color="#d9d9d9",
            border_color=gray,
            command= check_Entry,
            hover=False
        )

        buttonSave.place(x=302.5, y=649.4)

        Window.mainloop()
    interface()
    return data_list



