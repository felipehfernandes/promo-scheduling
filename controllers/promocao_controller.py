from models.database import get_connection
from models.promocao import Promocao

class PromocaoController:
    @staticmethod
    def criar_promocao(nomepromocao, valorpromocao, datainicio, datafim):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO agendamentos (nomepromocao, valorpromocao, datainicio, datafim)
            VALUES (?, ?, ?, ?)
        """, (nomepromocao, valorpromocao, datainicio, datafim))
        connection.commit()
        cursor.close()
        connection.close()

    @staticmethod
    def listar_promocoes():
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM agendamentos")
        resultados = cursor.fetchall()
        cursor.close()
        connection.close()
        return [Promocao(*r) for r in resultados]

    @staticmethod
    def editar_promocao(id, nomepromocao, valorpromocao, datainicio, datafim):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("""
            UPDATE agendamentos
            SET nomepromocao = ?, valorpromocao = ?, datainicio = ?, datafim = ?
            WHERE id = ?
        """, (nomepromocao, valorpromocao, datainicio, datafim, id))
        connection.commit()
        cursor.close()
        connection.close()

    @staticmethod
    def excluir_promocao(id):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM agendamentos WHERE id = ?", (id,))
        connection.commit()
        cursor.close()
        connection.close()
