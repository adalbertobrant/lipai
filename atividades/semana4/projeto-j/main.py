from datetime import datetime
from models.chamado import Chamado, Prioridade, StatusChamado
from models.setor import Setor
from models.tecnico import Tecnico
from models.usuario import Usuario
from relatorio import relatorios
from repositorio.repositorio_chamados import RepositorioChamados
from repositorio.repositorio_setores import RepositorioSetores
from repositorio.repositorio_tecnicos import RepositorioTecnicos
from repositorio.repositorio_usuarios import RepositorioUsuarios
from repositorio.repositorio_autenticacao import RepositorioAutenticacao


def exibir_lista_com_indices(itens, atributo_id, atributo_display):
    for i, item in enumerate(itens):
        print(f"{i + 1}. {getattr(item, atributo_display)} (ID: {getattr(item, atributo_id)})")

def selecionar_opcao_por_lista(itens, atributo_id, atributo_display, prompt):
    if not itens:
        print("Nenhum item disponível para seleção.")
        return None

    while True:
        exibir_lista_com_indices(itens, atributo_id, atributo_display)
        try:
            escolha = int(input(prompt))
            if 1 <= escolha <= len(itens):
                return getattr(itens[escolha - 1], atributo_id)
            else:
                print("Escolha inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")


def login(repo_autenticacao: RepositorioAutenticacao):
    while True:
        print("\n--- Login ---")
        username = input("Usuário: ")
        password = input("Senha: ")
        role, identity = repo_autenticacao.autenticar(username, password)
        if role and identity:
            print(f"Login bem-sucedido! Bem-vindo, {username} ({role}).")
            return role, identity
        elif role == 'admin' and not identity:
            print(f"Login bem-sucedido! Bem-vindo, {username} ({role}).")
            return role, None # Admin might not have a specific identity like CPF
        else:
            print("Usuário ou senha inválidos. Tente novamente.")

