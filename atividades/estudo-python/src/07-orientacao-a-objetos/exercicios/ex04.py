"""
 Exercício 04 - Lista de participações no Projeto
 Alterar a classe Projeto para incluir uma lista de participações e o método add_participacao.
"""

from ex03 import Participacao


class Projeto:
    """ Classe Projeto Atualizada (com lista de participações) """

    def __init__(self, codigo, titulo, responsavel):
        # Ao atribuir aqui, já acionamos os setters para validar
        self.codigo = codigo
        self.titulo = titulo
        self.responsavel = responsavel
        self.participacoes = []

    @classmethod
    def criar_projeto(cls, string_dados):
        """ Cria um objeto Projeto a partir de uma string 'cod, titulo, responsavel' """
        if not string_dados or not isinstance(string_dados, str):
            raise ValueError("Erro -> deve ser passada uma string válida")
        try:
            partes = [p.strip() for p in string_dados.split(',')]
            if len(partes) != 3:
                raise ValueError(
                    "A string deve ter 3 partes separadas por vírgula.")
            codigo_str, titulo, responsavel = partes
            return cls(int(codigo_str), titulo, responsavel)
        except ValueError as e:
            raise ValueError(f"Erro ao criar projeto: {e}")

    @property
    def codigo(self):
        """ retorna o código """
        return self._codigo

    @codigo.setter
    def codigo(self, valor):
        """ Valida se é inteiro e positivo """
        try:
            valor_int = int(valor)
        except (ValueError, TypeError):
            raise ValueError("O código deve ser um número inteiro.")
        if valor_int <= 0:
            raise ValueError("O código deve ser um inteiro positivo.")
        self._codigo = valor_int

    @property
    def titulo(self):
        """ retorna o título """
        return self._titulo

    @titulo.setter
    def titulo(self, valor):
        if not valor or not str(valor).strip():
            raise ValueError("O título não pode ser nulo ou vazio")
        self._titulo = valor.strip()

    @property
    def responsavel(self):
        """ retorna o responsavel """
        return self._responsavel

    @responsavel.setter
    def responsavel(self, valor):
        if not valor or not str(valor).strip():
            raise ValueError("O responsável não pode ser nulo ou vazio")
        self._responsavel = valor.strip()

    def add_participacao(self, participacao):
        """ Adiciona uma participação ao projeto. """
        if isinstance(participacao, Participacao):
            self.participacoes.append(participacao)
            print(
                f"Participação (Código: {participacao.codigo}) adicionada com sucesso ao Projeto {self.codigo}.")
        else:
            raise ValueError(
                "O objeto fornecido não é uma instância válida da classe Participacao.")

    def listar_participacoes(self):
        """ Método auxiliar para visualizar as participações (opcional, para testes) """
        print(f"\n--- Participações no Projeto: {self.titulo} ---")
        if not self.participacoes:
            print("Nenhuma participação cadastrada.")
        else:
            for p in self.participacoes:
                print(f" - {p}")

    def __eq__(self, other):
        """ Dois projetos são iguais se tiverem o mesmo código """
        if isinstance(other, Projeto):
            return self.codigo == other.codigo
        return False

    def __str__(self):
        # Atualizado __str__ para indicar quantas participações existem
        qtd_part = len(self.participacoes)
        return f'Projeto [Código: {self.codigo}, Título: "{self.titulo}", Responsável: {self.responsavel}, Participações: {qtd_part}]'


# testes

if __name__ == "__main__":
    print('-----\nTestes do Projeto Atualizado (Ex04)\n----')
    try:
        proj_novo = Projeto(100, 'Sistema de Gestão Acadêmica', 'Prof. Xavier')
        print(f"Projeto criado: {proj_novo}")
    except ValueError as e:
        print(f"Erro ao criar projeto: {e}")

    # 2. Criar Participações (Usando a classe do ex03)
    dados_part1 = '5001 ; "10-02-2025" ; "10-12-2025" ; "SP123, Ana Souza, ana@email.com" ; "100, SGA Módulo 1, Prof. Xavier"'
    dados_part2 = '5002 ; "15-03-2025" ; "20-11-2025" ; "SP124, Carlos Lima, carlos@email.com" ; "100, SGA Módulo 2, Prof. Xavier"'

    try:
        part1 = Participacao.criar_participacao(dados_part1)
        part2 = Participacao.criar_participacao(dados_part2)

        print("\nTentando adicionar participações...")

        # 3. Testar o método add_participacao
        proj_novo.add_participacao(part1)
        proj_novo.add_participacao(part2)

        # 4. Verificar se foram adicionadas
        print(f"\nEstado atual do projeto: {proj_novo}")

        # Listar detalhadamente
        proj_novo.listar_participacoes()

    except Exception as e:
        print(f"Erro durante os testes: {e}")

    # 5. Teste de erro (passando objeto inválido)
    print("\nTeste de Validação (Objeto Inválido):")
    try:
        proj_novo.add_participacao(
            "Uma string qualquer, não um objeto Participacao")
    except ValueError as e:
        print(f"Erro esperado capturado: {e}")
