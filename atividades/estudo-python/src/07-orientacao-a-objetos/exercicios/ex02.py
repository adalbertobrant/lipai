"""
 Exercício 02 - Implementar uma classe Projeto com código, título, responsável, 
código é número inteiro, nenhum dos atributos pode ser nulo, use @property , o objeto
projeto deve ser construído também como uma string do tipo "1,Laboratório de Desenvolvimento de
Software,Pedro Gomes", nenhum atributo pode ser nulo ou vazio, o código deve ser número inteiro.
Dois projetos são iguais se tiverem o mesmo código, implementar __eq__ comparando com o código
 """


class Projeto:
    """ Classe Projeto  """

    def __init__(self, codigo, titulo, responsavel):
        # Ao atribuir aqui, já acionamos os setters para validar
        self.codigo = codigo
        self.titulo = titulo
        self.responsavel = responsavel

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

    def __eq__(self, other):
        """ Dois projetos são iguais se tiverem o mesmo código """
        if isinstance(other, Projeto):
            return self.codigo == other.codigo
        return False

    def __str__(self):
        return f'Projeto [Código: {self.codigo}, Título: "{self.titulo}", Responsável: {self.responsavel}]'


if __name__ == "__main__":
    print('-----\nTestes do Projeto\n----')
    # 1. Teste normal (Construtor)
    try:
        p1 = Projeto(1, 'Lab Software', 'Pedro Gomes')
        print(f"P1 criado: {p1}")
    except ValueError as e:
        print(f"Erro P1: {e}")

    # 2. Teste via String
    try:
        entrada = "2, Laboratório de IA, Maria Silva"
        p2 = Projeto.criar_projeto(entrada)
        print(f"P2 criado via string: {p2}")
    except ValueError as e:
        print(f"Erro P2: {e}")

    # 3. Teste de Igualdade
    p3 = Projeto(1, "Outro Nome", "Outra Pessoa")  # Mesmo código que P1
    print(f"P1 é igual a P3 (mesmo código) ?  {p1 == p3}")  # Deve ser True

    # 4. Teste de Erro (Título Vazio)
    try:
        p_erro = Projeto(3, "", "Joao")
    except ValueError as e:
        print(f"Erro esperado capturado: {e}")

    print('----')