def menu_usuarios(repo_usuarios: RepositorioUsuarios, repo_setores: RepositorioSetores):
    while True:
        print("\n--- Menu Usuários ---")
        print("1. Cadastrar Usuário")
        print("2. Listar Usuários")
        print("0. Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cpf = input("CPF: ")
            nome = input("Nome: ")
            email = input("Email: ")
            
            setores_disponiveis = repo_setores.obter_todos()
            id_setor_selecionado = selecionar_opcao_por_lista(setores_disponiveis, 'id', 'nome', "Selecione o Setor do Usuário: ")
            
            if id_setor_selecionado is None:
                print("Nenhum setor foi selecionado. Cadastro cancelado.")
                continue

            try:
                usuario = Usuario(cpf, nome, email, id_setor_selecionado)
                repo_usuarios.adicionar(usuario)
                print("Usuário cadastrado com sucesso!")
            except ValueError as e:
                print(f"Erro ao cadastrar usuário: {e}")
        elif opcao == "2":
            for usuario in repo_usuarios.obter_todos():
                print(f"CPF: {usuario.cpf}, Nome: {usuario.nome}, Email: {usuario.email}, Setor: {usuario.id_setor}")
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")


def menu_tecnicos(repo_tecnicos: RepositorioTecnicos):
    while True:
        print("\n--- Menu Técnicos ---")
        print("1. Cadastrar Técnico")
        print("2. Listar Técnicos")
        print("0. Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            email = input("Email: ")
            especialidade = input("Especialidade: ")
            try:
                # O ID é gerado automaticamente pelo repositório
                tecnico = repo_tecnicos.adicionar(nome, email, especialidade)
                print(f"Técnico cadastrado com sucesso! ID: {tecnico.id}")
            except ValueError as e:
                print(f"Erro ao cadastrar técnico: {e}")
        elif opcao == "2":
            for tecnico in repo_tecnicos.obter_todos():
                print(f"ID: {tecnico.id}, Nome: {tecnico.nome}, Email: {tecnico.email}, Especialidade: {tecnico.especialidade}")
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")


def menu_setores(repo_setores: RepositorioSetores):
    while True:
        print("\n--- Menu Setores ---")
        print("1. Cadastrar Setor")
        print("2. Listar Setores")
        print("0. Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            
            # Precisamos do ID do gestor. Assumindo que gestores são usuários.
            # Se gestores forem uma entidade separada, precisaríamos de outro repo/lista.
            # Por simplicidade, vamos permitir input manual por enquanto ou selecionar de uma lista de usuários
            # Mas, como id_gestor é um ID, e usuários tem CPF, vamos tratar como um ID numérico.
            # Para este cenário, vamos manter o input manual para id_gestor, mas o ID do setor é automático.
            id_gestor = int(input("ID do Gestor: ")) # Manter manual para este campo

            try:
                # O ID do setor é gerado automaticamente
                setor = repo_setores.adicionar(nome, id_gestor)
                print(f"Setor cadastrado com sucesso! ID: {setor.id}")
            except ValueError as e:
                print(f"Erro ao cadastrar setor: {e}")
        elif opcao == "2":
            for setor in repo_setores.obter_todos():
                print(f"ID: {setor.id}, Nome: {setor.nome}, Gestor: {setor.id_gestor}")
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")


def menu_chamados(repo_chamados: RepositorioChamados, repo_usuarios: RepositorioUsuarios, repo_tecnicos: RepositorioTecnicos, repo_setores: RepositorioSetores, user_role: str, user_identity: str | None):
    while True:
        print("\n--- Menu Chamados ---")
        print("1. Abrir Chamado")
        
        if user_role == "admin":
            print("2. Atribuir Técnico")
            print("3. Atualizar Status")
            print("4. Listar Todos os Chamados")
        else:
            print("2. Listar Meus Chamados")
            print("3. Ver Status de um Chamado")
            
        print("0. Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == "1": # Abrir Chamado
            cpf_usuario = user_identity # Para usuário comum, o CPF já está definido

            if user_role == "admin": # Admin pode abrir chamado para qualquer usuário
                usuarios_disponiveis = repo_usuarios.obter_todos()
                cpf_usuario = selecionar_opcao_por_lista(usuarios_disponiveis, 'cpf', 'nome', "Selecione o Usuário que está abrindo o Chamado (CPF): ")
                if cpf_usuario is None:
                    print("Nenhum usuário selecionado. Abertura de chamado cancelada.")
                    continue

            titulo = input("Título: ")
            descricao = input("Descrição: ")
            
            setores_disponiveis = repo_setores.obter_todos()
            id_setor_selecionado = selecionar_opcao_por_lista(setores_disponiveis, 'id', 'nome', "Selecione o Setor associado ao Chamado: ")
            if id_setor_selecionado is None:
                print("Nenhum setor selecionado. Abertura de chamado cancelada.")
                continue

            prioridade_str = input("Prioridade (baixa, media, alta): ").lower()
            try:
                prioridade = Prioridade(prioridade_str)
                # O ID do chamado é gerado automaticamente pelo repositório
                chamado_aberto = repo_chamados.adicionar(cpf_usuario, titulo, descricao, id_setor_selecionado, prioridade)
                print(f"Chamado aberto com sucesso! ID: {chamado_aberto.id}")
            except (ValueError, KeyError) as e:
                print(f"Erro ao abrir chamado: {e}")
        
        elif opcao == "2":
            if user_role == "admin": # Admin option: Atribuir Técnico
                chamados_abertos = [c for c in repo_chamados.obter_todos() if c.status != StatusChamado.RESOLVIDO and c.status != StatusChamado.CANCELADO]
                id_chamado_selecionado = selecionar_opcao_por_lista(chamados_abertos, 'id', 'titulo', "Selecione o Chamado para atribuir (ID): ")
                if id_chamado_selecionado is None:
                    print("Nenhum chamado selecionado. Atribuição cancelada.")
                    continue
                
                tecnicos_disponiveis = repo_tecnicos.obter_todos()
                id_tecnico_selecionado = selecionar_opcao_por_lista(tecnicos_disponiveis, 'id', 'nome', "Selecione o Técnico para atribuir (ID): ")
                if id_tecnico_selecionado is None:
                    print("Nenhum técnico selecionado. Atribuição cancelada.")
                    continue

                chamado = repo_chamados.buscar_por_id(id_chamado_selecionado)
                if chamado:
                    chamado.id_tecnico = id_tecnico_selecionado
                    chamado.status = StatusChamado.EM_ATENDIMENTO
                    repo_chamados.atualizar(chamado)
                    print("Técnico atribuído com sucesso!")
                else:
                    print("Chamado não encontrado.")
            else: # User option: Listar Meus Chamados
                chamados_do_usuario = [c for c in repo_chamados.obter_todos() if c.usuario == user_identity]
                if chamados_do_usuario:
                    for c in chamados_do_usuario:
                        print(f"ID: {c.id}, Título: {c.titulo}, Status: {c.status.value}, Prioridade: {c.prioridade.value}")
                else:
                    print("Você não possui chamados abertos.")

        elif opcao == "3":
            if user_role == "admin": # Admin option: Atualizar Status
                chamados_para_atualizar = [c for c in repo_chamados.obter_todos() if c.status != StatusChamado.RESOLVIDO and c.status != StatusChamado.CANCELADO]
                id_chamado_selecionado = selecionar_opcao_por_lista(chamados_para_atualizar, 'id', 'titulo', "Selecione o Chamado para atualizar status (ID): ")
                if id_chamado_selecionado is None:
                    print("Nenhum chamado selecionado. Atualização cancelada.")
                    continue

                status_str = input("Novo Status (aberto, em atendimento, resolvido, cancelado): ").lower()
                chamado = repo_chamados.buscar_por_id(id_chamado_selecionado)
                if chamado:
                    try:
                        status = StatusChamado(status_str)
                        chamado.status = status
                        if status in [StatusChamado.RESOLVIDO, StatusChamado.CANCELADO]:
                            chamado.data_fechamento = datetime.now()
                        repo_chamados.atualizar(chamado)
                        print("Status atualizado com sucesso!")
                    except (ValueError, KeyError) as e:
                        print(f"Erro ao atualizar status: {e}")
                else:
                    print("Chamado não encontrado.")
            else: # User option: Ver Status de um Chamado
                chamados_do_usuario = [c for c in repo_chamados.obter_todos() if c.usuario == user_identity]
                id_chamado_selecionado = selecionar_opcao_por_lista(chamados_do_usuario, 'id', 'titulo', "Selecione o Chamado para verificar status (ID): ")
                if id_chamado_selecionado is None:
                    print("Nenhum chamado selecionado.")
                    continue

                chamado = repo_chamados.buscar_por_id(id_chamado_selecionado)
                if chamado and chamado.usuario == user_identity:
                    print(f"Chamado ID: {chamado.id}, Título: {chamado.titulo}, Status: {chamado.status.value}, Prioridade: {chamado.prioridade.value}")
                else:
                    print("Chamado não encontrado ou você não tem permissão para vê-lo.")
        elif opcao == "4":
            if user_role == "admin": # Admin option: Listar Todos os Chamados
                all_chamados = repo_chamados.obter_todos()
                if all_chamados:
                    for c in all_chamados:
                        print(f"ID: {c.id}, Usuário: {c.usuario}, Título: {c.titulo}, Status: {c.status.value}, Prioridade: {c.prioridade.value}, Técnico: {c.id_tecnico if c.id_tecnico else 'N/A'}")
                else:
                    print("Não há chamados cadastrados.")
            else:
                print("Opção inválida para seu perfil.")
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")


def menu_relatorios(repo_chamados: RepositorioChamados, repo_usuarios: RepositorioUsuarios, repo_tecnicos: RepositorioTecnicos, user_role: str, user_identity: str | None):
    while True:
        print("\n--- Menu Relatórios ---")
        if user_role == "admin":
            print("1. Listar Chamados Abertos")
            print("2. Listar Chamados por Usuário")
            print("3. Listar Chamados por Técnico")
        else: # Regular user
            print("1. Listar Meus Chamados Abertos")
            print("2. Listar Todos os Meus Chamados")
        print("0. Voltar")
        opcao = input("Escolha uma opção: ")

        if user_role == "admin":
            if opcao == "1":
                relatorios.listar_chamados_abertos()
            elif opcao == "2":
                usuarios_disponiveis = repo_usuarios.obter_todos()
                cpf_usuario_selecionado = selecionar_opcao_por_lista(usuarios_disponiveis, 'cpf', 'nome', "Selecione o Usuário para listar chamados (CPF): ")
                if cpf_usuario_selecionado is None:
                    print("Nenhum usuário selecionado. Operação cancelada.")
                    continue
                relatorios.listar_chamados_por_usuario(cpf_usuario_selecionado)
            elif opcao == "3":
                tecnicos_disponiveis = repo_tecnicos.obter_todos()
                id_tecnico_selecionado = selecionar_opcao_por_lista(tecnicos_disponiveis, 'id', 'nome', "Selecione o Técnico para listar chamados (ID): ")
                if id_tecnico_selecionado is None:
                    print("Nenhum técnico selecionado. Operação cancelada.")
                    continue
                relatorios.listar_chamados_por_tecnico(id_tecnico_selecionado)
            elif opcao == "0":
                break
            else:
                print("Opção inválida.")
        else: # Regular user
            if opcao == "1":
                chamados_abertos_do_usuario = [c for c in repo_chamados.obter_todos() if c.usuario == user_identity and c.status == StatusChamado.ABERTO]
                if chamados_abertos_do_usuario:
                    for c in chamados_abertos_do_usuario:
                        print(f"ID: {c.id}, Título: {c.titulo}, Status: {c.status.value}, Prioridade: {c.prioridade.value}")
                else:
                    print("Você não possui chamados abertos.")
            elif opcao == "2":
                chamados_do_usuario = [c for c in repo_chamados.obter_todos() if c.usuario == user_identity]
                if chamados_do_usuario:
                    for c in chamados_do_usuario:
                        print(f"ID: {c.id}, Título: {c.titulo}, Status: {c.status.value}, Prioridade: {c.prioridade.value}")
                else:
                    print("Você não possui chamados.")
            elif opcao == "0":
                break
            else:
                print("Opção inválida.")



def menu_gerenciar_usuarios_acesso(repo_autenticacao: RepositorioAutenticacao):
    while True:
        print("\n--- Gerenciar Usuários de Acesso ---")
        print("1. Cadastrar Novo Usuário de Acesso")
        print("2. Listar Usuários de Acesso")
        print("0. Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            username = input("Nome de Usuário (login): ")
            password = input("Senha: ")
            role = input("Função (admin/user): ").lower()
            cpf_or_id = None
            if role == "user":
                cpf_or_id = input("CPF associado (para usuário comum): ")
            
            try:
                repo_autenticacao.adicionar_usuario_acesso(username, password, role, cpf_or_id)
                print("Usuário de acesso cadastrado com sucesso!")
            except ValueError as e:
                print(f"Erro ao cadastrar usuário de acesso: {e}")
        elif opcao == "2":
            usuarios = repo_autenticacao.obter_todos_usuarios_acesso()
            if usuarios:
                for user in usuarios:
                    print(f"Usuário: {user['username']}, Função: {user['role']}, CPF/ID: {user['cpf_or_id'] if user['cpf_or_id'] else 'N/A'}")
            else:
                print("Nenhum usuário de acesso cadastrado.")
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")


def main():
    repo_usuarios = RepositorioUsuarios()
    repo_tecnicos = RepositorioTecnicos()
    repo_chamados = RepositorioChamados()
    repo_setores = RepositorioSetores()
    repo_autenticacao = RepositorioAutenticacao()

    user_role, user_identity = login(repo_autenticacao)

    if not user_role:
        print("Falha na autenticação. Encerrando o sistema.")
        return

    while True:
        print("\n--- Sistema de Chamados de Suporte de TI ---")
        if user_role == "admin":
            print("1. Gerenciar Usuários")
            print("2. Gerenciar Técnicos")
            print("3. Gerenciar Setores")
            print("4. Gerenciar Chamados (Admin)")
            print("5. Relatórios (Admin)")
            print("6. Gerenciar Usuários de Acesso")
            print("0. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                menu_usuarios(repo_usuarios, repo_setores)
            elif opcao == "2":
                menu_tecnicos(repo_tecnicos)
            elif opcao == "3":
                menu_setores(repo_setores)
            elif opcao == "4":
                menu_chamados(repo_chamados, repo_usuarios, repo_tecnicos, repo_setores, user_role, user_identity)
            elif opcao == "5":
                menu_relatorios(repo_chamados, repo_usuarios, repo_tecnicos, user_role, user_identity)
            elif opcao == "6":
                menu_gerenciar_usuarios_acesso(repo_autenticacao)
            elif opcao == "0":
                print("Saindo do sistema...")
                break
            else:
                print("Opção inválida.")
        else:  # user_role == "user"
            print("1. Gerenciar Meus Chamados")
            print("2. Meus Relatórios")
            print("0. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                menu_chamados(repo_chamados, user_role, user_identity)
            elif opcao == "2":
                menu_relatorios(repo_chamados, user_role, user_identity)
            elif opcao == "0":
                print("Saindo do sistema...")
                break
            else:
                print("Opção inválida.")


if __name__ == "__main__":
    main()

