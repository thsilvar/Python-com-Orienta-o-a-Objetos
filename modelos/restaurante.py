from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} ({self._categoria})'

    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | Ativo')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25) } | {restaurante.ativo}')    

    @property
    def ativo(self):
        return '⌧' if self._ativo else '☐'
    
    def alternar_status(self):
        self._ativo = not self._ativo

    def receber_avaliar(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        if(not avaliacao.validar_nota()):
            return print('Nota inválida')
        self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return str('Sem avaliações')
        media = sum([avaliacao._nota for avaliacao in self._avaliacao]) / len(self._avaliacao)
        return round(media, 1)

    def adicionar_item_no_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)

