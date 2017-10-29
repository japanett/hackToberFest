from listaLigada import ListaLigada


def main():
    lista = ListaLigada()
    lista2 = ListaLigada()
    original = ListaLigada()
    fim = False
    while not fim:
        print('-----------------')
        opcao = int(input('Escolha a operacao: \n\t1. Inserir elemento no inicio da lista: \n\t2.Imprimir lista(s)\n\t3.Dividir lista\n\t4.Sair\nOpcao: '))
        try:
            if opcao == 1:
                elem = int(input('Digite o numero a ser inserido: '))
                original.insereInicio(elem)
                # print('Elemento inserido !')
            elif opcao == 2:
                print('Lista Original:', end = " ")
                original.imprime()
                if not lista.eVazia() and not lista2.eVazia():
                    print('--- Lista Original dividida --- ')
                    print('Primeira metade:', end = " ")
                    lista.imprime()                     
                    print('Segunda metade:', end = " ")
                    lista2.imprime()
            elif opcao == 3:
                print('Dividindo lista...')
                lista = original.copia()
                lista2 = lista.divide()
            elif opcao == 4:
                print('Saindo...')
                fim = True
            else:
                print('Opcao invalida')
        except RuntimeError as erro:
            print(erro)
# Faça um programa em Python que seja capaz de dividir ao meio uma lista encadeada em outras duas listas. 
# Se houver quantidade ímpar de elementos, a maior lista deve ser a primeira.

# O usuário deve ser capaz de entrar com os elementos a serem inseridos e, posteriormente, a lista é dividida em duas.
# Imprima a lista original e depois as duas listas geradas.

# Lembre-se que o último elemento de uma lista deve ter seu campo "próximo" em Null. -
if __name__ == "__main__":
    main()