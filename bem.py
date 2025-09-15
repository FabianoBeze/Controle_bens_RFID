class Bem:
    def __init__(self, rfid, nome, local, responsavel, numero_patrimonio):
        self.rfid = rfid
        self.nome = nome
        self.local = local
        self.responsavel = responsavel
        self.numero_patrimonio = numero_patrimonio
        self.status = "operacional"  # operacional, em_reparo
        self.historico_movimentacoes = []

    def registrar_movimentacao(self, novo_local, usuario):
        self.movimentacoes.append({
            "de": self.local,
            "para": novo_local,
            "usuario": usuario.nome
        })
        self.local = novo_local