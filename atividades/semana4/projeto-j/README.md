# Documentação Detalhada do Projeto J - Sistema de Chamados de Suporte de TI

## 1. Visão Geral do Projeto

O Projeto J é um sistema de linha de comando (CLI) desenvolvido para registrar e acompanhar chamados de suporte de TI. Ele permite gerenciar usuários que abrem chamados, técnicos que os atendem, setores e os próprios chamados, desde a abertura até a resolução ou cancelamento. O sistema agora inclui um sistema de autenticação de usuários com controle de acesso baseado em funções (administrador e usuário comum). O objetivo principal é fornecer uma ferramenta básica para a gestão de tickets de suporte com níveis de permissão distintos.

## 2. Funcionalidades Implementadas

O sistema oferece as seguintes funcionalidades, conforme especificado no `README.md` original:

*   **Gestão de Usuários:**
    *   Cadastrar novos usuários (CPF, nome, email), selecionando o Setor a partir de uma lista de setores existentes.
    *   Listar todos os usuários cadastrados.
*   **Gestão de Técnicos:**
    *   Cadastrar novos técnicos (nome, email, especialidade), com o ID gerado automaticamente pelo sistema.
    *   Listar todos os técnicos cadastrados.
*   **Gestão de Setores:**
    *   Cadastrar novos setores (nome, ID do gestor), com o ID gerado automaticamente pelo sistema.
    *   Listar todos os setores cadastrados.
*   **Gestão de Chamados:**
    *   Abrir um novo chamado (título, descrição, prioridade, data de abertura, status inicial "aberto"), com o ID gerado automaticamente pelo sistema, associado a um usuário e setor selecionados de listas existentes.
    *   Atribuir um técnico a um chamado existente, selecionando o chamado e o técnico de listas.
    *   Atualizar o status de um chamado existente (aberto, em atendimento, resolvido, cancelado), selecionando o chamado de uma lista.
*   **Relatórios:**
    *   Listar todos os chamados atualmente abertos (disponível para administradores).
    *   Listar chamados específicos de um determinado usuário (Admin), selecionando o usuário de uma lista.
    *   Listar chamados atribuídos a um técnico específico (Admin), selecionando o técnico de uma lista.
    *   Listar meus chamados abertos (Usuário comum).
    *   Listar todos os meus chamados (Usuário comum).

*   **Autenticação e Gerenciamento de Acesso:**
    *   **Login de Usuários:** Autenticação baseada em nome de usuário e senha, utilizando o arquivo `data/senhas.csv`.
    *   **Controle de Acesso Baseado em Funções (RBAC):**
        *   **Administradores:** Têm acesso completo a todas as funcionalidades de gerenciamento (usuários, técnicos, setores, chamados) e a todos os relatórios. Podem também cadastrar e listar contas de acesso.
        *   **Usuários Comuns:** Possuem acesso restrito para abrir novos chamados, listar seus próprios chamados e verificar o status de seus chamados.
    *   **Gerenciamento de Credenciais de Acesso (Admin):** Administradores podem cadastrar novos nomes de usuário, senhas e definir suas funções (administrador ou usuário comum) para o sistema de autenticação.

## 3. Estrutura de Classes e Interações

O projeto é organizado em módulos Python, seguindo um padrão que separa a lógica de negócio (modelos), a persistência de dados (repositórios), os relatórios e a interface do usuário.

### Módulos Principais:

*   **`main.py`**:
    *   É o ponto de entrada da aplicação.
    *   Gerencia o processo de login e autenticação de usuários.
    *   Contém o menu principal e submenus dinâmicos para cada funcionalidade (usuários, técnicos, setores, chamados, relatórios), adaptando as opções com base na função do usuário autenticado.
    *   Inclui funções auxiliares (`exibir_lista_com_indices`, `selecionar_opcao_por_lista`) para facilitar a seleção de entidades por meio de listas numeradas.
    *   Orquestra as interações com o usuário, chamando os métodos apropriados dos repositórios e do módulo de relatórios.
    *   Instancia os repositórios (`RepositorioUsuarios`, `RepositorioTecnicos`, `RepositorioSetores`, `RepositorioChamados`, `RepositorioAutenticacao`) no início da execução.

