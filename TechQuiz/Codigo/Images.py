from PIL import Image
from customtkinter import CTkImage

def loadImage(path, resize=None):
    if resize != None:
        return CTkImage(Image.open(path),size=resize)
    else:
        return CTkImage(Image.open(path))

def ImageLogo(resize=None):
    path = "Imagens/LOGO.png"
    return loadImage(path, resize)

def ImageExcel(resize=None):
    path = "Imagens/logoExcel.png"
    return loadImage(path, resize)

def ImageInformation(resize=None):
    path = "Imagens/Information.png"
    return loadImage(path, resize)

def ImageCheckEdit(resize=None):
    path = "Imagens/check.png"
    return loadImage(path, resize)

def ImageEdit(resize=None):
    path = "Imagens/EDIT.png"
    return loadImage(path, resize)

def ImageRnkgLogo(resize=None):
    path = "Imagens/RANKING.png"
    return loadImage(path, resize)

def ImageLogoNEscrita(resize=None):
    path = "Imagens/LogoSemEscrita.png"
    return loadImage(path, resize)

def ImageGoBack(resize=None):
    path = "Imagens/Back.png"
    return loadImage(path, resize)

def ImageLupa(resize=None):
    path = "Imagens/lupa.PNG"
    return loadImage(path, resize)

def ImageGoFoward(resize=None):
    path = "Imagens/Foward.PNG"
    return loadImage(path, resize)