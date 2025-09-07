class Bem:
    def __init__(self, rfid, nome, local, responsavel):   # inicializa o bem com RFID, nome, local e responsável
        self.rfid = rfid
        self.nome = nome
        self.local = local
        self.responsavel = responsavel
        self.movimentacoes = []

    def registrar_movimentacao(self, novo_local, usuario):  # Registra a movimentação do bem
        self.movimentacoes.append({
            "de": self.local,
            "para": novo_local,
            "usuario": usuario.nome
        })
        self.local = novo_local