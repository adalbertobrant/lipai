    **Nome**: Adalberto Caldeira Brant Filho
    **Repositório GitHub**: https://github.com/adalbertobrant/lipai
    
    **Código das Videoaulas**:

    
     1. Instalação do ambiente alternativo ao vscode o vscodium para ubuntu usando o snap

     ```
         snap install codium --classic

     ```
    2. Criação da pasta de estudo para a atividade A1

    ```
        mkdir estudo-python

    ```
    3. Criação da pasta ./estudo-python/src , usando o vscodium gui

    4. Instalação das extensões 
    |  Nome da extensão  | funcionalidade  |
    | :---               | :---            |
    |  ms-python         |  extensão para utilizar o python no vscodium  |
    |  pylint            |  extensão para boas práticas da linguagem     |
    |  autopep8          |  extensão de condutas e normas da linguagem python  |

    5. Upload do projeto para o github

    ## Aula 02 - Keywords e identificadores

    # Keywords
      São palavras reservadas apenas utilizadas pelo python e não podem ser utilizadas pelo usuário para a declaração de variáveis e outras funcionalidades 
      ```
      # algumas palavras reservadas
      true, false, none, import, if, lambda
      ```
    # Identificadores
      São as palavras de nome de variáveis, funções, classes,eles são case sensitive ou seja existe diferença entre letras maiusculas ou minúsculas. 
      Todos os identificadores podem começar com underline _ ou uma letra, não podem ter espaços em branco entre um identificador composto por exemplo:
      ```python3
      nome de variável
      # no caso o certo seria nome_de_variavel
      nome = 'Maria'
      idade = 30
      Nome = 'João'
      nome_completo = 'Maria da Silva'
      ```
      Não se pode usar caracteres especiais nos nomes(identificadores) tais como #, !, @, $
      Uma boa prática da linguagem é utilizar sempre identificadores claros e que tenham significado para o que a variável está fazendo.
      Na definição de constantes ou seja variáveis que não mudam o correto é usar letras maiusculas:
      ```python3
      PI = 3.14
      
      idade = 18

      MAIORIDADE = 18

      if idade >= MAIORIDADE:
          print('Maior de idade')
      else:
          print('Menor de idade')
      ```

    ## Aula 3 - Comentários

    Podem ser apenas de uma única linha

    ```
     # comentário com uma única linha
    ```

    ```
    '''
    Comentários com várias linhas
    comentários com várias linhas
    comentários com várias linhas
    '''
    ```

    O comentário deve ser usado sempre que o código não estiver autoexplicativo

