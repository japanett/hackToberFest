class ListaLigada:
    class __Celula:
        def __init__(self, e):
            self.item = e
            self.prox = None
            # self.tail = None
        def getItem(self):
            return self.item
        def getProx(self):
            return self.prox
        def setItem(self, e):
            self.item = e
        def setProx(self, p):
            self.prox = p

    def __init__(self):
        self.prim = None
        self.tail = None

    def eVazia(self):
        return self.prim == None

    def insereInicio(self, e):
        aux = ListaLigada.__Celula(e)
        if self.prim == None:
            self.prim = aux
            self.tail = aux
        else:
            self.tail.prox = aux
        self.tail = aux

    def imprime(self):
        cursor = self.prim
        print("[ ", end = '')
        while cursor != None:
            print(cursor.getItem(), end = ' ')
            cursor = cursor.getProx()
        print("]")

    def qtdItens(self):
        qtd = 0
        cursor = self.prim
        while cursor != None:
            qtd += 1
            cursor = cursor.getProx()
        return qtd

    def busca(self, elem):
        cursor = self.prim
        while cursor != None:
            if cursor.getItem() == elem:
                return elem
            cursor = cursor.getProx()
        return None

    def contaOcorrencia(self, elem): #FAZER
        cursor = self.prim
        contador = 0
        while cursor != None:
            if cursor.getItem() == elem:
                contador += 1
            cursor = cursor.getProx()
        return contador

    def removePrimeira(self):
        if self.eVazia():
            return None
        else:
            rem = self.prim
            self.prim = self.prim.getProx()
            return rem.getItem()

    def removeUltima(self):
        if self.eVazia():
            return None
        elif self.prim.getProx() == None:
            return self.removePrimeira()
        else:
            ant = self.prim
            cursor = self.prim.getProx()
            while cursor.getProx() != None:
                ant = cursor
                cursor = cursor.getProx()
            ant.setProx(None)
            return cursor.getItem()

    def remove(self, elem):
        if self.eVazia():
            return None
        elif self.prim.getItem() == elem:
            return self.removePrimeira()
        else: #elem tem um anteior
            ant = self.prim
            cursor = self.prim.getProx()
            while cursor != None and cursor.getItem() != elem:
                ant = cursor
                cursor = cursor.getProx()
            if cursor == None: #elem nao encontrado
                return None
            ant.setProx(cursor.getProx())
            return cursor.getItem()

    def copia(self):
        l = ListaLigada()
        cursor = self.prim
        while cursor != None:
            l.insereInicio(cursor.getItem())
            cursor = cursor.getProx()
        return l
    
    def divide(self):
        l = ListaLigada()
        if self.eVazia():
            return l
        qtd1 = self.qtdItens() // 2
        for i in range(qtd1):
            cursor = self.prim
            ele = cursor.getItem()
            l.insereInicio(ele)
            self.removePrimeira()
            cursor.getProx()
        return l
