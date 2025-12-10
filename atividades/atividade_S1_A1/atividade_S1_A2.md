## The Linux Command Line 6th, Internet Edition -> https://sourceforge.net/projects/linuxcommand/

# Capítulo 1 

## Primeiro contato com o terminal 

```
# escrevendo qualquer coisa no terminal e observando a resposta
comandoDigitado
-bash: comandoDigitado: command not found
```
. Anotação
    Aparece uma mensagem de erro pois não é localizada a informação no sistema

![Primeiro Comando Digitado no Terminal Linux](/home/adalberto/github/lipai/imgs/comando_zero.png)

## Alguns comandos simples no terminal linux

|  Comando | Função | Observações |
| :---     | :---   | :---        |
| date     | Mostra a data no terminal | a data que aparece é completa e depende do que foi configurado no sistema|
| uptime   | Mostra o tempo que o pc está em atividade | um dado interessante é que o uptime mostra a carga que está no pc sendo 1.0 para carga de 100% como meu pc tem 4 cores a carga está ok, no uptime também consigo ver o que estava carregado nos tempos de 1 minutos, 5 minutos  e 15 minutos |
| df       | Mostra a quantidade de espaço livre no hd | gosto de usar a opção df -hT que me mostra de maneira mais fácil de entender |
| free     | Mostra a quantidade de memória livre no sistema | algumas vezes o sistema trava devido ao google-chrome e o free me ajuda a ver esses dados |

![Comandos date, uptime, df e free em ação](/home/adalberto/github/lipai/imgs/comandos_date_uptime_df_free.png)

## Saindo do terminal 

 . Para sair do terminal ou encerrar o mesmo usamos o comando exit
 ```
 # saída do terminal linux 
 exit
 ```
## Curiosidades
 . É importante notar que podemos abrir diversos terminais no linux mesmo que não estando em modo gráfico através da combinação de teclas Ctrl + Alt + tecla de função F1 até F6, em quase todas as distribuições.
 . Para mudar de ambiente e ir para outro pode ser usar a combinação da tecla Alt + tecla do ambiente original que foi inicialmente usado , se usou Ctrl + Alt + F1 e depois Ctrl + Alt + F2 , ao apertar Alt + F1, iremos para o ambiente gerado no F1.
 . Notar que cada distribuição linux pode ter um detalhe diferente nessa parte, na versão Ubuntu 24.04 no meu pc ao fazer Ctrl + Alt + F1 eu fecho a área de trabalho 

# Capítulo 2 

## Navegação 

 . Os comandos básico de navegação no terminal linux são:
 ```
 # mostra o diretório que estamos atualmente
 pwd

 # Muda o diretório atual
 cd novo_diretório

 # Lista o diretório atual, com todas as 'coisas' dentro.

 ls -alsht 
 ```
![Comandos pwd, cd , ls -alsht](/home/adalberto/github/lipai/imgs/comandos_pwd_cd_ls.png)

 . A árvore de diretórios dos sistemas baseados em Unix , considera apenas um diretório central e embaixo dele cria diferentes ramos para cada necessidade.

                                                 diretório raiz
                                                 |          |
                                  outros diretórios        / \home
                                       /                      \ user1
 ![Comando tree mostrando uma arvóre do diretório de trabalho do usuário adalberto](/home/adalberto/github/lipai/imgs/comando_tree.png)

 . Ao fazermos uma navegação podemos usar o cd caminho do diretório que queremos ir usando o caminho absoluto que é o caminho desde o diretório raiz até o diretório destino ou então podemos usar um caminho relativo usando ' . ' ou " .. " , dependendo de onde quer ir.

 ```
 # caminho absoluto
 cd /caminho absoluto

# caminho relativo 
 cd ./bin 
 ```
![Comando cd para caminho absoluto e relativo](/home/adalberto/github/lipai/imgs/comando_caminhos_absoluto_relativo.png)

# Capítulo 3

