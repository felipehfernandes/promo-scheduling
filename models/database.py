from config import get_connection

def create_tables():
    connection = get_connection()
    cursor = connection.cursor()

    # Tabela de Promoções (agendamentos)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS agendamentos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            nome_promocao TEXT NOT NULL,
            valor_promocao REAL NOT NULL CHECK(valor_promocao <= 10),
            data_inicio TIMESTAMP NOT NULL,
            data_fim TIMESTAMP NOT NULL,
            status INTEGER NOT NULL DEFAULT 1,
            FOREIGN KEY (status) REFERENCES status (id)
        )
    """)

    # Tabela de Status
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS status (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL UNIQUE,
            descricao TEXT NOT NULL
        )
    """)

    # Inserir status padrão
    cursor.execute("""
        INSERT OR IGNORE INTO status (id, nome, descricao)
        VALUES 
        (1, 'vigente', 'Promoção está ativa e válida'),
        (2, 'desativado', 'Promoção foi desativada')
    """)

    # Tabela de Histórico de Alterações
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS historico_alteracoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_promocao INTEGER NOT NULL,
            promocao_antes JSON NOT NULL,
            promocao_depois JSON NOT NULL,
            alteracao JSON NOT NULL,
            data_alteracao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (id_promocao) REFERENCES agendamentos (id)
        )
    """)

    # Tabela de Regiões
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS regioes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            uf TEXT NOT NULL UNIQUE,
            estado TEXT NOT NULL,
            fuso_horario TEXT NOT NULL
        )
    """)

    # Inserir estados do Brasil na tabela `regioes`
    regioes = [
        ("AC", "Acre", "UTC-5"),
        ("AL", "Alagoas", "UTC-3"),
        ("AP", "Amapá", "UTC-3"),
        ("AM", "Amazonas", "UTC-4"),
        ("BA", "Bahia", "UTC-3"),
        ("CE", "Ceará", "UTC-3"),
        ("DF", "Distrito Federal", "UTC-3"),
        ("ES", "Espírito Santo", "UTC-3"),
        ("GO", "Goiás", "UTC-3"),
        ("MA", "Maranhão", "UTC-3"),
        ("MT", "Mato Grosso", "UTC-4"),
        ("MS", "Mato Grosso do Sul", "UTC-4"),
        ("MG", "Minas Gerais", "UTC-3"),
        ("PA", "Pará", "UTC-3"),
        ("PB", "Paraíba", "UTC-3"),
        ("PR", "Paraná", "UTC-3"),
        ("PE", "Pernambuco", "UTC-3"),
        ("PI", "Piauí", "UTC-3"),
        ("RJ", "Rio de Janeiro", "UTC-3"),
        ("RN", "Rio Grande do Norte", "UTC-3"),
        ("RS", "Rio Grande do Sul", "UTC-3"),
        ("RO", "Rondônia", "UTC-4"),
        ("RR", "Roraima", "UTC-4"),
        ("SC", "Santa Catarina", "UTC-3"),
        ("SP", "São Paulo", "UTC-3"),
        ("SE", "Sergipe", "UTC-3"),
        ("TO", "Tocantins", "UTC-3")
    ]
    cursor.executemany("""
        INSERT OR IGNORE INTO regioes (uf, estado, fuso_horario)
        VALUES (?, ?, ?)
    """, regioes)

    # Tabela Associativa entre Promoções e Regiões
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS promocoes_regioes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_promocao INTEGER NOT NULL,
            id_regiao INTEGER NOT NULL,
            FOREIGN KEY (id_promocao) REFERENCES agendamentos (id),
            FOREIGN KEY (id_regiao) REFERENCES regioes (id)
        )
    """)

    connection.commit()
    cursor.close()
    connection.close()