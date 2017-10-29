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
        if self.__getRaiz() == None:
            return -1
        else:
            maior = ArvoreBinBusca.__achaMaior_elem(self.__getRaiz())
            return maior.getItem()

    @staticmethod
    def __achaMaior_elem(n):
        if n == None:
            return n.getPai()
        elif n.getDir() == None:
            return n
        else:
            return ArvoreBinBusca.__achaMaior_elem(n.getDir())


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

    def contaNos(self):
        if self.__getRaiz() == None:
            return 0
        else:
            return ArvoreBinBusca.__contaNos(self.__getRaiz())
        
            
    @staticmethod
    def __contaNos(n):
        cont = 1
        if n.getEsq() != None:
            cont += ArvoreBinBusca.__contaNos(n.getEsq())
        if n.getDir() != None:
            cont += ArvoreBinBusca.__contaNos(n.getDir())
        return cont

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