*   **`models/`**:
    *   Contém as definições das classes de domínio do sistema, implementadas como `dataclasses` para clareza e concisão.
    *   **`Usuario`**: Representa quem abre o chamado. Possui `cpf` (identificador), `nome`, `email` e `id_setor`. Inclui validação básica no `__post_init__` e um método de fábrica `criar_de_string` para parsing de CSV.
    *   **`Setor`**: Representa um departamento. Possui `id`, `nome` e `id_gestor`. Inclui validação e `criar_de_string`.
    *   **`Tecnico`**: Representa o profissional de TI. Possui `id`, `nome`, `email` e `especialidade`. Inclui validação e `criar_de_string`.
    *   **`Chamado`**: Representa um ticket de suporte. Possui `id`, `usuario` (CPF do solicitante), `titulo`, `descricao`, `id_setor_local`, `prioridade` (Enum), `id_tecnico` (opcional), `status` (Enum), `data_abertura` e `data_fechamento` (opcional). Utiliza Enums para `Prioridade` e `StatusChamado` e `datetime` para as datas. Inclui validação e `criar_de_string` para parsing complexo de CSV.

*   **`repositorio/`**:
    *   Contém as classes responsáveis pela persistência dos objetos de modelo em arquivos CSV, localizados no diretório `data/`.
    *   Cada classe de repositório (`RepositorioUsuarios`, `RepositorioTecnicos`, `RepositorioSetores`, `RepositorioChamados`, `RepositorioAutenticacao`) encapsula a lógica de leitura e escrita para seu respectivo arquivo CSV.
    *   Implementam métodos como `obter_todos()`, `adicionar(objeto)`, e `buscar_por_id(id)`. O `RepositorioAutenticacao` gerencia as credenciais de acesso.
    *   Utilizam métodos privados `_ler_` e `_escrever_` para gerenciar a leitura e reescrita completa dos arquivos CSV, garantindo a integridade dos dados (para este projeto, o arquivo é lido, modificado em memória e reescrito completamente).
    *   **Interação Chave**: Os repositórios utilizam o módulo `csv` do Python para leitura (`csv.reader` em `criar_de_string`) e escrita (`csv.writer` em `_escrever_`) para garantir que campos com vírgulas sejam tratados corretamente (escapados/desescapados).

*   **`relatorio/relatorios.py`**:
    *   Contém funções para gerar relatórios com base nos dados dos chamados.
    *   Depende do `RepositorioChamados` para obter os dados.
    *   Funções implementadas: `listar_chamados_abertos()`, `listar_chamados_por_usuario(cpf)`, `listar_chamados_por_tecnico(id_tecnico)`.
    *   Os relatórios são impressos diretamente no console.

## 4. Tratamento de Erros

O projeto incorpora um tratamento de erros básico, focado principalmente na validação de entrada de dados e na robustez da leitura de arquivos CSV:

*   **Validação de Modelos:** As classes de modelo (`Usuario`, `Setor`, `Tecnico`, `Chamado`) possuem o método `__post_init__` que valida os atributos no momento da criação do objeto. Entradas inválidas (e.g., CPF com formato incorreto, nome vazio, ID negativo) levantam `ValueError`.
*   **Autenticação:** O sistema de login trata credenciais inválidas, impedindo o acesso e informando o usuário sobre a falha na autenticação.
*   **Parsing de CSV:** O método `criar_de_string` em cada modelo utiliza blocos `try-except` para capturar `ValueError` durante a conversão de strings para tipos numéricos ou datas, ou quando há um número incorreto de campos na linha CSV.
*   **Leitura de Arquivos:** Os métodos `_ler_` dos repositórios utilizam blocos `try-except` ao chamar `criar_de_string` para cada linha do CSV, imprimindo uma mensagem de erro para linhas malformadas sem interromper a leitura do restante do arquivo.
*   **Tratamento Robusto de CSV:** A integração do módulo `csv` (com `csv.reader` e `csv.writer`) garante que caracteres especiais como vírgulas dentro dos campos dos arquivos CSV sejam tratados corretamente, evitando erros de "too many values to unpack" ao ler dados.
*   **Menus:** Os menus em `main.py` capturam `ValueError` e `KeyError` (para Enums inválidos) durante a entrada do usuário ou criação de objetos, informando o usuário sobre a entrada inválida.

