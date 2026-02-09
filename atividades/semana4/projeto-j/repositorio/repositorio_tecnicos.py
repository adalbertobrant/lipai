from pathlib import Path
from models.tecnico import Tecnico
import csv

class RepositorioTecnicos:
    def __init__(self):
        self.caminho_arquivo = Path(__file__).parent.parent / 'data' / 'tecnicos.csv'

    def _ler_tecnicos(self) -> list[Tecnico]:
        tecnicos = []
        if not self.caminho_arquivo.exists():
            return []
        with open(self.caminho_arquivo, 'r', encoding='utf-8') as f:
            for linha in f:
                linha = linha.strip()
                if not linha:
                    continue
                try:
                    tecnico = Tecnico.criar_de_string(linha)
                    tecnicos.append(tecnico)
                except ValueError as e:
                    print(f"Erro ao ler linha do tecnico: {e}")
        return tecnicos

    def _escrever_tecnicos(self, tecnicos: list[Tecnico]):
        with open(self.caminho_arquivo, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            for tecnico in tecnicos:
                writer.writerow([tecnico.id, tecnico.nome, tecnico.email, tecnico.especialidade])

    def _gerar_proximo_id(self) -> int:
        tecnicos = self._ler_tecnicos()
        if not tecnicos:
            return 1
        return max(t.id for t in tecnicos) + 1

    def obter_todos(self) -> list[Tecnico]:
        return self._ler_tecnicos()

    def adicionar(self, nome: str, email: str, especialidade: str):
        novo_id = self._gerar_proximo_id()
        tecnico = Tecnico(id=novo_id, nome=nome, email=email, especialidade=especialidade)
        tecnicos = self._ler_tecnicos()
        tecnicos.append(tecnico)
        self._escrever_tecnicos(tecnicos)
        return tecnico

    def buscar_por_id(self, id: int) -> Tecnico | None:
        todos = self.obter_todos()
        for tecnico in todos:
            if tecnico.id == id:
                return tecnico
        return None