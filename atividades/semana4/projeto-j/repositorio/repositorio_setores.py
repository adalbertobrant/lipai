from pathlib import Path
from models.setor import Setor
import csv

class RepositorioSetores:
    def __init__(self):
        self.caminho_arquivo = Path(__file__).parent.parent / 'data' / 'setores.csv'

    def _ler_setores(self) -> list[Setor]:
        setores = []
        if not self.caminho_arquivo.exists():
            return []
        with open(self.caminho_arquivo, 'r', encoding='utf-8') as f:
            for linha in f:
                linha = linha.strip()
                if not linha:
                    continue
                try:
                    setor = Setor.criar_de_string(linha)
                    setores.append(setor)
                except ValueError as e:
                    print(f"Erro ao ler linha do setor: {e}")
        return setores

    def _escrever_setores(self, setores: list[Setor]):
        with open(self.caminho_arquivo, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            for setor in setores:
                writer.writerow([setor.id, setor.nome, setor.id_gestor])

    def _gerar_proximo_id(self) -> int:
        setores = self._ler_setores()
        if not setores:
            return 1
        return max(s.id for s in setores) + 1

    def obter_todos(self) -> list[Setor]:
        return self._ler_setores()

    def adicionar(self, nome: str, id_gestor: int):
        novo_id = self._gerar_proximo_id()
        setor = Setor(id=novo_id, nome=nome, id_gestor=id_gestor)
        setores = self._ler_setores()
        setores.append(setor)
        self._escrever_setores(setores)
        return setor

    def buscar_por_id(self, id: int) -> Setor | None:
        todos = self.obter_todos()
        for setor in todos:
            if setor.id == id:
                return setor
        return None