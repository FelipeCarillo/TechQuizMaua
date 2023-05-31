import customtkinter as ctk
from Codes.Login import startGame 
from Codes.ScreenFirstTime import ScreenFrstTime
from Codes.Menu import menu
from Codes.Account import Account

User=startGame()
User = Account(User[0],User[1],User[2],User[3])

if User.firstLogin == 1:
    ScreenFrstTime(User.atribute,User.user)

# menu()







