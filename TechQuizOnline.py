from Online.Codigo.LoginWindow import LoginMainScreen
from Online.Codigo.ScreenFirstTime import ScreenFrstTime
from Online.Codigo.MenuWindow import MainScreen

def main():
    # Criar a tela de login e iniciar o loop principal
    login_screen = LoginMainScreen()
    login_screen.mainloop()

    try:
        # Obter informações de login do usuário
        Usuario = login_screen.get_Account()

        if Usuario.getFirstLogin() == 1 and Usuario.getCargo() == 3:
            # Abrir a tela de primeira vez
            first_time_screen = ScreenFrstTime(Usuario)
            first_time_screen.mainloop()

        # Abrir a tela principal
        main_screen = MainScreen(Usuario)
        main_screen.mainloop()
    except:
        pass

if __name__ == '__main__':
    main()    
