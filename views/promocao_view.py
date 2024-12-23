from config import get_connection

class PromocaoView:
    @staticmethod
    def exibir_promocoes(promocoes):
        for promocao in promocoes:
            print(f"ID: {promocao.id}, Nome: {promocao.nome_promocao}, Valor: R${promocao.valor_promocao:.2f}, "
                  f"Início: {promocao.data_inicio}, Fim: {promocao.data_fim}, Status: {promocao.status}, "
                  f"Criado em: {promocao.data_criacao}")

    @staticmethod
    def solicitar_dados_promocao():
        nome_promocao = input("Nome da Promoção: ")
        valor_promocao = input("Valor da Promoção (máximo R$10,00): R$")
        data_inicio = input("Data e Hora de Início (YYYY-MM-DD HH:MM:SS): ")
        data_fim = input("Data e Hora de Fim (YYYY-MM-DD HH:MM:SS): ")
        status = input("Status (1 = vigente, 2 = desativado): ")
        return nome_promocao, valor_promocao, data_inicio, data_fim, status

    @staticmethod
    def solicitar_dados_alteracao_status():
        id_promocao = input("Digite o ID da Promoção que deseja alterar o status: ")
        novo_status = input("Digite o novo status (1 = vigente, 2 = desativado): ")
        return id_promocao, novo_status

    @staticmethod
    def solicitar_dados_promocao_edicao():
        print("Deixe em branco para manter o valor atual.")
        nome_promocao = input("Nome da Promoção: ")
        valor_promocao = input("Valor da Promoção (máximo R$10,00): R$")
        data_inicio = input("Data e Hora de Início (YYYY-MM-DD HH:MM:SS): ")
        data_fim = input("Data e Hora de Fim (YYYY-MM-DD HH:MM:SS): ")
        status = input("Status (1 = vigente, 2 = desativado): ")
        print("\nRegiões: Deixe vazio para manter as regiões atuais ou digite 'todas' para todas as regiões.")
        regioes_ids = PromocaoView.solicitar_regioes()
        return nome_promocao, valor_promocao, data_inicio, data_fim, status, regioes_ids

    @staticmethod
    def solicitar_regioes():
        print("Escolha as regiões para a promoção. Digite 'todas' para selecionar todas as regiões.")
        print("ID | UF | Estado")
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT id, uf, estado FROM regioes")
        regioes = cursor.fetchall()
        cursor.close()
        connection.close()

        for regiao in regioes:
            print(f"{regiao[0]} | {regiao[1]} | {regiao[2]}")

        regioes_ids = input("Digite os IDs das regiões separados por vírgula (ex: 1,2,3): ")
        return [r.strip() for r in regioes_ids.split(",")]