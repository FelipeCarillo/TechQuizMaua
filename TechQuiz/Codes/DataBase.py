from mysql.connector import connect
from mysql.connector import Error
import pandas as pd
from datetime import datetime

user = "CodeConnection"
password = "TechQuiz2023--"
DataBase = "dbtechquiz"

connection = connect(
    host="localhost",
    user=user,
    passwd=password
)


def setOneData(table, chgAtribute,chgValue, findAtribute, findValue):
    cursor = connection.cursor()
    use_DataBase = f"USE {DataBase}"
    cursor.execute(use_DataBase)

    code = "UPDATE {} SET {} = {} WHERE ({} = %(dado)s)".format(table,chgAtribute, chgValue, findAtribute)
    data = {
        'dado':findValue
    }
    cursor.execute(code,data)

    connection.commit()

def createDataBase():
    cursor = connection.cursor()

    try:
        cursor.execute(f"drop database {DataBase}")
    except:
        pass

    database_TECHQUIZ = f"CREATE DATABASE {DataBase}"
    cursor.execute(database_TECHQUIZ)

    use_DataBase = f"USE {DataBase}"
    cursor.execute(use_DataBase)

    CreateTables = [
        "CREATE TABLE cargo (idCargo INT PRIMARY KEY, nomeCargo VARCHAR(100) NOT NULL)",
        "CREATE TABLE usuario (idUser int auto_increment primary key, registroUser char(11) not null, nomeUser varchar(40) not null, senhaUser varchar(40) not null,emailUser varchar(100) not null, cursoUser varchar(100), anoUser char(2), idCargo int not null, foreign key (idCargo) references cargo(idCargo), datetimeSignup datetime not null, FirstLogin boolean not null default true)",
        "CREATE TABLE categoria_jogo (idCategoria int auto_increment primary key, nomeCategoria varchar(100) not null)",
        "CREATE TABLE jogo (idJogo int auto_increment primary key, nomeJogo varchar(100) not null, idCategoria int not null, foreign key (idCategoria) references categoria_jogo(idCategoria),idUser int not null, foreign key (idUser) references usuario (idUser))",
        "CREATE TABLE progresso_usuario (idProgresso int auto_increment primary key, idJogo int not null, foreign key (idJogo) references jogo(idJogo), idUser int not null, foreign key (idUser) references usuario (idUser), progresso varchar(5) not null default 0)",
        "CREATE TABLE nivel_pergunta(idNivel int auto_increment primary key, nomeNivel varchar(50))",
        "CREATE TABLE perguntas(idPergunta int auto_increment primary key, idJogo int not null, foreign key (idJogo) references jogo(idJogo), Pergunta varchar(500) not null, idNivel int not null, foreign key (idNivel) references nivel_pergunta(idNivel))",
        "CREATE TABLE alternativas(idResposta int auto_increment primary key, idPergunta int not null, foreign key (idPergunta) references perguntas(idPergunta), Alternativa varchar(100) not null, isRight boolean not null)",
    ]

    InsertTables = [
        'INSERT INTO cargo VALUES (1,"Administrador"), (2,"Professor"), (3, "Aluno")',
        'INSERT INTO categoria_jogo values (1,"Lógica de Programação"),(2,"Programação Orientada a Objetos"),(3,"Modelagem Orientada a Objetos"), (4,"Banco de Dados Relacionais")',
        'INSERT INTO nivel_pergunta values (1,"Iniciante"), (2,"Intermediário"), (3,"Avançado")',
    ]

    for command in CreateTables:
        cursor.execute(command)
    for command in InsertTables:
        cursor.execute(command)

    connection.commit()
    

    return DataBase



# Verificar já o dado é duplicado
def duplicated(what, dado):
    cursor = connection.cursor()

    use_DataBase = f"USE {DataBase}"
    cursor.execute(use_DataBase)

    duplicate = "SELECT * FROM usuario WHERE ({} = %(what)s)".format(what)
    values = {"what": dado}
    cursor.execute(duplicate, values)

    hasDuplicate = cursor.fetchone()

    

    if hasDuplicate:
        return False
    
  

