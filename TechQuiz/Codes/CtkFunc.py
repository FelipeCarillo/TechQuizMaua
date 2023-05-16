import customtkinter as ctk
from Colors import lightGray,black,mainBlue,lightGray2,hoverColor

def createQuizBox(master,x,y,bg_color,Quiz,NumQuestoes,command,width=None,height=None):
    
    if Quiz != None:
        Nome = Quiz.get_nome()
        Autor =Quiz.get_autor()
        Categoria =Quiz.get_categoria()

    else:
        Nome = None
        Autor = None
        Categoria = None

    canvas = ctk.CTkCanvas(master, background=bg_color, width=269+18, height=298+15, highlightthickness=0)
    canvas.place(x=x,y=y)

    canvas.create_rectangle(18,0,18+269,298, fill=lightGray2, outline=lightGray2)
    canvas.create_rectangle(0,15,269,15+298, fill=lightGray, outline=lightGray)
    x=10
    y=15
    
    tittle=ctk.CTkLabel(canvas, text=f"{Nome}", font=(
                "Roboto", 42, "bold"), bg_color=lightGray, text_color=black, fg_color=lightGray)
    tittle.place(x=x,y=y+30)
    autor=ctk.CTkLabel(canvas, text=f"Autor: {Autor}", font=(
    "Roboto", 20, "bold"), bg_color=lightGray, text_color=black, fg_color=lightGray)
    autor.place(x=x,y=y+90)
    Categoria=ctk.CTkLabel(canvas, text=f"{Categoria}", font=(
                "Roboto", 20, "bold"), bg_color=lightGray, text_color=black, fg_color=lightGray)
    Categoria.place(x=x,y=y+130)
    NQuestoes=ctk.CTkLabel(canvas, text=f"N° de Questões: {NumQuestoes}", font=(
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
            hover_color=hoverColor,
            corner_radius=360
    )
    ButtonJogar.place(x=269/2-100, y=298+15-62)

    if width !=None and height !=None:
        canvas.configure(width=width,height=height)

    return  tittle,autor,Categoria,NQuestoes,ButtonJogar