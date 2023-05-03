from PIL import Image, ImageTk


def Logo():
    imageLogo = Image.open("Imagens\LOGO.png")
    imageLogo = ImageTk.PhotoImage(imageLogo)
    return imageLogo