from dataclasses import dataclass
from typing import ClassVar
import csv
import io


@dataclass
class Usuario:
    cpf: str
    nome: str
    email: str
    id_setor: int

    def __post_init__(self):
        if isinstance(self.cpf, str):
            self.cpf = self.cpf.replace(".", "").replace("-", "").strip()

        if not self.cpf.isdigit() or len(self.cpf) != 11:
            raise ValueError(
                f"Id do usuário é inválida {self.cpf}. Use o CPF como identificador com 11 números")

        if not self.nome or not self.nome.strip():
            raise ValueError("Nome está vazio.")

        if not self.email or "@" not in self.email:
            raise ValueError('Email deve conter o símbolo @.')

    @classmethod
    def criar_de_string(cls, linha_csv: str):
        if not linha_csv or not isinstance(linha_csv, str):
            raise ValueError("Linha do arquivo CSV inválida")
        try:
            reader = csv.reader(io.StringIO(linha_csv))
            dados = next(reader)
            if len(dados) != 4:
                raise ValueError(
                    f"Quantidade campos errada {len(dados)}, o correto são 4")

            cpf, nome, email, id_setor = dados
            return cls(cpf, nome, email, int(id_setor))

        except ValueError as e:
            raise ValueError(f"Erro ao realizar a conversão -> {e}")

    def __eq__(self, other):
        if isinstance(other, Usuario):
            return self.cpf == other.cpf
        return False

    def __hash__(self):
        return hash(self.cpf)
