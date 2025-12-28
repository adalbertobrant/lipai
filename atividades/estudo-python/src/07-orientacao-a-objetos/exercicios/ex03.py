"""
    Exercício 03 - Implementar uma classe Participacao, com os atributos:
    codigo - identificador da participação pode ser inteiro ou string
    data_inicio - data inicial pode ser string
    data_fim - data final pode ser string
    aluno - Objeto da classe Aluno
    projeto - Objeto da classe Projeto associado
"""
# reaproveitamento dos exercícios Aluno e Projeto
from ex01 import Aluno
from ex02 import Projeto


class Participacao:
    """ Classe participação """

    def __init__(self, codigo, data_inicio, data_fim, *dados):
        """ Construtor da classe participação com dois objetos Aluno e Projeto """
        self.codigo = codigo
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.aluno = Aluno.criar_de_string(dados[0])
        self.projeto = Projeto.criar_projeto(dados[1])

    @classmethod
    def criar_participacao(cls, string_participacoes):
        """ cria um objeto participacao a partir de uma string """
        if not string_participacoes or not isinstance(string_participacoes, str):
            raise ValueError("Erro -> a string deve ser válida")
        try:
            partes = [p.strip().strip('"')
                      for p in string_participacoes.split(';')]
            if len(partes) != 5:
                raise ValueError(
                    f"String deve ter 5 partes separadas por ';'. Encontrado: {len(partes)}")
            codigo, data_inicio, data_fim, *dados = partes
            return cls(int(codigo), data_inicio, data_fim, *dados)
        except ValueError as e:
            raise ValueError(f'Erro ao criar participacao: {e}')

    def __str__(self):
        return f'Participacao [ codigo={self.codigo}, data_inicio={self.data_inicio}, data_fim={self.data_fim}, \n  {self.aluno}, \n  {self.projeto}]'


if __name__ == "__main__":
    # teste 01
    print('\n----- Início do Teste Classe Participacao ----\n')
    DATA = '1234 ; "01-10-2025" ; "29-12-2026" ; "SP001, José da Silva, josé@email.com" ; "2, Laboratório de IA, Maria Silva"'

    try:
        participacao = Participacao.criar_participacao(DATA)
        print(participacao)
    except Exception as e:
        print(e)

    # teste 02

    print("\n--- Iniciando Teste 02 (Deve retornar erro) ---")

    DATA_ERRO = '9999;"01-01-2024";"30-06-2024";"SP002, Aluno Sem Email";"3, Projeto X, Prof. Girafales"'

    try:
        participacao_erro = Participacao.criar_participacao(DATA_ERRO)
        print(participacao_erro)
    except ValueError as e:
        print(f"Mensagem de erro capturada: {e}")
