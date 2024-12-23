class Promocao:
    def __init__(self, id, nome_promocao, valor_promocao, data_inicio, data_fim, status, data_criacao):
        self.id = id
        self.nome_promocao = nome_promocao
        self.valor_promocao = float(valor_promocao)  # Converte para float
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.status = status
        self.data_criacao = data_criacao
