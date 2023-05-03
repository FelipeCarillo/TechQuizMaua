import customtkinter as ctk
from PIL import Image, ImageTk
import ctypes
import checkValidation_Username_Email_Password as check
import DataBase as con
from ScreenFirstTime import ScreenFrstTime
from Images import Logo
# from Menu import menu
Account = None

def startGame():

    monitorScale = ctypes.windll.shcore.GetScaleFactorForDevice(0)

    Window = ctk.CTk()
    def Interface_Aviso_Escala():

        text = ctk.CTkTextbox(Window, height=300, width=400)
        text.insert(
            ctk.END, text="Mude a escala de seu monitor para 100%.\n\nSiga as intruções:\n\nConfigurações >  Tela  > Escala")
        text.configure(font=(
            "Roboto Mono Regular", 22, "bold"), text_color="black", fg_color="white")
        text.pack()
        Window.mainloop()


    def Interface_Login():
        
        imageLogo = Logo()
    
        imageInformationPasswd = Image.open(
            "Imagens\Information.png").resize([20, 20])
        imageInformationPasswd = ImageTk.PhotoImage(imageInformationPasswd)

        resoluçãoLogin = "1400x850"
        height = 850
        width = 1400

        Window.geometry(resoluçãoLogin)
        Window.config(bg='white')
        # Window.resizable(False, False)
        Window.maxsize(width, height)

        winLogo = ctk.CTkCanvas(
            Window, background="#5271FF", width=955, height=height, highlightthickness=0)
        winLogo.grid(row=0, column=0)
        winLogo.create_image(470, 400, image=imageLogo)

        winRegisters = ctk.CTkCanvas(
            Window, background="#FFFFFF", width=width-955, height=height, highlightthickness=0)
        winRegisters.grid(row=0, column=1)

        def apagarRegisters(master):
            for items in master.place_slaves():
                items.place_forget()
            for items in master.find_all():
                master.delete(items)

        def createTextInput(master, message, msgX, msgY, inpX, inpY):
            Title = ctk.CTkLabel(master, text=message, font=(
                "Roboto Mono Regular", 18, "bold"), bg_color="#FFFFFF", text_color="#5271FF")
            Title.place(x=msgX, y=msgY)

            entry = ctk.CTkEntry(winRegisters, font=("Roboto Mono Regular", 18), width=397.5,
                                    height=42, bg_color="#FFFFFF", fg_color="#FFFFFF", border_color="#D9D9D9", text_color="#000000", border_width=3)
            entry.place(x=inpX, y=inpY)

            return entry

        def createButtonInput(master, width, height, x, y, command, text):
            loginButton = ctk.CTkButton(master, width=width, height=height, text=text, font=(
                "Roboto Mono Regular", 18, "bold"), corner_radius=6, text_color="#FFFFFF", fg_color="#5271FF", bg_color="#FFFFFF", hover_color="#004AAD", command=command)
            loginButton.place(x=x, y=y)


        def createLabel(master, text, x, y, tmhFont):
            Text = ctk.CTkLabel(master, text=text, font=(
                "Roboto Mono Regular", tmhFont, "bold"), bg_color="#FFFFFF", text_color="#5271FF")
            Text.place(x=x, y=y)

        def showPsswdButton(command, show_Passwd, x, y):
            buttonShowPasswd = ctk.CTkCheckBox(winRegisters, text="Mostar senha", width=20, height=20, fg_color="#5271FF",
                                            bg_color="#FFFFFF", hover_color="#FFFFFF", variable=show_Passwd, onvalue=True, offvalue=False, text_color="#5271FF", command=command)
            buttonShowPasswd.place(x=x, y=y)

        def Login():
            Window.title("LOGIN")
            apagarRegisters(winRegisters)

            rect = winRegisters.create_rectangle(0, 167, 445, 164,
                                                fill="#D9D9D9", outline=winRegisters.cget('bg'))

            createLabel(winRegisters, "LOGIN", 155, 38.2, 42)
            createLabel(winRegisters, "Efetue o login para continuar", 80, 90, 22)

            # Login
            textUser = 'USERNAME / RA / MATRÍCULA'
            inputUser = createTextInput(
                winRegisters, textUser, 23.7, 207, 23.7, 242)

            # Senha
            textPasswd = 'PASSWORD'
            inputPasswd = createTextInput(
                winRegisters, textPasswd, 23.7, 315, 23.7, 350)
            inputPasswd.configure(show="*")

        # Botões
            

            def registrarLogin():
                global Account
                def msgError():
                    textError = ctk.CTkLabel(winRegisters, text="⚠️\nUsername / RA / Matrícula ou a Senha está inválido.", font=(
                        "Roboto Mono Regular", 16, "bold"), text_color="#E10E0E", bg_color="white")
                    textError.place(x=25, y=550)

                userLogin = inputUser.get()
                item = check.indentificador(userLogin)
                
                if item == 1:
                            item = 'nomeUser'
                else:
                            item = 'registroUser'

                Dados = con.getLogin(item, userLogin)
                senha = Dados[0]
                firstLogin = Dados[1]
                passwdLogin = inputPasswd.get()

                if senha == passwdLogin:
                    Account=[item, userLogin, senha, firstLogin]
                    Window.destroy()

                else:
                    msgError()

            buttonLogin = ctk.CTkButton(winRegisters, width=180, height=52, text="LOGIN", font=(
                "Roboto Mono Regular", 18, "bold"), corner_radius=6, text_color="#FFFFFF", fg_color="#5271FF", bg_color="#FFFFFF", hover_color="#004AAD", command=registrarLogin)
            buttonLogin.place(x=241.2, y=450)
            
            
            buttonSignup = createButtonInput(
                winRegisters, 180, 52, 23.7, 450, SignUp, "SIGNUP")

        # Check Mostrar Senha
            show_Passwd = ctk.BooleanVar()

            def showPasswd():
                if show_Passwd.get():
                    inputPasswd.configure(show="")
                else:
                    inputPasswd.configure(show="*")
            showPsswdButton(showPasswd, show_Passwd, 23.7, 402.7)  
            

    # Interface de Cadastro
        def SignUp():
            Window.title("SIGNUP")
            apagarRegisters(winRegisters)

            inputUser = 0
            inputRegistro = 0
            inputEmail = 0
            inputPasswd = 0
            inputConfirmPasswd = 0

            rect = winRegisters.create_rectangle(0, 148, 445, 145,
                                                fill="#D9D9D9", outline=winRegisters.cget('bg'))

            createLabel(winRegisters, "SignUp", 155, 38.2, 42)
            createLabel(winRegisters, "Efetue o SignUp para continuar", 80, 90, 22)

            inputUser = createTextInput(
                winRegisters, "USERNAME", 23.7, 169.4, 23.7, 200.9)
            inputRegistro = createTextInput(
                winRegisters, "RA / MATRÍCULA", 23.7, 257.6, 23.7, 288.8)
            inputRegistro.configure(placeholder_text="XX.XXXXX-X ou XXXXX")
            inputEmail = createTextInput(
                winRegisters, "EMAIL", 23.7, 345.5, 23.7, 376.7)
            inputPasswd = createTextInput(
                winRegisters, "PASSWORD", 23.7, 436.4, 23.7, 464.6)
            inputPasswd.configure(show="*")
            inputConfirmPasswd = createTextInput(
                winRegisters, "CONFIRM PASSWORD", 23.7, 522.5, 23.7, 553.7)
            inputConfirmPasswd.configure(show="*")

            def registrarLogin():
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

                nome, continues = operacao(
                    check.check_user_operation(nome), nome, inputUser, "Usuário Inválido.")
                isDadosCorretos.append(continues)
                continues = con.duplicated('nomeUser', nome)
                isDadosCorretos.append(continues)
                if continues == False:
                    operacao(False, 0, inputUser, "Usuário Inválido.")

                item = check.indentificador(registro)

                if item == 3:
                    registro, continues = operacao(check.check_RA_operation(
                        registro), registro, inputRegistro, "RA Inválido.")
                    isDadosCorretos.append(continues)
                    continues = con.duplicated('registroUser', registro)
                    isDadosCorretos.append(continues)
                    if continues == False:
                        operacao(False, 0, inputRegistro, "RA Inválido.")
                    cargo = 3

                elif item == 2:
                    registro, continues = operacao(check.check_Matricula_operation(
                        registro), registro, inputRegistro, "Matrícula Inválida.")
                    isDadosCorretos.append(continues)
                    continues = con.duplicated('registroUser', registro)
                    isDadosCorretos.append(continues)
                    if continues == False:
                        operacao(False, 0, inputRegistro, "Matrícula Inválida.")
                    cargo = 2

                email, continues = operacao(check.check_email_operation(
                    email), email, inputEmail, "Email Inválido.")
                isDadosCorretos.append(continues)
                continues = con.duplicated('emailUser', email)
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
                    Login()

            buttonSignup = createButtonInput(
                winRegisters, 180, 52, 23.7, 646.8, registrarLogin, "CADASTRAR")
            buttonLogin = createButtonInput(
                winRegisters, 180, 52, 241.2, 646.8, Login, "VOLTAR")

            show_Passwd = ctk.BooleanVar()

            def showPasswd():
                if show_Passwd.get():
                    inputPasswd.configure(show="")
                    inputConfirmPasswd.configure(show="")
                else:
                    inputPasswd.configure(show="*")
                    inputConfirmPasswd.configure(show="*")
            showPsswdButton(showPasswd, show_Passwd, 23.7, 605)

            def showIftnPasswd():
                textIftnPasswd = "{}\n{}\n{}\n{}\n{}\n{}".format("SENHA DEVE TER:", "- No mínimo 8 e no máximo 40 caracteres.",
                                                                "- No mínimo uma letra MAIÚSCULA.", "- No mínimo um caractere especial.", "- No mínimo uma letra.", "- No mínimo um número.")
                ifceIffnPasswd = ctk.CTkButton(master=winRegisters, text=textIftnPasswd, font=(
                    "Roboto Mono Regular", 15, "bold"), text_color="#FFFFFF", fg_color="#5271FF", bg_color="#FFFFFF", hover=False, command=lambda: ifceIffnPasswd.destroy())
                ifceIffnPasswd.place(x=60, y=470)

            buttonIftnPasswd = ctk.CTkButton(
                master=winRegisters, image=imageInformationPasswd, text="", fg_color="#FFFFFF", bg_color="#FFFFFF", width=20, height=20, hover=False, command=showIftnPasswd)
            buttonIftnPasswd.place(x=390, y=436.4)

        Login()
        Window.mainloop()
        
    if monitorScale == 100:
        Interface_Login()
        return Account
    else:
        Interface_Aviso_Escala()

