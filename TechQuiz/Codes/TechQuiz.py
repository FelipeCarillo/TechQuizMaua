from Login import startGame 
from ScreenFirstTime import ScreenFrstTime
from Menu import Menu
from Account import Account

Usuario = startGame()

while True:
    print(Usuario.getFirstLogin(), Usuario.getCurso())
    if Usuario.getFirstLogin() == 1 and Usuario.getCargo() == 3:
        FirstLogin, Curso, Ano = ScreenFrstTime(Usuario.getIdUsuario())
        Usuario.setFirstLogin(FirstLogin)
        Usuario.setCurso(Curso)
        Usuario.setAno(Ano)
    else:
        break
Menu(Usuario)







