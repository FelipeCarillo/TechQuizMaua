class Quiz:
    def __init__(self, idJogo, autor, nome, categoria, questoes):
        self.idJogo = idJogo
        self.autor = autor
        self.nome = nome
        self.categoria = categoria
        self.questoes = questoes

    def get_idJogo(self):
        return self.idJogo

    def set_idJogo(self, idJogo):
        self.idJogo = idJogo

    def get_autor(self):
        return self.autor

    def set_autor(self, autor):
        self.autor = autor

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_categoria(self):
        return self.categoria

    def set_categoria(self, categoria):
        self.categoria = categoria

    def get_questoes(self):
        return self.questoes

    def set_questoes(self, questoes):
        self.questoes = questoes

