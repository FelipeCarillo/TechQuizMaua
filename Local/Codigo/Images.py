from PIL import Image
from customtkinter import CTkImage

def loadImage(file, resize=None):
    path = f"Imagens/{file}"
    if resize != None:
        return CTkImage(Image.open(path),size=resize)
    else:
        return CTkImage(Image.open(path))

def ImageLogo(resize=None):
    file = "LOGO.png"
    return loadImage(file, resize)

def ImageExcel(resize=None):
    file = "logoExcel.png"
    return loadImage(file, resize)

def ImageInformation(resize=None):
    file = "Information.png"
    return loadImage(file, resize)

def ImageCheckEdit(resize=None):
    file = "check.png"
    return loadImage(file, resize)

def ImageEdit(resize=None):
    file = "EDIT.png"
    return loadImage(file, resize)

def ImageRnkgLogo(resize=None):
    file = "RANKING.png"
    return loadImage(file, resize)

def ImageLogoNEscrita(resize=None):
    file = "LogoSemEscrita.png"
    return loadImage(file, resize)

def ImageGoBack(resize=None):
    file = "Back.png"
    return loadImage(file, resize)

def ImageLupa(resize=None):
    file = "lupa.PNG"
    return loadImage(file, resize)

def ImageGoFoward(resize=None):
    file = "Foward.PNG"
    return loadImage(file, resize)

def ImageDataBase(resize=None):
    file = "DataBase.png"
    return loadImage(file, resize)