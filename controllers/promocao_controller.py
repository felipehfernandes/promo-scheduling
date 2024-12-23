from models.database import get_connection
from models.promocao import Promocao
from datetime import datetime

class PromocaoController:
    @staticmethod
    def criar_promocao(nome_promocao, valor_promocao, data_inicio, data_fim, status):
        # Validações
        agora = datetime.now()
        if datetime.fromisoformat(data_inicio) <= agora:
            raise ValueError("A data de início deve ser depois da hora atual.")
        if datetime.fromisoformat(data_fim) <= datetime.fromisoformat(data_inicio):
            raise ValueError("A data de fim deve ser depois da data de início.")
        if float(valor_promocao) > 10:
            raise ValueError("O valor da promoção não pode exceder R$10,00.")

        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO agendamentos (nome_promocao, valor_promocao, data_inicio, data_fim, status)
            VALUES (?, ?, ?, ?, ?)
        """, (nome_promocao, valor_promocao, data_inicio, data_fim, status))
        connection.commit()
        cursor.close()
        connection.close()

    @staticmethod
    def listar_promocoes():
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("""
            SELECT a.id, a.nome_promocao, a.valor_promocao, a.data_inicio, a.data_fim, s.nome AS status, a.data_criacao
            FROM agendamentos a
            INNER JOIN status s ON a.status = s.id
        """)
        resultados = cursor.fetchall()
        cursor.close()
        connection.close()
        return [Promocao(*r) for r in resultados]

    @staticmethod
    def editar_promocao(id, nome_promocao, valor_promocao, data_inicio, data_fim, status):
        agora = datetime.now()
        if datetime.fromisoformat(data_inicio) <= agora:
            raise ValueError("A data de início deve ser depois da hora atual.")
        if datetime.fromisoformat(data_fim) <= datetime.fromisoformat(data_inicio):
            raise ValueError("A data de fim deve ser depois da data de início.")
        if float(valor_promocao) > 10:
            raise ValueError("O valor da promoção não pode exceder R$10,00.")

        connection = get_connection()
        cursor = connection.cursor()

        # Atualiza promoção
        cursor.execute("""
            UPDATE agendamentos
            SET nome_promocao = ?, valor_promocao = ?, data_inicio = ?, data_fim = ?, status = ?
            WHERE id = ?
        """, (nome_promocao, valor_promocao, data_inicio, data_fim, status, id))

        # Insere histórico
        cursor.execute("""
            INSERT INTO historico_alteracoes (id_promocao, alteracao)
            VALUES (?, ?)
        """, (id, f"Promoção editada: nome={nome_promocao}, valor={valor_promocao}, início={data_inicio}, fim={data_fim}, status={status}"))

        connection.commit()
        cursor.close()
        connection.close()

    @staticmethod
    def alterar_status_promocao(id, novo_status):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("""
            UPDATE agendamentos
            SET status = ?
            WHERE id = ?
        """, (novo_status, id))

        # Insere no histórico a alteração do status
        cursor.execute("""
            INSERT INTO historico_alteracoes (id_promocao, alteracao)
            VALUES (?, ?)
        """, (id, f"Status alterado para {novo_status}"))

        connection.commit()
        cursor.close()
        connection.close()
