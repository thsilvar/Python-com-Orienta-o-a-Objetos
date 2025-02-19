class Restautante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self._ativo = False
        Restautante.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome} ({self.categoria})'

    def listar_restaurantes():
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | Ativo')
        for restaurante in Restautante.restaurantes:
            print(f'{restaurante.nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {restaurante.ativo}')    

    @property
    def ativo(self):
        return  'Sim' if self._ativo else 'Não'

restaurante_praca = Restautante('Restaurante da Praça', 'Comida Brasileira')
restaurante_pizza = Restautante('Pizzaria do Bairro', 'Pizzaria')

Restautante.listar_restaurantes()

