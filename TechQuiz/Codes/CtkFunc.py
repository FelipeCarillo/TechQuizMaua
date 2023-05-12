import customtkinter as ctk
from Colors import lightGray,black,mainBlue,lightGray2

def createQuizBox(master,x,y,bg_color,QuizName,Owner,categoria, number_questions,command):
    
    canvas = ctk.CTkCanvas(master, background=bg_color, width=269+18, height=298+15, highlightthickness=0)
    canvas.place(x=x,y=y)

    canvas.create_rectangle(18,0,18+269,298, fill=lightGray2, outline=lightGray2)
    canvas.create_rectangle(0,15,269,15+298, fill=lightGray, outline=lightGray)
    x=10
    y=15
    
    tittle=ctk.CTkLabel(canvas, text=f"{QuizName}", font=(
                "Roboto", 42, "bold"), bg_color=lightGray, text_color=black, fg_color=lightGray)
    tittle.place(x=x,y=y+30)
    Autor=ctk.CTkLabel(canvas, text=f"Autor: {Owner}", font=(
    "Roboto", 20, "bold"), bg_color=lightGray, text_color=black, fg_color=lightGray)
    Autor.place(x=x,y=y+90)
    Categoria=ctk.CTkLabel(canvas, text=f"Categoria: {categoria}", font=(
                "Roboto", 20, "bold"), bg_color=lightGray, text_color=black, fg_color=lightGray)
    Categoria.place(x=x,y=y+130)
    NQuestoes=ctk.CTkLabel(canvas, text=f"N° de Questões: {number_questions}", font=(
                "Roboto", 20, "bold"), bg_color=lightGray, text_color=black, fg_color=lightGray)
    NQuestoes.place(x=x,y=y+170)
    ButtonJogar = ctk.CTkButton(
            master=canvas,
            text='Jogar',
            font=("Roboto", 28, "bold"),
            width=200,
            height=32,
            command=command,
            fg_color=mainBlue,
            bg_color=lightGray,
            hover_color=mainBlue,
            corner_radius=360
    )
    ButtonJogar.place(x=269/2-100, y=298+15-62)
    return ButtonJogar 