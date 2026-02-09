from repositorio.repositorio_chamados import RepositorioChamados
from models.chamado import StatusChamado

def listar_chamados_abertos():
    repo_chamados = RepositorioChamados()
    chamados_abertos = [chamado for chamado in repo_chamados.obter_todos() if chamado.status == StatusChamado.ABERTO]
    
    if not chamados_abertos:
        print("Não há chamados abertos.")
        return

    for chamado in chamados_abertos:
        print(f"ID: {chamado.id}, Título: {chamado.titulo}, Prioridade: {chamado.prioridade.value}, Usuário: {chamado.usuario}")

def listar_chamados_por_usuario(cpf_usuario: str):
    repo_chamados = RepositorioChamados()
    chamados_usuario = [chamado for chamado in repo_chamados.obter_todos() if chamado.usuario == cpf_usuario]

    if not chamados_usuario:
        print(f"Não há chamados para o usuário com CPF {cpf_usuario}.")
        return

    for chamado in chamados_usuario:
        print(f"ID: {chamado.id}, Título: {chamado.titulo}, Status: {chamado.status.value}, Técnico: {chamado.id_tecnico or 'N/A'}")

def listar_chamados_por_tecnico(id_tecnico: int):
    repo_chamados = RepositorioChamados()
    chamados_tecnico = [chamado for chamado in repo_chamados.obter_todos() if chamado.id_tecnico == id_tecnico]

    if not chamados_tecnico:
        print(f"Não há chamados atribuídos ao técnico com ID {id_tecnico}.")
        return
        
    for chamado in chamados_tecnico:
        print(f"ID: {chamado.id}, Título: {chamado.titulo}, Status: {chamado.status.value}, Usuário: {chamado.usuario}")
