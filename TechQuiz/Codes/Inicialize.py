import customtkinter as ctk
import ctypes
import checkValidation_Username_Email_Password as check
import DataBase as con
from Images import ImageLogo, ImageInformation
from Account import Account
from Colors import *

def createTextInput(master, message, msgX, msgY, inpX, inpY):
    title = ctk.CTkLabel(master, text=message, font=(
                "Roboto Mono Regular", 18, "bold"), bg_color="#FFFFFF", text_color="#5271FF")
    title.place(x=msgX, y=msgY)
    entry = ctk.CTkEntry(master, font=("Roboto Mono Regular", 18), width=397.5,
                                    height=42, bg_color="#FFFFFF", fg_color="#FFFFFF", border_color="#D9D9D9", text_color="#000000", border_width=3)
    entry.place(x=inpX, y=inpY)
    return entry

def createButtonInput(master, width, height, x, y, command, text):
    
    loginButton = ctk.CTkButton(master, width=width, height=height, text=text, font=(
                "Roboto Mono Regular", 18, "bold"), corner_radius=6, text_color="#FFFFFF", fg_color="#5271FF", bg_color="#FFFFFF", hover_color="#004AAD", command=command)
    loginButton.place(x=x, y=y)
    return loginButton


def createLabel(master, text, x, y, tmhFont):
    Text = ctk.CTkLabel(master, text=text, font=(
                "Roboto Mono Regular", tmhFont, "bold"), bg_color="#FFFFFF", text_color="#5271FF")
    Text.place(x=x, y=y)

def showPsswdButton(master,command, show_Passwd, x, y):
    buttonShowPasswd = ctk.CTkCheckBox(master, text="Mostar senha", width=20, height=20, fg_color="#5271FF",
                                            bg_color="#FFFFFF", hover_color="#FFFFFF", variable=show_Passwd, onvalue=True, offvalue=False, text_color="#5271FF", command=command)
    buttonShowPasswd.place(x=x, y=y)


