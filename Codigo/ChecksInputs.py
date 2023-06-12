import re

validacao_email = r'^\w+[@]\w+[.]\w{2,3}(\.\w+)?$'

estruturaRA = r'^[0-9]+[.][0-9]+[-][0-9]+$'
estruturaMatricula = r'^[0-9]+$'

estruturaUsername = r'^[a-zA-Z0-9]+$'

def check_user_operation(username):
    
    hasEspecial= any(
            caracteres for caracteres in username if not caracteres.isalnum())
    hasLetter= any(
            caracteres for caracteres in username if caracteres.isalpha())
    
    if len(username)>40 or len(username)<4 or hasEspecial and not hasLetter:
        return False
    else:
        return True

def check_email_operation(email):

    validacao_email = re.search(validacao_email,email)

    if not validacao_email or len(email)>100:
        return False
    else:
        return True


def check_password_operation(passwd):

    hasNumber = any(caracteres.isnumeric() for caracteres in passwd)
    hasLetters = any(caracteres.isalpha() for caracteres in passwd)
    hasUPLetters = any(caracteres.isupper() for caracteres in passwd)
    hasSpecials = any(
            caracteres for caracteres in passwd if not caracteres.isalnum())

    if hasNumber and hasLetters and hasSpecials and hasUPLetters and len(passwd)<=40:
        return True
    else:
        return False
        

def check_RA_operation(RA):

    val_estruturaRA = re.search(estruturaRA,RA)
    tamanhoRA = len(RA)
    
    if not val_estruturaRA or tamanhoRA != 10:
        return False
    else:
        return True
         

def check_Matricula_operation(Matricula):

    val_estruturaMatricula = re.search(estruturaMatricula,Matricula)
    tamanhoMatricula = len(Matricula)
    
    if not val_estruturaMatricula or tamanhoMatricula != 5:
        return False
    else:
        return True
    

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
    