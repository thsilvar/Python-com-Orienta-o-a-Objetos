from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('restaurante da Praça', 'Comida Brasileira')
restaurante_pizza = Restaurante('Pizzaria do Bairro', 'Pizzaria')
restaurante_mexicano = Restaurante('Mexicano do Centro', 'Comida Mexicana')
restaurante_japones = Restaurante('Sushi da Esquina', 'Comida Japonesa')

restaurante_praca.alternar_status()

restaurante_praca.receber_avaliar('João', 4)
restaurante_praca.receber_avaliar('Maria', 5)
restaurante_praca.receber_avaliar('José', 3)


def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()