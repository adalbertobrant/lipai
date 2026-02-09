from pathlib import Path
import csv

from pathlib import Path
import csv

class RepositorioAutenticacao:
    def __init__(self):
        self.caminho_arquivo = Path(
            __file__).parent.parent / 'data' / 'senhas.csv'

    def _ler_usuarios_acesso(self):
        usuarios_acesso = []
        if not self.caminho_arquivo.exists():
            return []
        with open(self.caminho_arquivo, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) == 4:
                    usuarios_acesso.append({
                        "username": row[0],
                        "password": row[1], # In a real app, this would be hashed
                        "role": row[2],
                        "cpf_or_id": row[3] if row[3] else None
                    })
        return usuarios_acesso

    def _escrever_usuarios_acesso(self, usuarios_acesso):
        with open(self.caminho_arquivo, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            for user in usuarios_acesso:
                writer.writerow([
                    user["username"],
                    user["password"],
                    user["role"],
                    user["cpf_or_id"] if user["cpf_or_id"] is not None else ''
                ])

    def autenticar(self, username, password):
        usuarios = self._ler_usuarios_acesso()
        for user in usuarios:
            if user["username"] == username and user["password"] == password:
                return user["role"], user["cpf_or_id"]
        return None, None # Authentication failed

    def obter_todos_usuarios_acesso(self):
        return self._ler_usuarios_acesso()

    def adicionar_usuario_acesso(self, username, password, role, cpf_or_id=None):
        usuarios = self._ler_usuarios_acesso()
        if any(u["username"] == username for u in usuarios):
            raise ValueError(f"Usuário '{username}' já existe.")
        usuarios.append({
            "username": username,
            "password": password,
            "role": role,
            "cpf_or_id": cpf_or_id
        })
        self._escrever_usuarios_acesso(usuarios)