from administrador import Administrador
from usuario import Usuario
from bem import Bem
from antena import Antena


def menu_usuario(usuario, lista_bens):
    print(f"\nBem-vindo, {usuario.nome}!")
    print("Seus atributos:")
    print(f"Nome: {usuario.nome}")
    print(f"Tipo: {usuario.tipo}")

    while True:
        print("\nMenu do Usuário:")
        print("1 - Ver localização dos bens")
        
        if usuario.tipo == 'professor':
            print("2 - Solicitar reparo de um bem")
            print("3 - Sair")
        elif usuario.tipo == 'tecnico':
            print("2 - Gerenciar reparos")
            print("3 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("\nLocalização de todos os bens:")
            if not lista_bens:
                print("Nenhum bem cadastrado.")
            else:
                for bem in lista_bens:
                    print(f"- {bem.nome} (Patrimônio: {bem.numero_patrimonio}, Local: {bem.local}, Status: {bem.status})")
        
        elif opcao == "2" and usuario.tipo == 'professor':
            print("\nBens operacionais disponíveis para solicitar reparo:")
            bens_operacionais = [b for b in lista_bens if b.status == 'operacional']
            
            if not bens_operacionais:
                print("Nenhum bem operacional disponível para reparo.")
                continue

            for i, bem in enumerate(bens_operacionais):
                print(f"{i} - {bem.nome} (Patrimônio: {bem.numero_patrimonio})")
            
            try:
                idx_bem_input = input("Escolha o bem pelo número (ou pressione Enter para voltar): ")
                if not idx_bem_input:
                    continue
                
                idx_bem = int(idx_bem_input)
                if 0 <= idx_bem < len(bens_operacionais):
                    bem_selecionado = bens_operacionais[idx_bem]
                    bem_selecionado.status = "em_reparo"
                    print(f"Reparo solicitado para o bem '{bem_selecionado.nome}'.")
                else:
                    print("Seleção inválida.")
            except ValueError:
                print("Entrada inválida. Por favor, insira um número.")

        elif opcao == "2" and usuario.tipo == 'tecnico':
            print("\nBens com solicitação de reparo:")
            bens_em_reparo = [bem for bem in lista_bens if bem.status == 'em_reparo']
            if not bens_em_reparo:
                print("Nenhum bem com solicitação de reparo.")
            else:
                for i, bem in enumerate(bens_em_reparo):
                    print(f"{i} - {bem.nome} (Patrimônio: {bem.numero_patrimonio})")
                
                try:
                    idx_bem_reparo_input = input("Escolha o bem para marcar como 'operacional' (ou pressione Enter para voltar): ")
                    if not idx_bem_reparo_input:
                        continue
                    idx_bem_reparo = int(idx_bem_reparo_input)
                    if 0 <= idx_bem_reparo < len(bens_em_reparo):
                        bens_em_reparo[idx_bem_reparo].status = 'operacional'
                        print(f"O bem '{bens_em_reparo[idx_bem_reparo].nome}' foi marcado como operacional.")
                    else:
                        print("Seleção inválida.")
                except ValueError:
                    print("Entrada inválida. Por favor, insira um número.")

        elif opcao == "3":
            print("Saindo do menu do usuário...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")


def menu():
    lista_bens = []
    lista_usuarios = []
    lista_antenas = []

    admin = Administrador("Admin", "1234")

    print("=== Controle de Bens com RFID ===")

    while True:
        print("Menu Principal:")
        print("1 - Acessar como Administrador")
        print("2 - Acessar como Usuário")
        print("3 - Sair")
        opcao_acesso = input("Escolha uma opção de acesso: ")

        if opcao_acesso == "1":
            while True:
                nome = input("Usuário administrador: ")
                senha = input("Senha: ")
                if admin.login(nome, senha):
                    print("Login de administrador realizado com sucesso!")
                    menu_admin(admin, lista_bens, lista_usuarios, lista_antenas)
                    break
                else:
                    print("Usuário ou senha de administrador incorretos. Tente novamente.")
        elif opcao_acesso == "2":
            if not lista_usuarios:
                print("Nenhum usuário cadastrado. O administrador precisa cadastrar usuários primeiro.")
                continue
            nome_usuario = input("Nome de usuário: ")
            senha_usuario = input("Senha: ")
            usuario_encontrado = None
            for u in lista_usuarios:
                if u.login(nome_usuario, senha_usuario):
                    usuario_encontrado = u
                    break
            
            if usuario_encontrado:
                menu_usuario(usuario_encontrado, lista_bens)
            else:
                print("Usuário ou senha incorretos.")
        elif opcao_acesso == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_admin(admin, lista_bens, lista_usuarios, lista_antenas):
    while True:
        print("\\nMenu do Administrador:")
        print("1 - Cadastrar bem")
        print("2 - Cadastrar usuário")
        print("3 - Registrar movimentação")
        print("4 - Emitir relatório de movimentação")
        print("5 - Cadastrar antena/salas")
        print("6 - Voltar ao Menu Principal") 
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            rfid = input("RFID: ")
            nome_bem = input("Nome do bem: ")
            numero_patrimonio = input("Número de patrimônio: ")
            local = input("Local: ")
            responsavel = input("Responsável: ")
            if admin.cadastrar_bem(lista_bens, rfid, nome_bem, local, responsavel, numero_patrimonio):
                print("Bem cadastrado com sucesso!")
            else:
                print("Erro: RFID já cadastrado.")
        elif opcao == "2":
            nome_usuario = input("Nome do usuário: ")
            tipo = input("Tipo (professor/tecnico): ")
            senha_usuario = input("Senha do usuário: ")
            admin.cadastrar_usuario(lista_usuarios, nome_usuario, tipo, senha_usuario)
            print("Usuário cadastrado com sucesso!")
        elif opcao == "3":
            if not lista_bens or not lista_usuarios or not lista_antenas:  # Verifica se há bens, usuários e antenas cadastrados
                print("Cadastre bens, usuários e antenas primeiro.")
                continue
            print("Bens disponíveis:")
            for i, bem in enumerate(lista_bens):
                print(f"{i} - {bem.nome} (Patrimônio: {bem.numero_patrimonio}, Local: {bem.local})")
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
                print(f"{i} - {bem.nome} (Patrimônio: {bem.numero_patrimonio})")
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
            print("Voltando ao menu principal...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()