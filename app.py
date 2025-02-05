import os

restaurantes = [
    {
        'nome': 'Praça',
        'categoria': 'Japonesa',
        'ativo': False
    },
    {
        'nome': 'Pizza Suprema',
        'categoria': 'Pizza',
        'ativo': True
    },
    {
        'nome': 'Cantina',
        'categoria': 'Italiana',
        'ativo': False
    }
]

def exibir_nome_do_programa():
    print("""

    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
    """)

def exibir_opcoes():
    '''Função para exibir as opções do menu principal'''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alternar estado restaurante')
    print('4. Sair \n')
    
def finalizar_app():
    '''Função para finalizar o programa'''
    exibir_subtitulo('Encerrando o programa')

def voltar_ao_menu_principal():
    '''Função para voltar ao menu principal'''
    input('\nDigite uma tecla para voltar ao menu principal ')
    main()

def exibir_subtitulo(texto):
    '''Função para exibir um subtitulo'''
    os.system('cls')
    linha = '*' * len(texto)
    print(f'{linha}')
    print(f'{texto}')
    print(f'{linha}\n')

def opcao_invalida():
    '''Função para exibir mensagem de opção inválida'''
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def cadastrar_novo_restaurante():
    '''Função para cadastrar um novo restaurante
    
    Input:
     - Nome do restaurante
     - Categoria do restaurante

    '''
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante: ')
    categoria = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
    restaurante = {
        'nome': nome_do_restaurante,
        'categoria': categoria,
        'ativo': False
    }
    restaurantes.append(restaurante)
    print('Restaurante cadastrado com sucesso!\n')
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listando os restaurantes')
    print('Nome do restaurante'.ljust(20), ' | Categoria'.ljust(22), ' | Ativo')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'Sim' if restaurante['ativo'] else 'Não'
        print(f'-{nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    exibir_subtitulo('Alternando estado do restaurante')
    nome_do_restaurante = input('Digite o nome do restaurante: ')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if restaurante['nome'] == nome_do_restaurante:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            print(f'O restaurante {nome_do_restaurante} foi ativado' if restaurante['ativo'] else f'O restaurante {nome_do_restaurante} foi desativado')
            break
    if not restaurante_encontrado:
        print(f'O restaurante {nome_do_restaurante} não foi encontrado')
    voltar_ao_menu_principal()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Digite a opção desejada: '))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()    
        else:
            opcao_invalida()
    except:
        opcao_invalida()        
        

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()