from administrador import Administrador
from usuario import Usuario
from bem import Bem
from antena import Antena


def menu():
    lista_bens = []
    lista_usuarios = []
    lista_antenas = []

    admin = Administrador("Admin", "1234")

    print("=== Controle de Bens com RFID ===")
    nome = input("Usuário administrador: ")
    senha = input("Senha: ")

    if not admin.login(nome, senha):             # Verifica se o login é válido
        print("Usuário ou senha incorretos.")
        return

    print("Login realizado com sucesso!")

    while True:
        print("\nMenu:")
        print("1 - Cadastrar bem")
        print("2 - Cadastrar usuário")
        print("3 - Registrar movimentação")
        print("4 - Emitir relatório de movimentação")
        print("5 - Cadastrar antena/salas")
        print("6 - Sair") 
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            rfid = input("RFID: ")
            nome_bem = input("Nome do bem: ")   
            local = input("Local: ")
            responsavel = input("Responsável: ")
            admin.cadastrar_bem(lista_bens, rfid, nome_bem, local, responsavel)
            print("Bem cadastrado com sucesso!")
        elif opcao == "2":
            nome_usuario = input("Nome do usuário: ")
            tipo = input("Tipo (professor/tecnico): ")
            admin.cadastrar_usuario(lista_usuarios, nome_usuario, tipo)
            print("Usuário cadastrado com sucesso!")
        elif opcao == "3":
            if not lista_bens or not lista_usuarios or not lista_antenas:  # Verifica se há bens, usuários e antenas cadastrados
                print("Cadastre bens, usuários e antenas primeiro.")
                continue
            print("Bens disponíveis:")
            for i, bem in enumerate(lista_bens):
                print(f"{i} - {bem.nome} (Local: {bem.local})")
            idx_bem = int(input("Escolha o bem pelo número: "))
            print("Usuários disponíveis:")
            for i, usuario in enumerate(lista_usuarios):
                print(f"{i} - {usuario.nome} ({usuario.tipo})")
            idx_usuario = int(input("Escolha o usuário pelo número: "))
            print("Antenas/Salas disponíveis:")
            for i, antena in enumerate(lista_antenas):
                print(f"{i} - {antena.local} (ID: {antena.id_antena})")
            idx_antena = int(input("Escolha a antena/sala pelo número: "))
            novo_local = lista_antenas[idx_antena].local
            lista_bens[idx_bem].registrar_movimentacao(novo_local, lista_usuarios[idx_usuario])
            print("Movimentação registrada com sucesso!")
        elif opcao == "4":
            if not lista_bens:
                print("Cadastre bens primeiro.")
                continue
            print("Bens disponíveis:")
            for i, bem in enumerate(lista_bens):
                print(f"{i} - {bem.nome}")
            idx_bem = int(input("Escolha o bem pelo número: "))
            relatorio = admin.emitir_relatorio(lista_bens[idx_bem])
            for movimentacao in relatorio:
                print(f"De: {movimentacao['de']} Para: {movimentacao['para']} Por: {movimentacao['usuario']}")
        elif opcao == "5":
            id_antena = input("ID da antena: ")
            local = input("Local da antena: ")
            antena = Antena(id_antena, local)
            lista_antenas.append(antena)
            print("Antena cadastrada com sucesso!")
        elif opcao == "6":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()