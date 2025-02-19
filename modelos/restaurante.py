class Restautante:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False

restaurante_praca = Restautante('Restaurante da Praça', 'Comida Brasileira')
restaurante_pizza = Restautante('Pizzaria do Bairro', 'Pizzaria')

restaurantes = [restaurante_praca, restaurante_pizza]

print(vars(restaurante_praca))
print(vars(restaurante_pizza))