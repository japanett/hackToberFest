class ArvoreBinBusca:
    class __No:
        def __init__(self, e):
            self.item = e
            self.esq = None
            self.dir = None
            self.pai = None
        def getItem(self):
            return self.item
        def getEsq(self):
            return self.esq
        def getDir(self):
            return self.dir
        def getPai(self):
            return self.pai
        def setItem(self, e):
            self.item = e
        def setEsq(self, n):
            self.esq = n
        def setDir(self, n):
            self.dir = n
        def setPai(self, n):
            self.pai = n
        
    def __init__(self):
        self.raiz = None
    def eVazia(self):
        return self.raiz == None
    def __setRaiz(self, n):
        self.raiz = n
    def __getRaiz(self):
        return self.raiz

    def achaMaior(self):
        return ArvoreBinBusca.__achaMaior_elem(self.__getRaiz())
        
    @staticmethod
    def __achaMaior_elem(n):
        if n.getDir() == None:
            return n.getItem()
        else:
            ArvoreBinBusca.__achaMaior_elem(n.getDir())

    def insere(self, elem):
        novo = ArvoreBinBusca.__No(elem)
        if self.eVazia():
            self.__setRaiz(novo)
        else:
            ArvoreBinBusca.__insereNo(self.__getRaiz(), novo)
        
    @staticmethod
    def __insereNo(pai, novo):
        if novo.getItem() <= pai.getItem():
            if pai.getEsq() != None:
                ArvoreBinBusca.__insereNo(pai.getEsq(), novo)
            else:
                novo.setPai(pai)
                pai.setEsq(novo)
        elif pai.getDir() != None:
            ArvoreBinBusca.__insereNo(pai.getDir(), novo)
        else:
            novo.setPai(pai)
            pai.setDir(novo)

#         Percursos em Arvores Binarias
# Algoritmos p/ visitar todos os nós presentes em uma arvore Binaria
# Para visitar todos os nós a partir de um nó N, devemos:
#         *Visitar o nó N 
#         *Visitar todos os nós da subárvore esquerda de N
#         *Visitar todos os nós da subárvore direita de N 
#     Pré-Ordem: [ 10 - 5 - 7 - 40 - 20 - 50 ]
        # *Processa o nó N ANTES de processar suas subarvores
#     EXEMPLO: dada a árvore, exibir a sequencia de nos visitados ao percorre-la na pre-ordem     10
#     10 - 5 - 7 - 40 - 20 - 50                                                                5       40
#     [R] [Esq  ] [  direita  ]                                                                  7   20  50 

#     Em-Ordem: [ 5 - 7 - 10 - 20 - 40 - 50 ]
#     OBS: Se a arvore é binaria de busca, a sequencia será ordenada
#     *O nó N é processado DEPOIS da subarvore esquerda e ANTES da direita

#  Pós-Ordem: [ 7 - 5 - 20 - 50 - 40 - 10 ]
    #     *O nó N é processado DEPOIS das subarvores esquerda e direita.

        # Retorna o antecessor de um no n.
    #   n deve ter filho esquerdo

    # Qual eh a complexidade de busca em uma ABB ? 
    # OBS: Quanto maior a altura da arvore, maior o tempo gasto na busca(no pior caso)
    # R: O (n) pois, no pior caso, a arvore terá altura n.
    # Complexidade de algoritmos importantes: 
    #   - Inserçao é O(n)
    #   - Remocao é O(n)
    #   - Busca é O(n)
    #   dependem, no pior caso, da altura da arvore.
    #   todos eles sao de complexidade O(n), onde n é o numero de nós da arvore
    # Uma arvore binaria eh chamada de completa se todo nó interno tiver 2 folhas e 
    # todas as folhas tiverem a mesma profundidade

    # Arvore AVL - Reestruturar uma ABB de tal forma que a arvore resultante tenha uma
    # "distribuicao razoavel" dos nós nas subarvores direita e esquerda
    # Ideia: Manter um BALANCEAMENTO dos nós nas subarvores direita e esquerda
    # Criterio de balanceamento AVL: "A diferenca entre as alturas das subarvores 
    # direita e esquerda é, no máximo, 1. OBS: deve valer para todos os nós"
    def imprime_preOrdem(self):
        print("PreOrdem: [", end=' ')
        ArvoreBinBusca.__preOrdem(self.__getRaiz())
        print(" ]")

    @staticmethod      
    def __preOrdem(n):
        if n != None:
            print(n.getItem(), end=' ')
            ArvoreBinBusca.__preOrdem(n.getEsq())
            ArvoreBinBusca.__preOrdem(n.getDir())
   

    
    def imprime_emOrdem(self):
        print("EmOrdem: [", end=' ')
        ArvoreBinBusca.__emOrdem(self.__getRaiz())
        print(" ]")

    @staticmethod      
    def __emOrdem(n):
        if n != None:
            ArvoreBinBusca.__emOrdem(n.getEsq())
            print(n.getItem(), end=' ')
            ArvoreBinBusca.__emOrdem(n.getDir())


       
    def imprime_posOrdem(self):
        print("PosOrdem: [", end=' ')
        ArvoreBinBusca.__posOrdem(self.__getRaiz())
        print(" ]")

    @staticmethod      
    def __posOrdem(n):
        if n != None:
            ArvoreBinBusca.__posOrdem(n.getEsq())
            ArvoreBinBusca.__posOrdem(n.getDir())
            print(n.getItem(), end=' ')


        
    def busca(self, elem):
        resp = ArvoreBinBusca.__busca_elem(self.__getRaiz(), elem)
        if resp == None:
            return None
        else:
            return resp.getItem()

    @staticmethod      
    def __busca_elem(n, elem):
        if n == None:
            return None
        elif elem == n.getItem():
            return n
        elif elem <= n.getItem():
            return ArvoreBinBusca.__busca_elem(n.getEsq(), elem)
        else:
            return ArvoreBinBusca.__busca_elem(n.getDir(), elem)


    
    def remove(self, elem):
        rem= ArvoreBinBusca.__busca_elem(self.__getRaiz(), elem)
        if rem != None:
            self.__remove_no(rem)

    def __remove_no(self, rem):
        if rem.getEsq() == None:
            self.__transplante(rem, rem.getDir())
        elif rem.getDir() == None:
            self.__transplante(rem, rem.getEsq())
        else:
            ant= ArvoreBinBusca.__antecessor(rem)
            rem.setItem(ant.getItem())
            self.__remove_no(ant)

    # Retorna o antecessor de um no n.
    #   n deve ter filho esquerdo
    @staticmethod      
    def __antecessor(n):
        sub= n.getEsq()
        while sub.getDir() != None:
            sub= sub.getDir()
        return sub

    def __transplante(self, ant, nova):
        if ant.getPai() == None:
            self.__setRaiz(nova)
        elif ant.getPai().getEsq() == ant: # ant e filho esq
            ant.getPai().setEsq(nova)
        else:                              # ant e filho direito
            ant.getPai().setDir(nova)
        if nova != None:
            nova.setPai(ant.getPai())