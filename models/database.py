from config import get_connection

def create_tables():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS agendamentos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            nome_promocao TEXT NOT NULL,
            valor_promocao REAL NOT NULL,
            data_inicio TIMESTAMP NOT NULL,
            data_fim TIMESTAMP NOT NULL
        )
    """)
    connection.commit()
    cursor.close()
    connection.close()
