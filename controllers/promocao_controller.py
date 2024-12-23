from models.database import get_connection
from models.promocao import Promocao
from datetime import datetime
import json

class PromocaoController:
    @staticmethod
    def criar_promocao(nome_promocao, valor_promocao, data_inicio, data_fim, status, regioes_ids):
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

        # Cria a promoção
        cursor.execute("""
            INSERT INTO agendamentos (nome_promocao, valor_promocao, data_inicio, data_fim, status)
            VALUES (?, ?, ?, ?, ?)
        """, (nome_promocao, valor_promocao, data_inicio, data_fim, status))
        id_promocao = cursor.lastrowid

        connection.commit()
        cursor.close()
        connection.close()

        # Associa as regiões
        PromocaoController.associar_regioes(id_promocao, regioes_ids)

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
    def editar_promocao(id, nome_promocao, valor_promocao, data_inicio, data_fim, status, regioes_ids):
        connection = get_connection()
        cursor = connection.cursor()

        # Busca os valores atuais no banco
        cursor.execute("""
            SELECT nome_promocao, valor_promocao, data_inicio, data_fim, status
            FROM agendamentos
            WHERE id = ?
        """, (id,))
        promocao_atual = cursor.fetchone()

        if not promocao_atual:
            raise ValueError("Promoção com o ID fornecido não encontrada.")

        # Busca as regiões atuais associadas
        cursor.execute("""
            SELECT r.uf
            FROM promocoes_regioes pr
            INNER JOIN regioes r ON pr.id_regiao = r.id
            WHERE pr.id_promocao = ?
        """, (id,))
        regioes_atuais = [r[0] for r in cursor.fetchall()]

        # Mantém os valores antigos caso os novos estejam vazios
        nova_promocao = {
            "nome_promocao": nome_promocao or promocao_atual[0],
            "valor_promocao": valor_promocao or promocao_atual[1],
            "data_inicio": data_inicio or promocao_atual[2],
            "data_fim": data_fim or promocao_atual[3],
            "status": status or promocao_atual[4],
            "regioes": regioes_atuais  # Inclui as regiões atuais
        }

        # Determina as colunas alteradas
        colunas_alteradas = []
        for coluna, valor_novo in nova_promocao.items():
            if coluna != "regioes":  # Comparar regiões separadamente
                valor_antigo = promocao_atual[list(nova_promocao.keys()).index(coluna)]
                if str(valor_antigo) != str(valor_novo):
                    colunas_alteradas.append(coluna)

        # Atualiza a promoção
        cursor.execute("""
            UPDATE agendamentos
            SET nome_promocao = ?, valor_promocao = ?, data_inicio = ?, data_fim = ?, status = ?
            WHERE id = ?
        """, (nova_promocao["nome_promocao"], nova_promocao["valor_promocao"],
              nova_promocao["data_inicio"], nova_promocao["data_fim"], nova_promocao["status"], id))

        # Atualiza as regiões associadas
        if regioes_ids:
            # Remove associações antigas
            cursor.execute("DELETE FROM promocoes_regioes WHERE id_promocao = ?", (id,))

            # Reassocia novas regiões
            if "todas" in regioes_ids:
                cursor.execute("SELECT id FROM regioes")
                regioes_ids = [r[0] for r in cursor.fetchall()]

            for regiao_id in regioes_ids:
                cursor.execute("""
                    INSERT INTO promocoes_regioes (id_promocao, id_regiao)
                    VALUES (?, ?)
                """, (id, regiao_id))

            # Busca as novas regiões associadas
            cursor.execute("""
                SELECT r.uf
                FROM promocoes_regioes pr
                INNER JOIN regioes r ON pr.id_regiao = r.id
                WHERE pr.id_promocao = ?
            """, (id,))
            novas_regioes = [r[0] for r in cursor.fetchall()]
            nova_promocao["regioes"] = novas_regioes

            colunas_alteradas.append("regioes")

        # Registra o histórico da alteração
        promocao_antes = {
            "nome_promocao": promocao_atual[0],
            "valor_promocao": promocao_atual[1],
            "data_inicio": promocao_atual[2],
            "data_fim": promocao_atual[3],
            "status": promocao_atual[4],
            "regioes": regioes_atuais
        }

        cursor.execute("""
            INSERT INTO historico_alteracoes (id_promocao, promocao_antes, promocao_depois, alteracao)
            VALUES (?, ?, ?, ?)
        """, (id, json.dumps(promocao_antes), json.dumps(nova_promocao), json.dumps(colunas_alteradas)))

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

    @staticmethod
    def associar_regioes(id_promocao, regioes_ids):
        connection = get_connection()
        cursor = connection.cursor()

        # Associa todas as regiões se o usuário escolher "todas"
        if "todas" in regioes_ids:
            cursor.execute("SELECT id FROM regioes")
            regioes_ids = [r[0] for r in cursor.fetchall()]

        # Insere na tabela associativa
        for id_regiao in regioes_ids:
            cursor.execute("""
                INSERT INTO promocoes_regioes (id_promocao, id_regiao)
                VALUES (?, ?)
            """, (id_promocao, id_regiao))

        connection.commit()
        cursor.close()
        connection.close()
