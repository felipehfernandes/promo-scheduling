class Promocao:
    def __init__(self, id, nome_promocao, valor_promocao, data_inicio, data_fim, status, data_criacao, regioes=None):
        self.id = id
        self.nome_promocao = nome_promocao
        self.valor_promocao = float(valor_promocao)  # Converte para float
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.status = status
        self.data_criacao = data_criacao
        self.regioes = regioes or []  # Inicializa como lista vazia se não fornecido

    def to_dict(self):
        return {
            'id': self.id,
            'nome_promocao': self.nome_promocao,
            'valor_promocao': self.valor_promocao,
            'data_inicio': self.data_inicio,
            'data_fim': self.data_fim,
            'status': self.status,
            'data_criacao': self.data_criacao,
            'regioes': self.regioes  # Inclui as regiões no dicionário
        }
