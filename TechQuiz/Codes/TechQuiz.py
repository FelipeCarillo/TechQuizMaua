from Inicialize import LoginMainScreen 
from ScreenFirstTime import ScreenFrstTime
from MainScreen import MainScreen
from QuizScreen import QuizScreen

LoginMainScreen().mainloop()
Usuario = LoginMainScreen.get_Account(self=LoginMainScreen())

if Usuario:
    if Usuario.getFirstLogin() == 1 and Usuario.getCargo() == 3:
        ScreenFrstTime(Usuario)
    Menu = MainScreen(Usuario)
    Menu.mainloop()
    Quiz = Menu.getQuiz(self=MainScreen)
    if Quiz:
        QuizScreen(Usuario,Quiz).mainloop()
    else:
        MainScreen(Usuario).mainloop()


    
 






