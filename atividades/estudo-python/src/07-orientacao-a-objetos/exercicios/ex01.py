""" Exercício 01 - Implementar uma classe Aluno com atributos (prontuário, nome, email) 
    O objeto aluno pode ser criado com uma string do tipo 'prontuário, nome, email'
    Nenhum atributo pode ser vazio ou nulo, usar @property e @setters 
    dois alunos são iguais se tiverem o mesmo prontuário, implementar o método __eq__
    implementar __hash__ para usar alunos em sets ou chaves de dicionário """


class Aluno():
    """ Classe aluno com os atributos prontuario, nome, email """

    def __init__(self, prontuario, nome, email):
        """ método construtor com prontuário, nome, email """
        self.prontuario = prontuario
        self.nome = nome
        self.email = email

    @classmethod
    def criar_de_string(cls, dados_str):
        """
        Cria um objeto Aluno a partir de uma string no formato 'prontuario, nome, email'.
        Exemplo: Aluno.criar_de_string("SP001, Maria, maria@email.com")
        """
        if not dados_str or not isinstance(dados_str, str):
            raise ValueError("Dados incorretos.")
        try:
            prontuario, nome, email = [item.strip()
                                       for item in dados_str.split(',')]
            # Retorna uma nova instância da classe (cls)
            return cls(prontuario, nome, email)
        except ValueError:
            raise ValueError(
                "A string deve estar no formato: 'prontuario, nome, email'")

    @property
    def prontuario(self):
        """ retorna o prontuário """
        return self._prontuario

    @prontuario.setter
    def prontuario(self, valor):
        """ atribui valor e testa para o prontuário """
        if not valor or not str(valor).strip():
            raise ValueError("O prontuário não pode ser vazio ou nulo.")
        self._prontuario = valor

    @property
    def nome(self):
        """ retorna o nome do aluno """
        return self._nome

    @nome.setter
    def nome(self, valor):
        """ atribui e testa valor para o nome do aluno """
        if not valor or not str(valor).strip():
            raise ValueError("O nome não pode ser vazio ou nulo.")
        self._nome = valor

    @property
    def email(self):
        """ retorna o email """
        return self._email

    @email.setter
    def email(self, valor):
        """ testa e seta o valor do email """
        if not valor or not str(valor).strip():
            raise ValueError("O email não pode ser vazio ou nulo.")
        self._email = valor

    def __eq__(self, outro):
        """ Dois alunos são iguais se tiverem o mesmo prontuário """
        if isinstance(outro, Aluno):
            return self.prontuario == outro.prontuario
        return False

    def __hash__(self):
        """ Necessário para usar objetos Aluno em sets ou chaves de dicionário """
        return hash(self.prontuario)

    def __repr__(self):
        """ Representação do objeto """
        return f"Aluno(prontuario='{self.prontuario}', nome='{self.nome}', email='{self.email}')"

    def __str__(self):
        """ Retorna a string aluno """
        return f"Aluno [ prontuario = {self.prontuario}, nome = {self.nome}, email = {self.email}]"


aluno1 = Aluno('sp001', 'José da Silva', 'jose@email.com')
print(aluno1)
print('----')

aluno2 = Aluno.criar_de_string("SP30394, Maria Silva, maria@ufu.br")
print(aluno2)
