# Usuário API

Este projeto apresenta uma API para o registro e manipulção de informações de um usuário. desenvolvida em Python utilizando as tecnologias flask, SQLAlchemy, typing, Docker e PostgreSQL. O objetivo da aplicação é realizar operações CRUD (Criar, Ler, Atualizar, Deletar) sobre dados de usuários em um banco de dados.

## Funcionalidades

A API oferece as seguinte funcionalidades:
### 1. Adicionar um usuário
-  **URL**: `POST /usuarios`
- **Descrição**: Cria um novo usuário.
- **Requisição**:
    ```json
    {
    "name": "John Connor",
    "email": "John@Skynet.com",
    "password": "exterminator123"
    }
    ```

### 2. Buscar usuário pelo ID
-  **URL**: `GET /usuarios/{ID}`
- **Descrição**: Retorna um usário especifico.
- **Resposta de sucesso**:
    ```json
    {
    "email": "John@Skynet.com",
    "id": 1,
    "is_active": true,
    "name": "John Connor"
  }
    ```
### 3. Atualiza cadastro usuário
-  **URL**: `PUT /usuarios/{ID}`
-  **Descrição**: Atualiza um usuário existente.
-  **Requisição**:
    ```json
    {
    "name": "Ellen Ripley",
    "email": "Ellen@Weyland.com",
    "password": "alien8"
    }
    ```
- **Resposta de sucesso**:
  ```json
    {
    "email": "Ellen@Weyland.com",
    "id": 1,
    "is_active": true,
    "name": "Ellen Ripley"
  }
  ```

### 4. Deletar um usuário
- **URL**: `DELETE /usuarios/{ID}`
- **Descrição**: Deleta um usuário existente.

### 5. Listar todos os usuários
-  **URL**: `GET /usuarios`
- **Descrição**: Retorna uma lista com todos os usuarios registrados.


## Executando a aplicação

_Atenção: Garanta que você tenha o Docker instalado em sua máquina._

- Acessando o [GitHub do projeto](git@github.com:Herick2D/flask-api.git), faça o clone do mesmo;
- Acesse a pasta do projeto e execute o comando `docker-compose up --build` para criar a imagem do container e subir a aplicação;

## Observações

Esta aplicação foi desenvolvida como uma Prova de Conceito (POC) em um ambiente de estudos. Como tal, algumas funcionalidades e descrições podem ser limitadas, e o comportamento da aplicação pode não ser completamente previsível. Bugs ou falhas podem ocorrer. Caso encontre algum problema, por favor, registre uma issue no repositório do projeto para que possamos analisar e aprimorar.
