from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
import csv
import io

class Prioridade(Enum):
    BAIXA = "baixa"
    MEDIA = "media"
    ALTA = "alta"

class StatusChamado(Enum):
    ABERTO = "aberto"
    EM_ATENDIMENTO = "em atendimento"
    RESOLVIDO = "resolvido"
    CANCELADO = "cancelado"

@dataclass
class Chamado:
    id: int
    usuario: str # cpf do usuario
    titulo: str
    descricao: str
    id_setor_local: int
    prioridade: Prioridade
    id_tecnico: int | None = None
    status: StatusChamado = StatusChamado.ABERTO
    data_abertura: datetime = field(default_factory=datetime.now)
    data_fechamento: datetime | None = None

    def __post_init__(self):
        if not isinstance(self.id, int) or self.id <= 0:
            raise ValueError(f"Id do chamado é inválido {self.id}")
        
        if not self.usuario or not self.usuario.strip():
            raise ValueError("Usuário está vazio.")

        if not self.titulo or not self.titulo.strip():
            raise ValueError("Título está vazio.")

        if not self.descricao or not self.descricao.strip():
            raise ValueError("Descrição está vazia.")
        
        if not isinstance(self.id_setor_local, int) or self.id_setor_local <= 0:
            raise ValueError(f"Id do setor é inválido {self.id_setor_local}")

    @classmethod
    def criar_de_string(cls, linha_csv: str):
        if not linha_csv or not isinstance(linha_csv, str):
            raise ValueError("Linha do arquivo CSV inválida")
        try:
            reader = csv.reader(io.StringIO(linha_csv))
            dados = next(reader)
            
            if len(dados) != 10:
                raise ValueError(
                    f"Quantidade de campos errada {len(dados)}, o correto são 10")

            id, usuario, id_tecnico, titulo, descricao, prioridade, data_abertura, data_fechamento, status, id_setor_local = [item.strip() for item in dados]
            
            return cls(
                id=int(id),
                usuario=usuario,
                id_tecnico=int(id_tecnico) if id_tecnico and id_tecnico != 'None' else None,
                titulo=titulo,
                descricao=descricao,
                prioridade=Prioridade(prioridade),
                data_abertura=datetime.fromisoformat(data_abertura),
                data_fechamento=datetime.fromisoformat(data_fechamento) if data_fechamento and data_fechamento != 'None' else None,
                status=StatusChamado(status),
                id_setor_local=int(id_setor_local)
            )

        except ValueError as e:
            raise ValueError(f"Erro ao realizar a conversão -> {e}")

    def __eq__(self, other):
        if isinstance(other, Chamado):
            return self.id == other.id
        return False

    def __hash__(self):
        return hash(self.id)
