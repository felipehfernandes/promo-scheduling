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

3. Instale as dependências do projeto executando o script:
    ```bash
    bash install_dependencies.sh
    ```

4. Execute o script para criar a tabela no banco de dados:
    ```bash
    python -c "from models.database import create_tables; create_tables()"
    ```

## Executando a Aplicação

Para iniciar o backend, execute:

```bash
python app.py
```

Para iniciar o frontend, navegue até o diretório `frontend` e execute:

```bash
npm run serve
```

Você verá as opções no menu principal. Escolha a ação desejada e siga as instruções no terminal.

## Dockerização

Para facilitar a execução do projeto, você pode utilizar Docker. Siga os passos abaixo para construir e executar o projeto em um container Docker.

### Construir a Imagem Docker

1. Certifique-se de ter o Docker instalado e em execução em sua máquina.

2. Navegue até o diretório raiz do projeto e execute o seguinte comando para construir a imagem Docker:
   ```bash
   docker build -t promo-scheduling .
   ```

### Executar o Container Docker

1. Após a construção da imagem, execute o seguinte comando para iniciar o container:
   ```bash
   docker run -p 8000:8000 promo-scheduling
   ```

2. O aplicativo estará disponível em `http://localhost:8000`.

## Build do Projeto

Para construir o projeto localmente sem Docker, siga os passos abaixo:

1. Certifique-se de que todas as dependências estejam instaladas conforme descrito na seção "Configurando o Ambiente".

2. Execute o seguinte comando para construir o projeto:
   ```bash
   npm run build
   ```

3. O projeto estará pronto para ser servido em um servidor de produção.

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
├── frontend/          # Diretório para o frontend Vue.js
│   ├── src/           # Código-fonte do frontend
│   ├── public/        # Arquivos públicos
│   └── package.json   # Dependências do frontend
├── requirements.txt   # Dependências do projeto
└── README.md          # Documentação do projeto
