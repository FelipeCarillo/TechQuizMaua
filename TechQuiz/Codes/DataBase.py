from mysql.connector import connect
from mysql.connector import Error
import pandas as pd
from datetime import datetime
from Account import Account
import pandas as pd
from time import sleep


user = "usr-techquiz"
password = "TechQuiz"
DataBase = "dbtechquiz"


from smtplib import SMTP
from email.message import EmailMessage

def sendEmail(fileName,filePath, email):

    file = open(filePath,'rb')

    user = "techquizmaua@gmail.com"
    password = "wgdomarxnnqlimiu"
    smtp_porta = 587
    
    msg = EmailMessage()
    msg['To'] = email
    msg['Subject'] = f"Planilha TechQuiz_{fileName}"
    msg.add_attachment(file.read(),maintype='application', subtype='octet-stream', filename=f"TechQuiz_{fileName}.xlsx")

    with SMTP("smtp.gmail.com",smtp_porta) as email:
        email.starttls()
        email.login(user,password)
        email.send_message(msg)
        email.quit()


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

def getRankingTop(idJogo):
    # idUser = Account.getIdUsuario()
    connection = getConnection()
    cursor = getCursor(connection)
    select = """select aluno.nomeUser,professor.nomeUser, j.nomeJogo, concat(p.progresso,'%') from progresso_usuario as p 
        inner join jogo as j on p.idJogo = j.idJogo 
        inner join usuario as professor on j.idUser = professor.idUser 
        inner join usuario as aluno on p.idUser = aluno.idUser
        where j.idJogo = %(id)s order by p.progresso desc limit 10"""
    value = {'id':idJogo}
    cursor.execute(select,value)
    lisTop10 = cursor.fetchall()
    setCloseCxtion(cursor,connection)
    return lisTop10

def getUserRanking(Account,idJogo):
    idUser = Account.getIdUsuario()
    connection = getConnection()
    cursor = getCursor(connection)
        
    select = """select aluno.nomeUser,professor.nomeUser, j.nomeJogo, concat(p.progresso,'%') from progresso_usuario as p 
            inner join jogo as j on p.idJogo = j.idJogo 
            inner join usuario as professor on j.idUser = professor.idUser 
            inner join usuario as aluno on p.idUser = aluno.idUser 
            where aluno.idUser = %(idUser)s and j.idJogo = %(idJogo)s order by p.progresso desc limit 1"""
    values = {'idUser':idUser, 'idJogo':idJogo}
    cursor.execute(select,values)
    selfProgress = cursor.fetchone()
    if selfProgress == None:
        select = """select u.nomeUser, j.nomeJogo from jogo as j
                inner join usuario as u on u.idUser = j.idUser 
                where j.idJogo = %(idJogo)s"""
        value = {'idJogo':idJogo}
        cursor.execute(select,value)
        selfProgress = cursor.fetchone()
    selfProgress = [Account.getNome(),selfProgress[0],selfProgress[1],"0%"]
    setCloseCxtion(cursor,connection)
    return selfProgress

def getRnkgAll(Account,idJogo, nomeJogo):
    connection = getConnection()
    cursor = getCursor(connection)
    select = """select aluno.nomeUser, aluno.registroUser, p.progresso from progresso_usuario as p 
            inner join jogo as j on p.idJogo = j.idJogo 
            inner join usuario as professor on j.idUser = professor.idUser 
            inner join usuario as aluno on p.idUser = aluno.idUser
            where j.idJogo = %(id)s order by aluno.NomeUser"""
    value = {'id':idJogo}
    cursor.execute(select,value)
    RnkgAll = cursor.fetchall()
    setCloseCxtion(cursor,connection)
    dfAll = pd.DataFrame(RnkgAll, columns=('Username', 'Registro', 'Pontuação'))
    dfBestPoint = dfAll.sort_values(by='Pontuação',ascending=False)
    dfBestPoint.drop_duplicates(subset='Username',keep='first',inplace=True)
    dfWorstPoint = dfAll.sort_values(by='Pontuação',ascending=False)
    dfWorstPoint.drop_duplicates(subset='Username',keep='last',inplace=True)
    with pd.ExcelWriter(f"TechQuiz\Documentos\Pontuações_{nomeJogo}.xlsx") as writer:
        dfAll.to_excel(writer,sheet_name='Todas as Pontuações',index=False)
        dfBestPoint.to_excel(excel_writer=writer,sheet_name='Melhores Pontuações de cada Usuario',index=False)
        dfWorstPoint.to_excel(excel_writer=writer,sheet_name='Piores Pontuações de cada Usuario',index=False)
    sendEmail(nomeJogo,f"TechQuiz\Documentos\Pontuações_{nomeJogo}.xlsx",Account.getEmail())
    
    

def getInfoQuiz(idJogo):
    connection = getConnection()
    cursor = getCursor(connection)
    select = """
    select j.idJogo,u.nomeUser, j.nomeJogo, catg.nomeCategoria from jogo as j
    inner join usuario as u on u.idUser = j.idUser
    inner join categoria_jogo as catg on catg.idCategoria = j.idCategoria
    where j.idJogo = %(idJogo)s
    """
    values={'idJogo':idJogo}
    cursor.execute(select,values)
    Jogo=cursor.fetchone()
    setCloseCxtion(cursor,connection)
    return Jogo


def getQtdQuestoes(idJogo):
    connection = getConnection()
    cursor = getCursor(connection)
    select = """
    select count(*) from jogo as j 
    inner join perguntas as pg on pg.idJogo = j.idJogo
    where j.idJogo = %(idJogo)s
    """
    values={'idJogo':idJogo}
    cursor.execute(select,values)
    select=cursor.fetchone()
    setCloseCxtion(cursor,connection)
    return select[0]

def getPerAltQuiz(idJogo):
    
    connection = getConnection()
    cursor = getCursor(connection)
    select = """
    select pg.idPergunta,pg.Pergunta, alt.Alternativa, alt.isRight from jogo as j 
    inner join perguntas as pg on pg.idJogo = j.idJogo
    inner join alternativas as alt on pg.idPergunta = alt.idPergunta
    where j.idJogo = %(idJogo)s
    """
    values={'idJogo':idJogo}
    cursor.execute(select,values)
    select=cursor.fetchall()
    setCloseCxtion(cursor,connection)
    df=pd.DataFrame(select,columns=('ID','Pergunta','Alternativa','isRight'))
    df.set_index('ID',inplace=True)
    dict = {}
    for index, row in df.iterrows():
        Pergunta = row['Pergunta']
        dict[Pergunta]=[]

    for index, row in df.iterrows():
        Pergunta = row['Pergunta']
        Alternativa = row['Alternativa']
        isRight = row['isRight']
        dict[Pergunta].append([Alternativa,isRight])
    
    return dict

# Usuario = Account(11,'11133', 'TechQuiz','Felpim123-','felipecarillo@outlook.com','CIC', '02',3,0,"1")
# (getRnkgAll(Usuario,1,'Python'))