| Comando | Função,Observações                                                              |
| :---    | :---                                                                            |
|  ls -a  |  Lista todos os arquivos, mostra inclusive os arquivos ocultos que começam com  |
|  ls -l  |  Formato longo,"Exibe permissões, dono, tamanho e data. É o que mais uso para ver detalhes"  |
|  ls -h  |  Tamanho legível,"Mostra o tamanho em K, M, G (humano) em vez de bytes. Gosto de usar junto com o -l (ls -lh)"  |
|  ls -r  |  Inverte a ordem,Útil para ver os últimos arquivos se combinado com ordenação por tempo  |
|  ls -S  |  Ordena por tamanho,Ajuda a achar arquivos grandes  |
|  ls -t  |  Ordena por tempo,Mostra os modificados recentemente primeiro  |

```
# listando arquivos com detalhes, tamanho legível e ordenado por tempo (mais recentes no fim)
ls -lhtr

# a opção r é que mostra a reversão 
```
![Comando ls -lhtr](/home/adalberto/github/lipai/imgs/comando_ls_arquivos.png)

## Descobrindo o tipo de arquivo e visualizando conteúdo

. No Linux, a extensão do arquivo (como .txt ou .jpg) não importa tanto. Para saber o que o arquivo realmente é, usamos o comando file. . Para ler arquivos de texto longos sem abrir um editor, usamos o less.

```
# mostra os dados do arquivo comando_ls_arquivos.png
   
   file comando_ls_arquivos.png
# mostra os dados do arquivo , como é um arquivo de imagem mostra a dimensão, o tipo de cor, o padrão de cor no caso RGBA de 8 bits 
```
![Comando file em ação](/home/adalberto/github/lipai/imgs/comando_file.png)

## Comando less

 . faz a listagem do conteúdo de um arquivo que é muito grande para se ver de uma vez só no terminal. 
 |  Comando  |  Função                               |
 | :---      | :---                                  |
 | q         | faz a saída do less                   |
 | /texto    | procura um texto que está no arquivo  |
 |  G        | vai para o final do arquivo           |
 | 1G        | vai para o início do arquivo          |

## Estrutura de diretórios do linux

|  Diretório  |  Função  |  Observações  |
| :---        | :---     | :---          |
| /           | Raiz do sistema  |  Tudo começa aqui  |
| /bin        | Binários essenciais  |  "Onde ficam comandos como ls, cp, mv"  |
| /etc        | Configurações  |  Onde ficam os arquivos de configuração do sistema (quase tudo texto)  |
| /home       | Arquivos dos usuários  |  Onde fica a minha pasta /home/adalberto e meus documentos  |
| /root       | Home do superusuário  |  Área restrita do administrador (root)  |
| /var        | Arquivos variáveis  |  Onde ficam logs (/var/log) e arquivos que mudam constantemente  |
| /usr        | Recursos do sistema  |  Onde ficam os programas instalados para usuários (/usr/bin)  |

# Capítulo 4

## Manipulando Arquivos e Diretórios. 

## Usando Curingas (Wildcards)

. O shell usa caracteres especiais para selecionar grupos de arquivos rapidamente.

| **Curinga** | **Significado**        | **Observações**                                              |
| ----------- | ---------------------- | ------------------------------------------------------------ |
| `*`         | Qualquer caractere     | O mais usado. `rm *.html` apaga todos os html. Cuidado com o espaço! 444 |
| `?`         | Um único caractere     | Útil quando os nomes variam apenas por uma letra ou número 5 |
| `[ ]`       | Conjunto de caracteres | `[abc]*` pega arquivos começando com a, b ou c 6             |
| `[:digit:]` | Apenas números         | Uso para filtrar arquivos que têm números no nome 7          |

## Copia todos os arquivos que terminam com .txt para a pasta Documentos

```
cp *.txt Documentos/

```
## Criar um diretório