## 5. Próximos Passos e Melhorias

Para evoluir o Projeto J, as seguintes melhorias são sugeridas:

*   **Interface de Usuário (UI):** A CLI atual é funcional, mas básica. Uma interface mais interativa (utilizando bibliotecas como `prompt_toolkit` ou `rich`) ou até mesmo uma interface web (com Flask, Django ou FastAPI) poderia melhorar drasticamente a experiência do usuário.
*   **Persistência de Dados:** A utilização de arquivos CSV é simples para um protótipo, mas pode ser ineficiente e propenso a erros em um ambiente real (concorrência, volume de dados). Migrar para um banco de dados (e.g., SQLite para uma solução embarcada, PostgreSQL ou MySQL para um sistema mais robusto) com um ORM (e.g., SQLAlchemy) melhoraria a integridade, performance e capacidade de consulta dos dados.
*   **Tratamento de Erros Mais Sofisticado:** Implementar um sistema de logging mais robusto (módulo `logging` do Python) para registrar erros e eventos, em vez de apenas `print()` para o console. Definir exceções personalizadas para cenários específicos.
*   **Validação de Dados Aprimorada:**
    *   **Chaves Estrangeiras:** Implementar validação para garantir que `id_setor` em `Usuario` e `Chamado`, e `id_tecnico` em `Chamado`, realmente existam nos respectivos repositórios antes de cadastrar.
    *   **Formatos:** Validações mais rigorosas para email (regex), datas, etc.
*   **Geração Automática de IDs:** A geração automática de IDs para Chamados, Técnicos e Setores foi implementada, eliminando a entrada manual de IDs. Melhorias adicionais podem incluir:
    *   Utilização de UUIDs: Para garantir IDs globalmente únicos em ambientes distribuídos.
    *   Persistência de contador: Para garantir que os IDs sequenciais continuem mesmo após reinícios do sistema.
*   **Funcionalidades CRUD Completas:** Adicionar operações de "Atualizar" (além de status/técnico para chamados) e "Excluir" para todas as entidades (Usuário, Técnico, Setor, Chamado).
*   **Funcionalidades de Busca e Filtro:** Expandir as capacidades de relatório com opções de busca e filtro mais flexíveis (e.g., buscar chamados por palavra-chave na descrição, filtrar por intervalo de datas, combinar múltiplos critérios).
*   **Autenticação e Autorização:** Um sistema básico de autenticação e controle de acesso foi implementado. Melhorias futuras incluem:
    *   Criptografia de senhas: As senhas estão atualmente armazenadas em texto simples no `senhas.csv`. Implementar hashing de senhas (e.g., usando `bcrypt` ou `scrypt`) para maior segurança.
    *   Gestão de sessões: Para aplicações web ou mais complexas, a gestão de sessões se faz necessária.
    *   Controle de acesso mais granular: Implementar permissões mais finas para diferentes ações, em vez de apenas dois papéis.
    *   Interface de gerenciamento de usuários de acesso: Aprimorar a CLI para gerenciar usuários de acesso de forma mais robusta (editar, desativar, redefinir senha).
*   **Testes Automatizados:** Desenvolver uma suíte abrangente de testes unitários e de integração para todas as classes e funcionalidades, utilizando um framework como `unittest` ou `pytest`, para garantir a estabilidade e facilitar futuras modificações.
*   **Documentação de Código:** Adicionar docstrings detalhadas a todas as classes, métodos e funções para descrever seu propósito, argumentos e retornos, melhorando a manutenibilidade do código.

Esta documentação serve como um guia abrangente sobre a implementação atual do Projeto J e um roteiro para seu crescimento futuro.
