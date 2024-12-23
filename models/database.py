from config import get_connection

def create_tables():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS status (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL UNIQUE,
            descricao TEXT NOT NULL
        )
    """)
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
    # Inserindo status padrão, caso ainda não existam
    cursor.execute("""
        INSERT OR IGNORE INTO status (id, nome, descricao)
        VALUES 
        (1, 'vigente', 'Promoção está ativa e válida'),
        (2, 'desativado', 'Promoção foi desativada')
    """)
    connection.commit()
    cursor.close()
    connection.close()
