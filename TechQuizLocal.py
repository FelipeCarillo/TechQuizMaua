from Local.Codigo.LoginWindow import LoginMainScreen
from Local.Codigo.ScreenFirstTime import ScreenFrstTime
from Local.Codigo.MenuWindow import MainScreen
from Local.Codigo.AdminWindow import AdminMainScreen

def main():
    # Criar a tela de login e iniciar o loop principal
    login_screen = LoginMainScreen()
    login_screen.mainloop()

    try:
    # Obter informações de login do usuário
        Usuario = login_screen.get_Account()

        if Usuario.getCargo() == 1:
            # Tela de Admin
            admin_screen = AdminMainScreen(Usuario)
            admin_screen.mainloop()
        else:
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
