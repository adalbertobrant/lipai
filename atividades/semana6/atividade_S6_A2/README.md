## Manipulação de Dados em Python / Pandas - Pandas Essencial

## Apresentação e ambiente

Para a manipulação de informações usando a biblioteca Pandas, iremos criar ambiente virtual, e instalar diversas ferramentas, uma das maneiras de se fazer isso é utilizando o anaconda.

```bash
    # listagem de ambientes virtuais já criados
        conda env list
    # criação de um novo ambiente virtual
        conda create -n lipai_ufu python=3.13 pandas jupyter
```

Ao digitarmos o comando conda create -n lipai_ufu python=3.13 pandas jupyter, iremos criar um ambiente virtual com as versões atuais do pandas, python 3.13 e também do jupyter, entretanto como podem verificar na imagem abaixo a versão do meu ambiente conda estava desatualizada , então primeiro vamos proceder a atualização do ambiente virtual para depois realizarmos a instalação

![Aviso WARNING mostrando que o ambiente conda está desatualizado](/home/adalberto/github/lipai/imgs/atividade_S6_A2/001.png)

Depois da atualização, podemos continuar com a instalação, veremos a seguinte mensagem na parte final do processo de instalação das bibliotecas e do python:

![Mensagem final do processo de instalação das bibliotecas](/home/adalberto/github/lipai/imgs/atividade_S6_A2/002.png)

## Tipos de dados

Os dados podem ser divididos em dados não estruturados e dados estruturados.

Dados estruturados são aqueles que podemos colocar em uma tabela ou em bancos de dados, podendo ser identificados em linhas e colunas , podem ser números, datas, strings, esses dados requerem uma menor alocação de espaço e são mais fáceis de gerenciar e proteger até mesmo em soluções legadas.

Dados não estruturados são dados que não conseguimos quantificar e qualificar da mesma forma que os dados estruturados, eles podem ser: 

- ​    documentos pdf, imagens, audio, vídeo, planilhas, documentos de editores de texto entre outros.

Esses tipos de dados requerem mais espaço e são mais complexos de gerenciar , proteger e manipular com soluções legadas. 

No pandas iremos trabalhar com os dados estruturados.

### Elementos chave de Dados Estruturados

Ao utilizamos o pandas para descrever uma série de dados podemos encontrar termos comumente utilizados por analistas de dados e programadores esses termos são:

| Termo                              |  Significado                                                            |
| ---                                |  ---                                                                    |
| DataFrame, Table, Rectangular Data |  São a reunião dos dados que estão sendo visualizadas no momento        |
| Amostra,(Sample)                   |  É toda uma linha de nosso dataframe                                    |
| Feature ( característica )         |  São todos os atributos de nossas variáveis de entrada                  |
| Indices                            |  São numerados de zero até um , podendo também ser texto                |
| Series                             |  É uma linha ou coluna de nossa tabela ou dataframe no pandas são arrays|
| Variáveis Independentes            |  Os atributos não dependem de outras variáveis em nosso dataframe       |
| Variáveis Dependentes              |  Dependem de outras variáveis para geração de um output ex: média       |
| População                          |  Os elementos de um universo qualquer, população de pessoas no país     |
| Amostragem                         |  Subconjunto da população selecionado a partir de regras estatísticas   |
| Amostra no pandas                  |  Corresponde a apenas uma única observação de nosso dataframe           |

De maneira geral os Dados podem ser expressados em uma escala numérica (quantitativos), e também categóricos (qualitativos).
Nos dados numéricos, eles podem ser discretos ( aqueles que podemos contar ) ou contínuos ( necessitam de um intervalo de medição ):



| Dados Numéricos    | Discretos           | Contínuos                      |
| ---                |   ---               | ---                            |
|                    | Número de nascidos  | Tempo gasto para parto normal  |
|                    | idade de uma pessoa | Peso de uma pessoa             |

| Dados Categóricos | Nominal          | Ordinal                                   |
| ----------------- | ---------------- | ----------------------------------------- |
|                   | cor do cabelo    | Tamanho da roupa ( P, M, G)               |
|                   | gênero literário | Escala de satisfação ( Ruim, médio, Bom ) |

Em dados categóricos também temos o identificador que é um tipo de dado que possui apenas um indivíduo único relacionado ao identificador , por exemplo cada pessoa tem apenas um cpf.

Observe a figura e veja exemplos relativos aos dados numéricos e categóricos;

![Exemplos de dados](/home/adalberto/github/lipai/imgs/atividade_S6_A2/003.png)

Imagem extraída do youtube no vídeo https://www.youtube.com/watch?v=cC-WWgs7Ilk&list=PL3ZslI15yo2pfkf7EGNR14xTwe-wZ2bNX&index=3&t=658s

## Importando um Dataset com pandas

