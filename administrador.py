from usuario import Usuario
from bem import Bem

class Administrador(Usuario):
    def __init__(self, nome, senha):   # Inicializa o administrador com nome e senha
        self.nome = nome
        self.senha = senha

    def login(self, nome, senha):   # Verifica se o login é válido
        return self.nome == nome and self.senha == senha

    def cadastrar_bem(self, lista_bens, rfid, nome, local, responsavel):
        bem = Bem(rfid, nome, local, responsavel)
        lista_bens.append(bem)

    def editar_bem(self, bem, **kwargs):  # Edita as informações do bem
        for key, value in kwargs.items():
            setattr(bem, key, value)

    def emitir_relatorio(self, bem):
        return bem.movimentacoes

    def cadastrar_usuario(self, lista_usuarios, nome, tipo):
        usuario = Usuario(nome, tipo)
        lista_usuarios.append(usuario)

    def configurar_alerta(self, bem, alerta):
        bem.alerta = alerta
