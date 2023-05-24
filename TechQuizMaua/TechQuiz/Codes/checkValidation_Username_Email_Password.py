import re

validacao_com_razao = '\w+[@]\w+[.]\w{2,3}$'
validacao_com_br_razao = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}\w+[.]\w{2,3}$'


estruturaRA = '^[0-9]+[.][0-9]+[-][0-9]'
estruturaMatricula = '^[0-9]'

def check_user_operation(username):
    if len(username)>30 or len(username)<4:
        return False
       

def check_email_operation(email):

    validacao_com = re.search(validacao_com_razao, email)
    validacao_com_br = re.search(validacao_com_br_razao, email)
    if not validacao_com and not validacao_com_br:
        return False


def check_password_operation(passwd):
    
    verification = []

    hasNumber = any(caracteres.isnumeric() for caracteres in passwd)
    hasLetters = any(caracteres.isalpha() for caracteres in passwd)
    hasUPLetters = any(caracteres.isupper() for caracteres in passwd)
    hasSpecials = any(
            caracteres for caracteres in passwd if not caracteres.isalnum())

    if hasNumber and hasLetters and hasSpecials and hasUPLetters:
        return True
    else:
        return False
        

def check_RA_operation(RA):

    val_estruturaRA = re.search(estruturaRA,RA)
    tamanhoRA = len(RA)
    
    if not val_estruturaRA or tamanhoRA != 10:
        return False
         

def check_Matricula_operation(Matricula):

    val_estruturaMatricula = re.search(estruturaMatricula,Matricula)
    tamanhoMatricula = len(Matricula)
    
    if not val_estruturaMatricula or tamanhoMatricula != 5:
        return False
    

def indentificador(dado):

    val_estruturaRA = re.search(estruturaRA,dado)
    val_estruturaMatricula = re.search(estruturaMatricula,dado)

    isUsername=1
    isMatricula=2
    isRA=3
    

    if val_estruturaRA:
        return isRA
    
    elif val_estruturaMatricula:
        return isMatricula

    else:
        return isUsername 
    