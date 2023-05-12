from Login import startGame 
from ScreenFirstTime import ScreenFrstTime
from MainScreen import MainScreen
from MenuClass import *

Usuario, Continues = startGame()

if Continues == True:
    while True:
        if Usuario.getFirstLogin() == 1 and Usuario.getCargo() == 3:
            FirstLogin, Curso, Ano = ScreenFrstTime(Usuario.getIdUsuario())
            Usuario.setFirstLogin(FirstLogin)
            Usuario.setCurso(Curso)
            Usuario.setAno(Ano)
        else:
            break
    MainScreen(Menu,Usuario).mainloop()

    







