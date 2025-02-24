from modelos.restaurante import Restaurante
from modelos.cardapio.prato import Prato
from modelos.cardapio.bebida import Bebida

restaurante_praca = Restaurante('restaurante da Praça', 'Comida Brasileira')
restaurante_pizza = Restaurante('Pizzaria do Bairro', 'Pizzaria')
restaurante_mexicano = Restaurante('Mexicano do Centro', 'Comida Mexicana')
restaurante_japones = Restaurante('Sushi da Esquina', 'Comida Japonesa')

restaurante_praca.alternar_status()

bebida_suco = Bebida('Suco de Laranja', 5.0, '300ml')
bebida_refri = Bebida('Refrigerante', 4.0, '300ml')

prato_feijoada = Prato('Feijoada', 20.0, 'Feijoada completa com arroz, farofa e couve')
prato_macarrao = Prato('Macarrão', 15.0, 'Macarrão ao molho bolonhesa')

restaurante_praca.adicionar_bebida_no_cardapio(bebida_suco)
restaurante_praca.adicionar_bebida_no_cardapio(bebida_refri)
restaurante_praca.adicionar_prato_no_cardapio(prato_feijoada)
restaurante_praca.adicionar_prato_no_cardapio(prato_macarrao)

def main():
    print(bebida_suco)
    print(bebida_refri)
    print(prato_feijoada)

if __name__ == '__main__':
    main()