from tarefa10 import ArvoreBinBusca

def main():
    arvore = ArvoreBinBusca()
    # arvore.insere(10)
    # arvore.insere(20)
    # print("teste: ", arvore.raiz.getItem())
    # print("teste: ", arvore.raiz.getDir().getItem())

    opcao = 10
    while (opcao != 0):
        opcao = int(input("\tMenu Arvore Binaria de Busca\n0. Sair\n1. Inserir elemento\n2. Achar maior elemento\n3. Qtd de nos\n4. Imprime em ordem\nDigite a opcao: "))
        if (opcao == 1): #inserir elemento
            ele = int(input("### Digite um numero para ser inserido na arvore: "))
            arvore.insere(ele)
        elif (opcao == 2): #achar maior elemento
            maior = arvore.achaMaior()
            if maior == -1:
                print("\t### Nenhum nó encontrado !")
            else:
                print("\t### O maior elemento eh: %d ####" %(maior))
        elif (opcao == 3): #qtd de nos
            qtd = arvore.contaNos()
            print("\t### Quantidade de Nos: %d" %(qtd))
        elif (opcao == 4):
            arvore.imprime_emOrdem()
        elif (opcao == 0):#sair
            print("Saindo...")
        else:
            print("- Opcao Invalida -")
if __name__ == "__main__":
    main()