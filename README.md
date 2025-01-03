# Promo Scheduling

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

4. Execute o script para criar a tabela no banco de dados:
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
├── app.py
├── config.py
├── models/
│   ├── __init__.py
│   ├── database.py
│   └── promocao.py
├── controllers/
│   ├── __init__.py
│   └── promocao_controller.py
├── views/
│   ├── __init__.py
│   └── promocao_view.py
├── requirements.txt
└── README.md


```
