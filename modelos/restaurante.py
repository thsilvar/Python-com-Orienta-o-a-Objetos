class Restautante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restautante.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome} ({self.categoria})'

    def listar_restaurantes():
        for restaurante in Restautante.restaurantes:
            print(f'{restaurante.nome} ({restaurante.categoria}) - {restaurante.ativo}')    

restaurante_praca = Restautante('Restaurante da Praça', 'Comida Brasileira')
restaurante_pizza = Restautante('Pizzaria do Bairro', 'Pizzaria')

Restautante.listar_restaurantes()