def getOneData(target_atribute,table,atribute, data):
    cursor = connection.cursor()

    use_DataBase = f"USE {DataBase}"
    cursor.execute(use_DataBase)

    getPasswd = "SELECT {} FROM {} WHERE ({} = %(data)s)".format(target_atribute, table, atribute)
    values={
        'data':data
    }

    cursor.execute(getPasswd, values)
    target = cursor.fetchone()

    

    return target[0]


# Inserir dados na tabela de login


def cadastrarDados(registroUser, nomeUser, senhaUser, emailUser, idCargo):
    cursor = connection.cursor()

    use_DataBase = f"USE {DataBase}"
    cursor.execute(use_DataBase)

    insertDatas = "INSERT INTO usuario (registroUser, nomeUser, senhaUser, emailUser, idCargo, datetimeSignup) VALUES (%(registro)s, %(nome)s, %(senha)s, %(email)s, %(cargo)s, %(time)s)"

    time = datetime.today()
    time = time.strftime("%Y-%m-%d  %H:%M:%S")

    values = {
        "registro": registroUser,
        "nome": nomeUser,
        "senha": senhaUser,
        "email": emailUser,
        "cargo": idCargo,
        "time": time,
    }

    cursor.execute(insertDatas, values)

    connection.commit()
    

def getSigma(table, atribute, data):
    cursor = connection.cursor()

    use_DataBase = f"USE {DataBase}"
    cursor.execute(use_DataBase)

    Operation_Sigma = "SELECT * FROM {} WHERE ({} = %(data)s)".format(table,atribute)

    values = {
        "data": data
    }

    cursor.execute(Operation_Sigma, values)
    group = cursor.fetchone()

    connection.commit()

    return group
    

# Mostrar dados

# def showDatas(nameTable):
#     showTable = "SELECT * FROM {};".format(nameTable)
#     cursor.execute(showTable)
#     linhas = cursor.fetchall()
#     print(linhas)


# Localizar se item já possui na tabela

def getLogin(whatAtribute, login):
    cursor = connection.cursor()

    use_DataBase = f"USE {DataBase}"
    cursor.execute(use_DataBase)

    getData = "SELECT senhaUser FROM usuario WHERE ({} = %(dado)s)".format(
        whatAtribute
    )
    values = {"dado": login}

    cursor.execute(getData, values)
    data = cursor.fetchone()

    connection.commit()

    return data
    



# Inserir perguntas e respostas


def inputPerguntaResposta(
    nameTable, Pergunta, respostaCorreta, resposta1, resposta2, resposta3, resposta4
):
    cursor = connection.cursor()

    use_DataBase = f"USE {DataBase}"
    cursor.execute(use_DataBase)

    insertDatas = "INSERT INTO {} (Pergunta, respostaCorreta, resposta1, resposta2, resposta3, resposta4) Values (%(Pergunta)s, %(respostaCorreta)s, %(resposta1)s, %(resposta2)s, %(resposta3)s, %(resposta4)s)".format(
        nameTable
    )

    values = {
        "Pergunta": Pergunta,
        "respostaCorreta": respostaCorreta,
        "resposta1": resposta1,
        "resposta2": resposta2,
        "resposta3": resposta3,
        "resposta4": resposta4,
    }

    cursor.execute(insertDatas, values)

    connection.commit()


# def getOneValue(whatOperation,data,):
#     cursor = connection.cursor()

#     use_DataBase= f'USE {DataBase}'
#     cursor.execute(use_DataBase)

#     getPasswd = "SELECT senhaUser FROM usuario WHERE ({} = %(dado)s)".format(whatAtribute)
#     values = {
#         'dado': login
#     }


