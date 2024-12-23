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
