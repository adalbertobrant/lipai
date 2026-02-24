##Saindo do zero com Numpy

### Instalando a biblioteca Numpy no Linux Ubuntu 24.04 em um ambiente com o Anaconda 

1- Primeiro devemos criar um novo ambiente com o comando conda no terminal :

~~~bash
    conda create -n nome_do_ambiente python=3.12 
~~~

2- Acessar o site do [https://numpy.org/](Numpy.org)

Ao entrar no site podemos ver em destaque a versão atual do Numpy, bem como um espaço para o aprendizado mais profundo do mesmo, exemplos técnicos e muitas informações relevantes.

3- Instalando o Numpy:
    Podemos instalar o Numpy usando um ambiente conda como demonstrado abaixo:

~~~bash
    conda activate nome_do_ambiente
    conda install numpy
~~~

Entretanto podemos utilizar o próprio python para criar um ambiente virtual e instalar a biblioteca numpy da seguinte forma:

~~~bash
    # criar um diretório 
    mkdir nome_do_diretório
    # ir para o diretório nome_do_diretorio
    cd nome_do_diretorio
    # criar um ambiente dentro do diretório nome_do_diretorio
    python3 -m venv nome_do_ambiente
    # instalar o numpy
    pip3 install numpy
~~~

Após a instalação o nosso sistema ficará dessa forma abaixo:

![Histórico da Instalação](../../../imgs/atividade_S6_A1/001.png)

Na imagem percebemos que estamos no ambiente virtual chamado estudo_numpy

Podemos verificar se a instalação do Numpy está correta, chamado dentro do terminal o python e depois importando a biblioteca numpy da seguinte forma:
~~~bash
	python
	import numpy as np
	print(np.__version__)
~~~

Ao rodarmos dentro do ambiente do python esse comando teremos o seguinte resultado, como indica a imagem abaixo:

![terminal do python importando e verificando a versão do numpy](../../../imgs/atividade_S6_A1/002.png)

### Conceitos básicos Numpy

1- O Array em Numpy
    É um conjunto de dados, que pode estar disposto em dimensões diferentes, 1 , 2, 3,..., n dimensões diferentes. No numpy temos então uma estrutura de dados que representa essas diferentes possibilidades que é o ndarrays -> Onde n é número d é dimensões:

| Tipo de array                                   | Nome         |
| ----------------------------------------------- | ------------ |
| 1-D array -> array de apenas uma única dimensão | É um vetor   |
| 2-D array -> array de duas dimensões            | É uma matriz |
| 3-D array -> array de 3 ou mais dimensões       | É um tensor  |

2- Definindo um array em numpy

~~~bash
    # abrir o python
    python
    # importar a biblioteca numpy como np
    import numpy as np
    # definir uma variável e criar um objeto do tipo array() em numpy
    a = np.array([1,2,3,4,5,6,7,8,9,10])
    print(a)
~~~

Essa é uma forma de criar os dados manualmente, utilizando a biblioteca numpy.


