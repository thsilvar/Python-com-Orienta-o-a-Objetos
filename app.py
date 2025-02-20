from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('restaurante da Praça', 'Comida Brasileira')
restaurante_pizza = Restaurante('Pizzaria do Bairro', 'Pizzaria')
restaurante_mexicano = Restaurante('Mexicano do Centro', 'Comida Mexicana')
restaurante_japones = Restaurante('Sushi da Esquina', 'Comida Japonesa')

restaurante_praca.alternar_status()

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()