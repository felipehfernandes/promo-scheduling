# Promoções App

Este é um projeto simples de gerenciamento de promoções utilizando Python, arquitetura MVC, e banco de dados PostgreSQL.

## Configurando o Ambiente

1. Clone este repositório para sua máquina local:
   ```bash
   git clone https://github.com/seu-usuario/promocoes-app.git
   cd promo-scheduling
   ```

2. Crie e ative um ambiente virtual:
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```
3. Instale as dependências do projeto:
    ```bash
    pip install -r requirements.txt
    ```
   
4. Configure o banco de dados PostgreSQL:
   - Crie um banco de dados chamado promocoes_db.
   - Atualize o arquivo config.py com suas credenciais do PostgreSQL:

    ```python
    database="promocoes_db",
    user="seu_usuario",
    password="sua_senha",
    host="localhost",
    port="5432"
   ```
   
5. Execute o script para criar a tabela no banco de dados:
    ```bash
    python -c "from models.database import create_tables; create_tables()"
    ```
   
## Executando a Aplicação
Inicie o programa com o seguinte comando:

```bash
python app.py
```

Você verá as opções no menu principal. Escolha a ação desejada e siga as instruções no terminal.

## Estrutura do Projeto

```bash
promocoes_app/
│
├── app.py             # Arquivo principal para rodar a aplicação
├── config.py          # Configuração do banco de dados
├── models/            # Diretório para os modelos
│   ├── __init__.py    # Inicializador do módulo
│   ├── database.py    # Conexão e manipulação do banco de dados
│   └── promocao.py    # Modelo de Promoção
├── controllers/       # Diretório para os controladores
│   ├── __init__.py    # Inicializador do módulo
│   └── promocao_controller.py # Lógica para gerenciar promoções
├── views/             # Diretório para as interfaces
│   ├── __init__.py    # Inicializador do módulo
│   └── promocao_view.py  # Interface com o usuário
├── requirements.txt   # Dependências do projeto
└── README.md          # Documentação do projeto

```