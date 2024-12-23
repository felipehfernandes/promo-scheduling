class Promocao:
    def __init__(self, id, nomepromocao, valorpromocao, datainicio, datafim, datacriacao=None):
        self.id = id
        self.nomepromocao = nomepromocao
        self.valorpromocao = valorpromocao
        self.datainicio = datainicio
        self.datafim = datafim
        self.datacriacao = datacriacao
