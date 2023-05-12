from mysql.connector import connect
from mysql.connector import Error
import pandas as pd
from datetime import datetime
from Account import Account

user = "usr-techquiz"
password = "TechQuiz"
DataBase = "dbtechquiz"

# Conectar com o Banco de Dados.
def getConnection():
    connection = connect(
        host="mysql246.umbler.com",
        port='41890',
        user=user,
        passwd=password
    )
    return connection

# Retorna o Cursor, variável que executa comandos com o Banco de Dados.
def getCursor(connection):
    cursor = connection.cursor()
    use_DataBase = f"USE {DataBase}"
    cursor.execute(use_DataBase)
    return cursor

# Fecha a conexão com o Banco de Dados e apaga o cursor.
def setCloseCxtion(cursor, connection):
    cursor.close()
    connection.close() 

# Cria o Banco de Dados do jogo.
def createDataBase():
    connection=getConnection()
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
        "CREATE TABLE perguntas(idPergunta int auto_increment primary key, idJogo int not null, foreign key (idJogo) references jogo(idJogo), Pergunta varchar(500) not null)",
        "CREATE TABLE alternativas(idResposta int auto_increment primary key, idPergunta int not null, foreign key (idPergunta) references perguntas(idPergunta), Alternativa varchar(100) not null, isRight boolean not null)",
    ]

    InsertTables = [
        'INSERT INTO cargo VALUES (1,"Administrador"), (2,"Professor"), (3, "Aluno")',
        'INSERT INTO categoria_jogo values (1,"Lógica de Programação"),(2,"Programação Orientada a Objetos"),(3,"Modelagem Orientada a Objetos"), (4,"Banco de Dados Relacionais")',
        "insert into usuario value (1, 1, 'TechQuiz', 'TechQuiz2023', 'techquizIMT@gmail.com','...','..', 2, '2023-05-08 09:57:00',0)"
    ]

    for command in CreateTables:
        cursor.execute(command)
    for command in InsertTables:
        cursor.execute(command)
    connection.commit()
    setCloseCxtion(cursor,connection)
    return DataBase


# Alteração de um dado.
def setOneData(table, chgAtribute,chgValue, findAtribute, findValue):
    connection = getConnection()
    cursor = getCursor(connection)
    code = "UPDATE {} SET {} = %(dadoChange)s WHERE ({} = %(dado)s)".format(table,chgAtribute, findAtribute)
    data = {
        'dadoChange':chgValue,
        'dado':findValue
    }
    cursor.execute(code,data)
    connection.commit()
    setCloseCxtion(cursor,connection)
    

# Verificar se o dado é duplicado.
def hasDuplicated(what, dado):
    connection = getConnection()
    cursor = getCursor(connection)
    duplicate = "SELECT * FROM usuario WHERE ({} = %(what)s)".format(what)
    values = {"what": dado}
    cursor.execute(duplicate, values)
    hasDuplicate = cursor.fetchone()
    if hasDuplicate:
        return False
    setCloseCxtion(cursor,connection)
  
# Retorna um dado de origem especificada.
def getOneData(target_atribute,table,atribute, data):
    connection = getConnection()
    cursor = getCursor(connection)
    getPasswd = "SELECT {} FROM {} WHERE ({} = %(data)s)".format(target_atribute, table, atribute)
    values={
        'data':data
    }
    cursor.execute(getPasswd, values)
    target = cursor.fetchone()
    setCloseCxtion(cursor,connection)
    try:
        return target[0]
    except:
        return target


# Cadastrar um novo jogador.
def cadastrarDados(registroUser, nomeUser, senhaUser, emailUser, idCargo):
    connection = getConnection()
    cursor = getCursor(connection)
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
    setCloseCxtion(cursor,connection)

# Faz a operação Sigma na relação desejada.
def getSigma(table, atribute, data):
    connection = getConnection()
    cursor = getCursor(connection)
    Operation_Sigma = "SELECT * FROM {} WHERE ({} = %(data)s)".format(table,atribute)
    values = {
        "data": data
    }
    cursor.execute(Operation_Sigma, values)
    group = cursor.fetchone()
    setCloseCxtion(cursor,connection)
    return group

# Verificação de dados de Login.
def getLogin(whatAtribute, login):
    connection = getConnection()
    cursor = getCursor(connection)
    getData = "SELECT senhaUser FROM usuario WHERE ({} = %(dado)s)".format(
        whatAtribute
    )
    values = {"dado": login}
    cursor.execute(getData, values)
    data = cursor.fetchone()
    setCloseCxtion(cursor,connection)
    return data

