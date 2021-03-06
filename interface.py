from services.avl_tree_service import AvlTreeService
from services.binary_tree_service import BinaryTreeService
from services.red_black_tree_service import RedBlackTreeService


def invalid_key():
    print 'Opcao invalida!'


def kill_interface():
    print 'Encerrando...'


options = {
    '1': AvlTreeService.generate_and_print,
    '2': BinaryTreeService.generate_and_print,
    '3': RedBlackTreeService.generate_and_print,
    '4': kill_interface
}


def run():
    option = '0'

    while option != '4':
        option = raw_input('Qual arvore deseja montar? Digite sua opcao\n'
                           '1 - AVL\n'
                           '2 - Binaria\n'
                           '3 - Rubro-negra\n'
                           '4 - Encerrar\n')

        try:
            options[option]()
        except KeyError:
            invalid_key()
