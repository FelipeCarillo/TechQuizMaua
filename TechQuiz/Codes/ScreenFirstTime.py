import customtkinter as ctk
from PIL import Image, ImageTk
from Colors import Branco, Cinza, AzulKing, Preto
from DataBase import changeStatusFrstTime
from Images import Logo


def ScreenFrstTime(atribute, data):
    Window = ctk.CTk()
    Window.geometry("700x700")
    Window.maxsize(700, 700)

    imageLogo = Logo()

    curso = ["", "Ciência da Computação", "Sistema da Informação"]

    ano = ["", "01", "02", "03", "04", "05"]

    fundo = ctk.CTkCanvas(
        Window, background="#5271FF", width=700, height=700, highlightthickness=0
    )
    fundo.grid(column=0, row=0)

    def check_Entry():
        var_list = [inputCurso, inputAno]
        if all(var.get() for var in var_list):
            buttonSave.configure(hover=True)
            if (len(inputAno.get()) == 2 or len(inputAno.get()) == 1)and inputAno.get().isnumeric() and len(inputCurso.get()) <= 100:
                Window.destroy()
                changeStatusFrstTime(atribute, data)

            else:
                buttonSave.configure(hover=False)
        else:
            buttonSave.configure(hover=False)

    def Entry(x, values):
        
        entry = ctk.CTkComboBox(
            fundo,
            values=values,
            width=300,
            height=82,
            bg_color=AzulKing,
            button_color=Branco,
            border_width=0,
            corner_radius=20,
            fg_color=Branco,
            font=("Roboto", 20, "bold"),
            text_color=Preto,
            button_hover_color="#d9d9d9",
            dropdown_text_color=Preto,
            dropdown_fg_color=Branco,
        )
        entry.place(x=x, y=540)
        return entry

    texto = ctk.CTkLabel(
        fundo,
        text="Bem Vindo Aluno!\nPelas minhas verificações está\né sua primeira vez por aqui!",
        height=120,
        corner_radius=20,
        fg_color=Branco,
        bg_color=AzulKing,
        font=("Roboto", 25, "bold"),
        text_color=Cinza,
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
        text_color=AzulKing,
        font=("Roboto", 20, "bold"),
        fg_color=Branco,
        border_width=3,
        hover_color="#d9d9d9",
        border_color=Cinza,
        command= check_Entry,
        hover=False
    )

    buttonSave.place(x=302.5, y=649.4)

    Window.mainloop()
    passInterface = True


    return passInterface