def insertOneData(table,whtAtrbute,Value):
    connection = getConnection()
    cursor = getCursor(connection)
    code = "INSERT INTO {} ({}) VALUES (%(value)s)".format(table,whtAtrbute)
    values={
        'value':Value
    }
    cursor.execute(code,values)
    connection.commit()
    setCloseCxtion(cursor,connection)
    

def createQuiz(Account,nome,categoria,dictPerguntas):
    idUser = Account.getIdUsuario()
    connection = getConnection()
    cursor = getCursor(connection)
    idCategoria = getOneData('idCategoria','categoria_jogo', 'nomeCategoria', categoria)

    if not idCategoria:    
        insertOneData('categoria_jogo','nomeCategoria',categoria)
        idCategoria=getOneData('idCategoria','categoria_jogo', 'nomeCategoria', categoria)
        print(idCategoria)
    insertJogo = "INSERT INTO jogo (nomeJogo,idCategoria,idUser) VALUE (%(nome)s,%(idCat)s,%(idUser)s)"
    values ={'nome':nome,'idCat':idCategoria,'idUser':idUser}
    cursor.execute(insertJogo,values)
    connection.commit()
    idJogo = getOneData(table='jogo',atribute='nomeJogo',target_atribute='idJogo',data=nome)
    

    for pergunta, alternativas in dictPerguntas.items():
        insertPergunta = "INSERT INTO perguntas (idJogo, Pergunta) VALUE (%(idJogo)s,%(pergunta)s)"
        values ={'idJogo':idJogo,'pergunta':pergunta}
        cursor.execute(insertPergunta,values)
        connection.commit()
        IdPergunta = getOneData(table='perguntas',target_atribute='idPergunta',atribute='Pergunta',data=pergunta)
        for alternativa in alternativas:
            insertAlternativa = "INSERT INTO alternativas (idPergunta, Alternativa,isRight) VALUE (%(idPergunta)s,%(alternativa)s,%(bool)s)"
            values ={'idPergunta':IdPergunta,'alternativa':alternativa[0],'bool':alternativa[1]}
            cursor.execute(insertAlternativa,values)
            connection.commit()
    setCloseCxtion(cursor,connection)

def getRankingTop():
    # idUser = Account.getIdUsuario()
    connection = getConnection()
    cursor = getCursor(connection)
    select = """select aluno.nomeUser,professor.nomeUser, j.nomeJogo, p.progresso from progresso_usuario as p 
        inner join jogo as j on p.idJogo = j.idJogo 
        inner join usuario as professor on j.idUser = professor.idUser 
        inner join usuario as aluno on p.idUser = aluno.idUser order by p.progresso limit 10;"""
    cursor.execute(select)
    lisTop10 = cursor.fetchall()
    setCloseCxtion(cursor,connection)
    return lisTop10

def getUserRanking(Account):
    idUser = Account.getIdUsuario()
    connection = getConnection()
    cursor = getCursor(connection)
    select = """select aluno.nomeUser,professor.nomeUser, j.nomeJogo, p.progresso  from progresso_usuario as p 
        inner join jogo as j on p.idJogo = j.idJogo 
        inner join usuario as professor on j.idUser = professor.idUser 
        inner join usuario as aluno on p.idUser = aluno.idUser where aluno.idUser = %(id)s;"""
    value = {'id':idUser}
    cursor.execute(select)
    selfProgress = cursor.fetchall()
    setCloseCxtion(cursor,connection)
    return selfProgress;
# Usuario = Account(1,'11133', 'Felipe','Felpim123-','felipe@gamil.com','CIC', '02',3,0,"1")
# dictPerguntas = {'Você sabe Python':[['Sim',False],['Não',True]],'Como vai?':[['Uma bosta',True],['Felicidade',False]]}

# createQuiz(Usuario,'Felipe','Lóic',dictPerguntas)




# # Inserir perguntas e respostas
# def inputPerguntaResposta(nameTable, Pergunta, respostaCorreta, resposta1, resposta2, resposta3, resposta4):
#     cursor = getCursor()

#     insertDatas = "INSERT INTO {} (Pergunta, respostaCorreta, resposta1, resposta2, resposta3, resposta4) Values (%(Pergunta)s, %(respostaCorreta)s, %(resposta1)s, %(resposta2)s, %(resposta3)s, %(resposta4)s)".format(
#         nameTable
#     )

#     values = {
#         "Pergunta": Pergunta,
#         "respostaCorreta": respostaCorreta,
#         "resposta1": resposta1,
#         "resposta2": resposta2,
#         "resposta3": resposta3,
#         "resposta4": resposta4,
#     }

#     cursor.execute(insertDatas, values)

#     connection.commit()