class LoginMainScreen(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        monitorScale = ctypes.windll.shcore.GetScaleFactorForDevice(0)

        imagelogo = ImageLogo([500,500])

        resoluçãoLogin = "1400x850"
        height = 850
        width = 1400

        self.geometry(resoluçãoLogin)
        self.config(bg=white)
        self.maxsize(width, height)

        winLogo = ctk.CTkCanvas(
            self, background=mainBlue, width=955, height=height, highlightthickness=0)
        winLogo.grid(row=0, column=0)
        ctk.CTkButton(winLogo, image=imagelogo,bg_color=mainBlue,fg_color=mainBlue,state='disabled',text=None).place(x=200,y=150)
        
        winRegisters = ctk.CTkCanvas(
            self, background=white, width=width-955, height=height, highlightthickness=0)
        winRegisters.grid(row=0, column=1)
        if monitorScale == 100:
            self.myframe = Login(self,winRegisters)
        else:
            self.myframe = Itfc_Warning_Escala(self)
        
    def get_Account(self):
        return self.Account
    
    def set_Account(self,Account):
        self.Account = Account

    def set_Frame(self, frame):
        self.myframe=frame
        

class Itfc_Warning_Escala(ctk.CTkFrame):
    def __init__(self,parent):
        for items in parent.grid_slaves():
            items.grid_forget()
        parent.geometry("400x200")
        parent.title('TechQuiz - Aviso')
        text = ctk.CTkTextbox(parent, height=300, width=400)
        text.insert(
                ctk.END, text="Mude a escala de seu monitor para 100%.\n\nSiga as intruções:\n\nConfigurações >  Tela  > Escala")
        text.configure(font=(
                "Roboto Mono Regular", 22, "bold"), text_color="black", fg_color="white")
        text.pack()


class Login(ctk.CTkFrame):
    def __init__(self,parent,grid):            
        parent.title("LOGIN")
        # apagarRegisters()

        grid.create_rectangle(0, 167, 445, 164,
            fill="#D9D9D9", outline=grid.cget('bg'))

        
        createLabel(grid, "LOGIN", 155, 38.2, 42)
        createLabel(grid, "Efetue o login para continuar", 80, 90, 22)

            # Login
        textUser = 'USERNAME / RA / MATRÍCULA'
        inputUser = createTextInput(
        grid, textUser, 23.7, 207, 23.7, 242)

            # Senha
        textPasswd = 'PASSWORD'
        inputPasswd = createTextInput(
            grid, textPasswd, 23.7, 315, 23.7, 350)
        inputPasswd.configure(show="*")

        # Botões
        def registrarLogin():
            buttonLogin.configure(state='disable')
            def msgError():
                    textError = ctk.CTkLabel(grid, text="⚠️\nUsername / RA / Matrícula ou a Senha está inválido.", font=(
                        "Roboto Mono Regular", 16, "bold"), text_color="#E10E0E", bg_color="white")
                    textError.place(x=25, y=550)

            userLogin = inputUser.get()
            idCargo = check.indentificador(userLogin)
            try:
                try:
                    if idCargo == 1:
                        atribute = 'nomeUser'
                    else:
                        atribute = 'registroUser'
                    Dados = con.getLogin(atribute, userLogin)
                    senha = Dados[0]
                    passwdLogin = inputPasswd.get()

                    if senha == passwdLogin:
                        data = con.getSigma('usuario', atribute, userLogin)
                        LoginMainScreen.set_Account(LoginMainScreen,Account(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[9],data[8]))
                        parent.destroy()
                except:
                    msgError()
            except:
                buttonLogin.configure(state='enable')

        buttonLogin = ctk.CTkButton(grid, width=180, height=52, text="LOGIN", font=(
                "Roboto Mono Regular", 18, "bold"), corner_radius=6, text_color="#FFFFFF", fg_color="#5271FF", bg_color="#FFFFFF", hover_color="#004AAD", command=registrarLogin)
        buttonLogin.place(x=241.2, y=450)
        
        def apagarRegisters():
            for items in grid.find_all():
                grid.delete(items)
            for items in grid.place_slaves():
                items.place_forget()
        
        def GoSignUp():
            apagarRegisters()
            LoginMainScreen.set_Frame(self=LoginMainScreen,frame=SignUp(parent,grid))

        buttonSignup = createButtonInput(
        grid, 180, 52, 23.7, 450, GoSignUp, "SIGNUP")

        # Check Mostrar Senha
        show_Passwd = ctk.BooleanVar()

        def showPasswd():
            if show_Passwd.get():
                inputPasswd.configure(show="")
            else:
                inputPasswd.configure(show="*")
        showPsswdButton(grid,showPasswd, show_Passwd, 23.7, 402.7)

class SignUp(ctk.CTkFrame):
    # Interface de Cadastro
    def __init__(self, parent,grid):
        def apagarRegisters():
            for items in grid.find_all():
                grid.delete(items)
            for items in grid.place_slaves():
                items.place_forget()

        parent.title("SIGNUP")

        imageInformationPasswd = ImageInformation([20, 20])

        inputUser = 0
        inputRegistro = 0
        inputEmail = 0
        inputPasswd = 0
        inputConfirmPasswd = 0

        grid.create_rectangle(0, 148, 445, 145,
                                            fill="#D9D9D9", outline=grid.cget('bg'))
        createLabel(grid, "SignUp", 155, 38.2, 42)
        createLabel(grid, "Efetue o SignUp para continuar", 80, 90, 22)
        inputUser = createTextInput(
            grid, "USERNAME", 23.7, 169.4, 23.7, 200.9)
        inputRegistro = createTextInput(
            grid, "RA / MATRÍCULA", 23.7, 257.6, 23.7, 288.8)
        inputRegistro.configure(placeholder_text="XX.XXXXX-X ou XXXXX")
        inputEmail = createTextInput(
            grid, "EMAIL", 23.7, 345.5, 23.7, 376.7)
        inputPasswd = createTextInput(
            grid, "PASSWORD", 23.7, 436.4, 23.7, 464.6)
        inputPasswd.configure(show="*")
        inputConfirmPasswd = createTextInput(
            grid, "CONFIRM PASSWORD", 23.7, 522.5, 23.7, 553.7)
        inputConfirmPasswd.configure(show="*")
        
        def GoLogin():
            apagarRegisters()
            LoginMainScreen.set_Frame(self=LoginMainScreen,frame=Login(parent,grid))
        def registrarLogin():
            buttonSignup.configure(state='disable')
            nome = inputUser.get()
            registro = inputRegistro.get()
            email = inputEmail.get()
            senha = inputPasswd.get()
            confirmacaoSenha = inputConfirmPasswd.get()
            cargo = 0
            def operacao(entrada, dado, entry, textError):
                checagem = entrada
                if checagem == False:
                    entry.delete(0, 100)
                    entry.configure(placeholder_text=f"⚠️ {textError}")
                    return dado, False
                else:
                    return dado, True
            isDadosCorretos = []
            try:
                nome, continues = operacao(
                    check.check_user_operation(nome), nome, inputUser, "Usuário Inválido.")
                isDadosCorretos.append(continues)
                continues = con.hasDuplicated('nomeUser', nome)
                isDadosCorretos.append(continues)
                if continues == False:
                    operacao(False, 0, inputUser, "Usuário Inválido.")
                item = check.indentificador(registro)
                if item == 3:
                    registro, continues = operacao(check.check_RA_operation(
                        registro), registro, inputRegistro, "RA Inválido.")
                    isDadosCorretos.append(continues)
                    continues = con.hasDuplicated('registroUser', registro)
                    isDadosCorretos.append(continues)
                    if continues == False:
                        operacao(False, 0, inputRegistro, "RA Inválido.")
                    cargo = 3
                elif item == 2:
                    registro, continues = operacao(check.check_Matricula_operation(
                        registro), registro, inputRegistro, "Matrícula Inválida.")
                    isDadosCorretos.append(continues)
                    continues = con.hasDuplicated('registroUser', registro)
                    isDadosCorretos.append(continues)
                    if continues == False:
                        operacao(False, 0, inputRegistro, "Matrícula Inválida.")
                    cargo = 2
                email, continues = operacao(check.check_email_operation(
                    email), email, inputEmail, "Email Inválido.")
                isDadosCorretos.append(continues)
                continues = con.hasDuplicated('emailUser', email)
                isDadosCorretos.append(continues)
                if continues == False:
                    operacao(False, 0, inputEmail, "Email Inválido.")
                senha, continues = operacao(check.check_password_operation(
                    senha), senha, inputPasswd, "Senha Inválida.")
                isDadosCorretos.append(continues)
                if confirmacaoSenha == senha:
                    continues = True
                else:
                    continues = False
                    inputConfirmPasswd.delete(0, 100)
                    inputConfirmPasswd.configure(
                        placeholder_text="⚠️ Senha não é a mesma.")
                isDadosCorretos.append(continues)
                if False not in isDadosCorretos:
                    con.cadastrarDados(registro, nome, senha, email, str(cargo))
                    GoLogin()
            except:
                buttonSignup.configure(state='enable')
        buttonSignup = createButtonInput(
            grid, 180, 52, 23.7, 646.8, registrarLogin, "CADASTRAR")
        
        buttonLogin = createButtonInput(
            grid, 180, 52, 241.2, 646.8, GoLogin, "VOLTAR")
        show_Passwd = ctk.BooleanVar()
        def showPasswd():
            if show_Passwd.get():
                inputPasswd.configure(show="")
                inputConfirmPasswd.configure(show="")
            else:
                inputPasswd.configure(show="*")
                inputConfirmPasswd.configure(show="*")
        showPsswdButton(grid,showPasswd, show_Passwd, 23.7, 605)
        def showIftnPasswd():
            textIftnPasswd = "{}\n{}\n{}\n{}\n{}\n{}".format("SENHA DEVE TER:", "- No mínimo 8 e no máximo 40 caracteres.",
                                                            "- No mínimo uma letra MAIÚSCULA.", "- No mínimo um caractere especial.", "- No mínimo uma letra.", "- No mínimo um número.")
            ifceIffnPasswd = ctk.CTkButton(master=grid, text=textIftnPasswd, font=(
                "Roboto Mono Regular", 15, "bold"), text_color="#FFFFFF", fg_color="#5271FF", bg_color="#FFFFFF", hover=False, command=lambda: ifceIffnPasswd.destroy())
            ifceIffnPasswd.place(x=60, y=470)
        buttonIftnPasswd = ctk.CTkButton(
            master=grid, image=imageInformationPasswd, text="", fg_color="#FFFFFF", bg_color="#FFFFFF", width=20, height=20, hover=False, command=showIftnPasswd)
        buttonIftnPasswd.place(x=390, y=436.4)
