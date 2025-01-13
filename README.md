# Django REST API

Django REST API é um projeto desenvolvido em Django com o Django Rest Framework, focado na criação de uma API RESTful para gerenciar dados e servir como backend para qualquer aplicação frontend. Este repositório contém a base de uma API para gerenciar diferentes recursos (como livros, usuários, etc.) com operações básicas de CRUD.

## Funcionalidades

- Cadastro de recursos (como livros, usuários, etc.)
- Leitura de dados: exibe a lista completa de itens cadastrados e permite visualizar detalhes
- Atualização de registros existentes
- Exclusão de itens
- Autenticação e autorização utilizando JWT
- Documentação automática da API com drf-yasg

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **Django**: Framework web para criação da API.
- **Django Rest Framework**: Biblioteca para a construção de APIs RESTful.
- **SQLite**: Banco de dados utilizado para persistência de dados (pode ser alterado para outro, como PostgreSQL, se desejado).
- **drf-yasg**: Geração automática de documentação da API.
- **djangorestframework-simplejwt**: Implementação de autenticação JWT para os usuários.

## Instalação

Para executar o Django REST API em sua máquina local, siga os passos abaixo:

1. Clone o repositório:

   ```bash
   git clone https://github.com/jvdellolio/Django_Rest_API.git
   cd Django_Rest_API

   2. Crie um ambiente virtual:

   ```bash
   python -m venv env
3. **Ative o ambiente virtual**:

   - Para Windows:

     ```bash
     env\Scripts\activate
     ```

   - Para Linux/Mac:

     ```bash
     source env/bin/activate
     ```

4. **Instale as dependências**:

   ```bash
   pip install -r requirements.txt
   ```
   5. **Faça push para a branch**:

   ```bash
   git push origin feature/nome-da-feature
   ```

   6. **Abra um Pull Request**:

   - Vá para a página do seu repositório forked no GitHub.
   - Clique no botão **Compare & pull request**.
   - Descreva suas alterações e clique em **Create pull request**.

## Licença

Este projeto está licenciado sob a MIT License. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

## Autor

João Vitor Lima Dell'Olio - [jvdellolio](https://github.com/jvdellolio)

