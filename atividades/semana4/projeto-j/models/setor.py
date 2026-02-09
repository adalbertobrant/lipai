from dataclasses import dataclass
import csv
import io

@dataclass
class Setor:
    id: int
    nome: str
    id_gestor: int

    def __post_init__(self):
        if not isinstance(self.id, int) or self.id <= 0:
            raise ValueError(f"Id do setor é inválido {self.id}")

        if not self.nome or not self.nome.strip():
            raise ValueError("Nome está vazio.")

        if not isinstance(self.id_gestor, int) or self.id_gestor <= 0:
            raise ValueError(f"Id do gestor é inválido {self.id_gestor}")

    @classmethod
    def criar_de_string(cls, linha_csv: str):
        if not linha_csv or not isinstance(linha_csv, str):
            raise ValueError("Linha do arquivo CSV inválida")
        try:
            reader = csv.reader(io.StringIO(linha_csv))
            dados = next(reader)
            if len(dados) != 3:
                raise ValueError(
                    f"Quantidade campos errada {len(dados)}, o correto são 3")

            id, nome, id_gestor = dados
            return cls(int(id), nome, int(id_gestor))

        except ValueError as e:
            raise ValueError(f"Erro ao realizar a conversão -> {e}")

    def __eq__(self, other):
        if isinstance(other, Setor):
            return self.id == other.id
        return False

    def __hash__(self):
        return hash(self.id)
