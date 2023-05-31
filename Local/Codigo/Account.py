class Account:
    def __init__(self, idUsuario,registro, nome, passwd, email, curso, ano, cargo, firstLogin, dateSignup):
        self.idUsuario = int(idUsuario)
        self.registro = registro
        self.nome = nome
        self.passwd = passwd
        self.email = email
        self.curso = curso
        self.ano = ano
        self.cargo = int(cargo)
        self.firstLogin = int(firstLogin)
        self.dateSignup = dateSignup

    # Getters
    def getIdUsuario(self):
        return self.idUsuario
    
    def getRegistro(self):
        return self.registro
    
    def getNome(self):
        return self.nome
    
    def getPasswd(self):
        return self.passwd
    
    def getEmail(self):
        return self.email
    
    def getCurso(self):
        return self.curso
    
    def getAno(self):
        return self.ano
    
    def getCargo(self):
        return self.cargo
    
    def getFirstLogin(self):
        return self.firstLogin
    
    def getDateSignup(self):
        return self.dateSignup
    
    # Setters
    def setIdUsuario(self, idUsuario):
        self.idUsuario = idUsuario
    
    def setRegistro(self, registro):
        self.registro = registro
    
    def setNome(self, nome):
        self.nome = nome
    
    def setPasswd(self, passwd):
        self.passwd = passwd
    
    def setEmail(self, email):
        self.email = email
    
    def setCurso(self, curso):
        self.curso = curso
    
    def setAno(self, ano):
        self.ano = ano
    
    def setCargo(self, cargo):
        self.cargo = cargo
    
    def setFirstLogin(self, firstLogin):
        self.firstLogin = firstLogin
    
    def setDateSignup(self, dateSignup):
        self.dateSignup = dateSignup