```
mkdir novo_diretório

# ou 

mkdir ~/github/lipai/novo_diretorio

```
## Copia arquivos de um local 

```
   cp /home/user/adalberto/texto.txt ~/github/lipai/novo_diretorio

```
## Move arquivos e renomeia se for no mesmo diretório

```
   # renomeia arquivo
   mv arquivo.txt novo_nome_arquivo.txt 
   # move arquivo para outro diretório
   mv arquivo.txt /diretório_novo/arquivo.txt
```
## Apaga um arquivo pode ser recursivo (r)

```
  # apaga os arquivos txt que estão no diretório e nos subdiretórios
  rm -rf *.txt

  # apaga um arquivo 
  rm arquivo.txt
```
## Links (Hard e Simbólicos). 
 . O comando ln cria links. 
 . Existem dois tipos: Hard Links (antigos, não podem cruzar partições) e Links Simbólicos (mais modernos, parecem atalhos do Windows)

| **Tipo**      | **Comando**          | **Observações**                                              |
| ------------- | -------------------- | ------------------------------------------------------------ |
| Hard Link     | `ln arquivo link`    | Os dois arquivos são idênticos e apontam para o mesmo lugar no disco |
| Symbolic Link | `ln -s arquivo link` | Se apagar o link, o arquivo original fica lá                 |

# Capítulo 5

## Trabalhando com Comandos

. Até agora usamos uma série de comandos "misteriosos". [cite_start]Neste capítulo, vamos tirar esse mistério e descobrir o que eles realmente são. [cite: 3, 4]
. [cite_start]Um comando pode ser: um programa executável (binário), um comando interno do shell (builtin), uma função do shell ou um alias. [cite: 18]

## Identificando Comandos

. É útil saber exatamente que tipo de comando estamos usando. O Linux nos dá ferramentas para descobrir isso.

| Comando | Função | Observações |
| :---    | :---   | :---        |
| type    | Mostra o tipo do comando | [cite_start]Descobri que o `ls` na verdade é um alias para `ls --color=auto` no meu sistema [cite: 31, 40] |
| which   | Mostra onde está o executável | Ele mostra o caminho completo (ex: /usr/bin/cp). [cite_start]Só funciona para programas reais, não para comandos internos como o `cd` [cite: 42, 47] |

```bash
# Verificando o que é o comando ls
type ls
# Saída: ls is aliased to `ls --color=auto'

# Verificando onde está o executável do navegador
which firefox

## Conseguindo Ajuda (Documentação)
. O Linux possui muita documentação embutida. Não precisamos decorar tudo, apenas saber onde procurar.



```

| **Comando** | **Função**             | **Observações**                                              |
| ----------- | ---------------------- | ------------------------------------------------------------ |
| help        | Ajuda para builtins    | Uso para comandos internos do shell como `cd` ou `exit`, que não têm manual comum |
| --help      | Resumo de uso          | A maioria dos programas aceita isso (ex: `mkdir --help`) para mostrar as opções rapidamente |
| man         | Manual completo        | O `man ls` mostra tudo. Uso as setas para ler e a tecla `/` para pesquisar um texto lá dentro |
| apropos     | Pesquisa no manual     | Útil quando não sei o nome do comando, mas sei o que quero fazer. Ex: `apropos partition` |
| whatis      | Descrição de uma linha | Mostra um resumo muito breve do que o comando faz            |

## Criando meus próprios comandos (Alias)

. Podemos criar nossos próprios comandos usando o `alias`.  . Um truque legal antes de criar o alias é saber que podemos usar `;` para colocar vários comandos numa linha só.

```
# Criando um comando chamado 'foo' que entra em /usr, lista o conteúdo e volta para onde eu estava
alias foo='cd /usr; ls; cd -'

# Para remover o alias criado
unalias foo
```

 . Aliases criados diretamente no terminal somem quando fecho a janela (sessão). Depois aprenderei a salvar eles para sempre nos arquivos de inicialização.
