from listaLigada import ListaLigada


def main():
    lista = ListaLigada()
    fim = False
    while not fim:
        print('-----------------')
        opcao = int(input(('Escolha a operacao: \n\t1.Inserir elemento no inicio\n\t2.Imprimir\n\t3.Consultar qtd de itens\n\t4.Buscar elemento\n\t5.Contar ocorrencia de um elemento\n\t6.Remover primeira celula\n\t7.Remover ultima celula\n\t8.Remover elemento X\n\t9.Sair\nOpcao: ')))
        try:
            if opcao == 1:
                elem = int(input('Digite o numero a ser inserido: '))
                lista.insereInicio(elem)
                print('Elemento inserido !')
            elif opcao == 2:
                lista.imprime()
            elif opcao == 3:
                print('Quantidade de itens: ', lista.qtdItens())
            elif opcao == 4:
                elem = int(input('Insira o elemento a ser buscado: '))
                if lista.busca(elem):
                     print('Elemento - %d - foi encontrado' %(elem))
                else:
                    print('Elemento - %d - NAO foi encontrado' %(elem))
            elif opcao == 5:
                elem = int(input('Contar ocorrencias do numero: '))
                ocorrencia = lista.contaOcorrencia(elem)
                print('O numero %d ocorre %d vez(es)' %(elem, ocorrencia))
            elif opcao == 6:
                lista.removePrimeira()
            elif opcao == 7:
                lista.removeUltima()
            elif opcao == 8:
                elem = int(input('Insira o numero a remover da lista: '))
                lista.remove(elem)
            elif opcao == 9:
                print('Saindo...')
                fim = True
            else:
                print('Opcao invalida')
        except RuntimeError as erro:
            print(erro)
# Exercicios: 
# fazer um metodo que retorna o numero de ocorrencias d eum elemento
# metodo que retorna a informacao que esta na ultima celula
# metodo para inserir elemento no final da lista

if __name__ == "__main__":
    main()


