from dataclasses import dataclass
import csv
import io

@dataclass
class Tecnico:
    id: int
    nome: str
    email: str
    especialidade: str

    def __post_init__(self):
        if not isinstance(self.id, int) or self.id <= 0:
            raise ValueError(f"Id do técnico é inválido {self.id}")

        if not self.nome or not self.nome.strip():
            raise ValueError("Nome está vazio.")
        
        if not self.email or "@" not in self.email:
            raise ValueError('Email deve conter o símbolo @.')

        if not self.especialidade or not self.especialidade.strip():
            raise ValueError("Especialidade está vazia.")

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

            id, nome, email, especialidade = dados
            return cls(int(id), nome, email, especialidade)

        except ValueError as e:
            raise ValueError(f"Erro ao realizar a conversão -> {e}")
    
    def __eq__(self, other):
        if isinstance(other, Tecnico):
            return self.id == other.id
        return False

    def __hash__(self):
        return hash(self.id)
