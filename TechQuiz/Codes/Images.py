from PIL import Image, ImageTk


def loadImage(path, resize=None):
    if resize != None:
        return ImageTk.PhotoImage(Image.open(path).resize(resize))
    else:
        return ImageTk.PhotoImage(Image.open(path))


def ImageLogo(resize=None):
    if resize != None:
        return loadImage("Imagens\LOGO.png", resize)
    else:
        return loadImage("Imagens\LOGO.png")


def ImageInformation(resize=None):
    if resize != None:
        return loadImage("Imagens\Information.png", resize)
    else:
        return loadImage("Imagens\Information.png")


def ImageCheckEdit(resize=None):
    if resize != None:
        return loadImage("Imagens\check.png", resize)
    else:
        return loadImage("Imagens\check.png")


def ImageEdit(resize=None):
    if resize != None:
        return loadImage("Imagens/EDIT.png", resize)
    else:
        return loadImage("Imagens\EDIT.png")


def ImageRnkgLogo(resize=None):
    if resize != None:
        return loadImage("Imagens/RANKING.png", resize)
    else:
        return loadImage("Imagens\RANKING.png")


def ImageLogoNEscrita(resize=None):
    if resize != None:
        return loadImage("Imagens\LOGO_N_Escrita.png", resize)
    else:
        return loadImage("Imagens\LOGO_N_Escrita.png")
