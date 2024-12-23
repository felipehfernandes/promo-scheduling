class PromocaoView:
    @staticmethod
    def exibir_promocoes(promocoes):
        for promocao in promocoes:
            print(f"ID: {promocao.id}, Nome: {promocao.nomepromocao}, Valor: R${promocao.valorpromocao:.2f}, Início: {promocao.datainicio}, Fim: {promocao.datafim}, Criado em: {promocao.datacriacao}")

    @staticmethod
    def solicitar_dados_promocao():
        nomepromocao = input("Nome da Promoção: ")
        valorpromocao = float(input("Valor da Promoção: "))
        datainicio = input("Data de Início (YYYY-MM-DD): ")
        datafim = input("Data de Fim (YYYY-MM-DD): ")
        return nomepromocao, valorpromocao, datainicio, datafim
