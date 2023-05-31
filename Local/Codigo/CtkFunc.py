import customtkinter as ctk
from Local.Codigo.Colors import lightGray,black,mainBlue,lightGray2,hoverColor

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
                "Roboto", 42, "bold"), bg_color=lightGray, text_color=black, fg_color=lightGray, wraplength= 269, justify='left'
                )
    y+=30
    tittle.place(x=x,y=y)
    autor=ctk.CTkLabel(canvas, text=f"Autor: {Autor}", font=(
    "Roboto", 18, "bold"), bg_color=lightGray, text_color=black, fg_color=lightGray, wraplength= 269, justify='left')
    y+=60
    autor.place(x=x,y=y)
    Categoria=ctk.CTkLabel(canvas, text=f"{Categoria}", font=(
                "Roboto", 18, "bold"), bg_color=lightGray, text_color=black, fg_color=lightGray, wraplength= 269, justify='left')
    y+=50
    Categoria.place(x=x,y=y)
    NQuestoes=ctk.CTkLabel(canvas, text=f"N° de Questões: {NumQuestoes}", font=(
                "Roboto", 18, "bold"), bg_color=lightGray, text_color=black, fg_color=lightGray)
    y+=50
    NQuestoes.place(x=x,y=y)

    
    ButtonJogar = ctk.CTkButton(
        master=canvas,
        text='Jogar',
        font=("Roboto", 28, "bold"),
        width=200,
        height=32,
        fg_color=mainBlue,
        bg_color=lightGray,
        hover_color=hoverColor,
        corner_radius=360,
        command=command
    )
    ButtonJogar.place(x=269/2-100, y=298+15-62)
    
    if command == None:
        ButtonJogar.destroy()

    if width !=None and height !=None:
        canvas.configure(width=width,height=height)

    return tittle,autor,Categoria,NQuestoes,ButtonJogar
    
def InfoRnkBox(parent, x, y, username, progress, underline=None):
    ctk.CTkLabel(parent,width=660,height=42,text=None,corner_radius=20,bg_color=lightGray2,fg_color=mainBlue).place(x=x,y=y)
    text = ctk.CTkLabel(parent,text=username,font=("Roboto", 32, "bold"),bg_color=mainBlue,fg_color=mainBlue)
    text.place(x=x+20,y=y+2.5)
    if underline:
        text.configure(font=("Roboto", 32, "bold","underline"))
    else:
        text.configure(font=("Roboto", 32, "bold"))

    ctk.CTkLabel(parent,width=80,text=progress,font=("Roboto", 32, "bold"),bg_color=mainBlue,fg_color=mainBlue,anchor='e').place(x=x+510,y=y+2.5)

def chngQuizBoxData(slctQuiz,varQtdQuestoes,title,autor,categoria,nquestoes,buttonjogar,searchButton):
    title.configure(text=slctQuiz.get_nome())
    autor.configure(text=f"Autor: {slctQuiz.get_autor()}")
    categoria.configure(text=slctQuiz.get_categoria())
    nquestoes.configure(text=f'N° de Questões: {varQtdQuestoes}')
    if buttonjogar != None:
        buttonjogar.configure(state='enable')
        searchButton.configure(state='enable')
        searchButton.configure(state='enable')