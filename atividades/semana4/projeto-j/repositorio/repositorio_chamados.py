from pathlib import Path
from models.chamado import Chamado, StatusChamado
import csv


class RepositorioChamados:
    def __init__(self):
        self.caminho_arquivo = Path(
            __file__).parent.parent / 'data' / 'chamados.csv'

    def _ler_chamados(self) -> list[Chamado]:
        chamados = []
        if not self.caminho_arquivo.exists():
            return []
        with open(self.caminho_arquivo, 'r', encoding='utf-8') as f:
            for linha in f:
                linha = linha.strip()
                if not linha:
                    continue
                try:
                    chamado = Chamado.criar_de_string(linha)
                    chamados.append(chamado)
                except ValueError as e:
                    print(f"Erro ao ler linha do chamado: {e}")
        return chamados

    def _escrever_chamados(self, chamados: list[Chamado]):
        with open(self.caminho_arquivo, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            for chamado in chamados:
                row = [
                    str(chamado.id),
                    chamado.usuario,
                    str(chamado.id_tecnico) if chamado.id_tecnico is not None else 'None',
                    chamado.titulo,
                    chamado.descricao,
                    chamado.prioridade.value,
                    chamado.data_abertura.isoformat(),
                    chamado.data_fechamento.isoformat() if chamado.data_fechamento else 'None',
                    chamado.status.value,
                    str(chamado.id_setor_local)
                ]
                writer.writerow(row)
    
    def _gerar_proximo_id(self) -> int:
        chamados = self._ler_chamados()
        if not chamados:
            return 1
        return max(c.id for c in chamados) + 1

    def obter_todos(self) -> list[Chamado]:
        return self._ler_chamados()

    def adicionar(self, usuario: str, titulo: str, descricao: str, id_setor_local: int, prioridade: StatusChamado):
        novo_id = self._gerar_proximo_id()
        chamado = Chamado(id=novo_id, usuario=usuario, titulo=titulo, descricao=descricao, id_setor_local=id_setor_local, prioridade=prioridade)
        chamados = self._ler_chamados()
        chamados.append(chamado)
        self._escrever_chamados(chamados)
        return chamado

    def buscar_por_id(self, id: int) -> Chamado | None:
        for chamado in self._ler_chamados():
            if chamado.id == id:
                return chamado
        return None

    def atualizar(self, chamado_atualizado: Chamado):
        chamados = self._ler_chamados()
        chamados = [chamado if chamado.id != chamado_atualizado.id else chamado_atualizado for chamado in chamados]
        self._escrever_chamados(chamados)
