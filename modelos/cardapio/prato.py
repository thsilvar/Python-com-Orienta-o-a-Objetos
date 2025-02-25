from modelos.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio):
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco)
        self._descricao = descricao

    def __str__(self):
        return f'Prato: {self._nome} - R$ {self._preco} - {self._descricao}'
    
    def aplicar_desconto(self, desconto):
        self._preco -= (self._preco * desconto)