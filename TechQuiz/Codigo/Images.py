from PIL import Image
from customtkinter import CTkImage

def loadImage(path, resize=None):
    if resize != None:
        return CTkImage(Image.open(path),size=resize)
    else:
        return CTkImage(Image.open(path))

def ImageLogo(resize=None):
    path = "TechQuizMaua\TechQuiz\imagens\LOGO.png"
    return loadImage(path, resize)

def ImageExcel(resize=None):
    path = "TechQuizMaua\TechQuiz\imagens\logoExcel.png"
    return loadImage(path, resize)

def ImageInformation(resize=None):
    path = "TechQuizMaua\TechQuiz\imagens\Information.png"
    return loadImage(path, resize)

def ImageCheckEdit(resize=None):
    path = "TechQuizMaua\TechQuiz\imagens\check.png"
    return loadImage(path, resize)

def ImageEdit(resize=None):
    path = "TechQuizMaua\TechQuiz\imagens\EDIT.png"
    return loadImage(path, resize)

def ImageRnkgLogo(resize=None):
    path = "TechQuizMaua\TechQuiz\imagens\RANKING.png"
    return loadImage(path, resize)

def ImageLogoNEscrita(resize=None):
    path = "TechQuizMaua\TechQuiz\imagens\LogoSemEscrita.png"
    return loadImage(path, resize)

def ImageGoBack(resize=None):
    path = "TechQuizMaua\TechQuiz\imagens\Back.png"
    return loadImage(path, resize)

def ImageLupa(resize=None):
    path = "TechQuizMaua\TechQuiz\imagens\lupa.PNG"
    return loadImage(path, resize)

def ImageGoFoward(resize=None):
    path = "TechQuizMaua\TechQuiz\imagens\Foward.PNG"
    return loadImage(path, resize)
