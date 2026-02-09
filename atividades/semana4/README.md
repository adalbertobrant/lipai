# Projeto J – Sistema de Chamados de Suporte de TI 

Desenvolver um sistema para registrar e acompanhar chamados de suporte de TI
(problemas em computadores, rede, sistemas etc.).

Funcionalidades obrigatórias

● Cadastrar e listar usuários (quem abre chamado).
● Cadastrar e listar técnicos (quem atende chamados).
● Abrir chamado:
○ usuário, título, descrição, prioridade, data de abertura, status inicial
(“aberto”).
● Atribuir um técnico a um chamado.
● Atualizar status do chamado (aberto, em atendimento, resolvido, cancelado).
● Listar:
○ Chamados abertos.
○ Chamados de um determinado usuário.
○ Chamados atribuídos a um técnico.

Classes sugeridas

●Setor – id, nome, id_gestor
●Usuario – id, nome, email, id_setor.
●Tecnico – id, nome, email, especialidade.
●Chamado – id, usuario, id_tecnico (pode começar como None), titulo, descricao,
prioridade, data_abertura, data_fechamento, status, id_setor_local (setor).



Módulos sugeridos

●main.py – menus (usuários, técnicos, chamados).
●models.py – classes.
●repositorio_usuarios.py, repositorio_tecnicos.py, repositorio_chamados.py, repositorio_setores.py.
●relatorios.py – listagens por status, por usuário, por técnico.

Arquivos de dados

● data/usuarios.csv
● data/tecnicos.csv
● data/chamados.csv
●  data/setores.csv



[ Link projeto -j ] (https://github.com/adalbertobrant/lipai/tree/main/atividades/semana4/projeto-j) | PROJETO - J |
