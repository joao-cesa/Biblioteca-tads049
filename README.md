# Sistema de Biblioteca

## Sobre o Projeto

Este é um sistema de gerenciamento de biblioteca desenvolvido como projeto acadêmico. O sistema permite o controle completo do acervo de uma biblioteca, com funcionalidades de cadastro, busca, empréstimo e devolução de livros através de uma interface gráfica moderna e intuitiva.



## Participantes

Ruth Camile: Dev <br>
Matheus Henrique: Dev <br>
João César: Dev <br>
Thayanne Stella: Dev <br>
Nicollas Abraão: Dev <br>

## Tecnologias Utilizadas

- Python : Linguagem principal do projeto

- PyQt5 : Framework para desenvolvimento da interface gráfica

- SQLite : Banco de dados para armazenamento das informações

## Como Executar o Projeto

### Pré-requisitos

- Python instalado no computador

- PyQt5 instalado

### Passos para Execução

1. Clone o repositório
```bash
git clone https://github.com/joao-cesa/Biblioteca-tads049.git
```

2. Instale as dependências:
```bash
pip install PyQt5
```

3. Execute o programa:
```bash
python scr/main.py
```

## Funcionalidades

### Gerenciamento de Livros

- Cadastro de livros com:

  - Título

  - Autor

  - Gênero

  - Ano de lançamento

- Sistema de busca por diferentes campos

- Controle de empréstimos e devoluções

### Interface do Usuário

- Design moderno com tema escuro

- Tabela interativa para visualização do acervo

- Campos de busca e filtros

- Botões para ações principais (cadastrar, emprestar, devolver, excluir)

## Estrutura do Projeto

### Arquitetura MVC

- Model : Definição das estruturas de dados

- View : Interface gráfica em PyQt5

- Controller : Lógica de negócios

- Repository : Acesso ao banco de dados

- Service : Regras de negócio

### Banco de Dados

- SQLite com tabela para armazenamento dos livros

- Campos: id, título, autor, gênero, ano_lancamento, emprestado

## Atividades Realizadas

- Implementação da arquitetura MVC

- Desenvolvimento da interface gráfica

- Criação do sistema de busca

- Implementação do controle de empréstimos

- Integração com banco de dados SQLite

## Observações

- O sistema utiliza um arquivo de banco de dados local (biblioteca_0.db)

- A interface foi desenvolvida pensando na usabilidade do usuário
