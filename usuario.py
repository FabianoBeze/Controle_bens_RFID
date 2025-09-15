class Usuario:
    def __init__(self, nome, tipo, senha):
        self.nome = nome
        self.tipo = tipo  # 'professor' ou 'tecnico'
        self.senha = senha

    def login(self, nome, senha):
        return self.nome == nome and self.senha == senha