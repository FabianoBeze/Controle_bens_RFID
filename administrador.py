from bem import Bem
from usuario import Usuario

class Administrador:
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha

    def login(self, nome, senha):
        return self.nome == nome and self.senha == senha

    def cadastrar_bem(self, lista_bens, rfid, nome, local, responsavel, numero_patrimonio):
        for bem in lista_bens:
            if bem.rfid == rfid:
                return False  # RFID já cadastrado
        bem = Bem(rfid, nome, local, responsavel, numero_patrimonio)
        lista_bens.append(bem)
        return True

    def cadastrar_usuario(self, lista_usuarios, nome, tipo, senha):
        usuario = Usuario(nome, tipo, senha)
        lista_usuarios.append(usuario)

    def emitir_relatorio(self, bem):
        return bem.historico_movimentacoes