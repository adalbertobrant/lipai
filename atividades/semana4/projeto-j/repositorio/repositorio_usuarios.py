from pathlib import Path
from models.usuario import Usuario
import csv

class RepositorioUsuarios:
    def __init__(self):
        self.caminho_arquivo = Path(__file__).parent.parent / 'data' / 'usuarios.csv'

    def _ler_usuarios(self) -> list[Usuario]:
        usuarios = []
        if not self.caminho_arquivo.exists():
            return []
        with open(self.caminho_arquivo, 'r', encoding='utf-8') as f:
            for linha in f:
                linha = linha.strip()
                if not linha:
                    continue
                try:
                    usuario = Usuario.criar_de_string(linha)
                    usuarios.append(usuario)
                except ValueError as e:
                    print(f"Erro ao ler linha do usuario: {e}")
        return usuarios

    def _escrever_usuarios(self, usuarios: list[Usuario]):
        with open(self.caminho_arquivo, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            for usuario in usuarios:
                writer.writerow([usuario.cpf, usuario.nome, usuario.email, usuario.id_setor])

    def obter_todos(self) -> list[Usuario]:
        return self._ler_usuarios()

    def adicionar(self, usuario: Usuario):
        usuarios = self._ler_usuarios()
        usuarios.append(usuario)
        self._escrever_usuarios(usuarios)

    def buscar_por_cpf(self, cpf: str) -> Usuario | None:
        todos = self.obter_todos()
        cpf_limpo = cpf.replace(".", "").replace("-", "").strip()

        for usuario in todos:
            if usuario.cpf == cpf_limpo:
                return usuario
        return None