# A Lista Encadeada e a Lista Sequencial possuem uma interface comum, pois elas irão disponibilizar os mesmos recursos para o usuário. 
# A diferença entre elas é interna, onde tem diferenças na complexidade dos algoritmos e até do uso de recursos do computador. 

# A Lista Encadeada não há muito o que falar. É uma lista que utiliza de Nós para ser preenchida, e sua alocação não é sequencial, mas
# possui dados espalhados na memória. 

from node import Node

class Lista_encadeada:
    
    # Uma lista encadeada é nada mais do que uma sequência de Nós um ligado ao outro, de forma que cada Nó sabe quem é seu próximo.
    # Então, é possível ver basta ter o primeiro Nó para que possamos transitar por todos os outros. Dentro da lista então
    # teremos apenas uma referência no atributo chamado de cabeça, que inicialmente receberá None por não termos delimitado a lista.
    # O segundo atributo é apenas por conveniência, mas não define necessariamente o uso da lista. 

    def __init__(self):
        self.cabeca = None
        self._size = 0 # Aqqui já temos a criação da lista, tudo que vier agora são os métodos que ela requer, ou seja, adicionar, retirar, etc

    # Há dois casos para adicionar. O primeiro é quando a lista ta vazia, ou seja, já vai ser adicionado no "final". O segundo é quando a lista
    # já possui elementos, então temos um Nó associado a cabeça. Por isso usaremos o laço condicional para verificar qual dos casos estamos.

    def adicionar(self, elemento):
        # Vamos usar uma variável auxiliar chamada ponteiro para ajudar
        if self.cabeca:
            # inserção quando há elementos na lista
            ponteiro = self.cabeca # Essa variável vai apontar para o espaço de memória da cabeca
            while(ponteiro.next): # Isso pode ser lido da seguinte forma: Enquanto o ponteiro tiver um próximo valor signfica que não chegou no final
                ponteiro = ponteiro.next # então se não chegou ao fim, avança para o próximo
            ponteiro.next = Node(elemento) # Quando a lista chegar ao fim, e sair do laço de repetição, irá então adicionar no próximo Nó o elemento       

        else:
            # primeira inserção da lista
            self.cabecaa = Node(elemento)

        self._size = self._size + 1 # Apenas incrementando o tamanho da lista 

    # Ainda não conseguimos enxergar os elementos da lista. Além disso, pedir o tamanho da lista através do size não é uma boa prática em Python.
    # Vamos criar então a função len, que já é usada para descobrir o tamanho de uma lista qualquer em python. Ela será especial igual ao init
    # Essa função irá retornar o tamanho que estamos armazenando. 
    # Por questão que convenção, ao invés de chamar de size, vamos por o _size, para o usuário ou quem usar a classe não tenha acesso direto
    
    def __len__(self):
        '''Retorna o tamanho da lista'''
        return self._size
    
    # Agora vamos criar o método para acessar um determinado elemento na lista.

    def get(self, index):
        pass

    # Estamos usando esse __getitem__ para fazer uma sobrecarga do operador, um recurso de Orientação a objetos para usar o operador de colchetes
    # para ter um determinado comportamento na classe. Estamos fazendo isso para usar os [], assim usando para achar os elementos nos index, como
    # a linguagem já nos proporciona 'elemento[0]'.  

    def __getitem__(self, index):
        # Igual na função de adicionar, precisaremos de um ponteiro para nos guiar dentro da lista, pois se modificarmos o self.cabeca, isso
        # faria a lista se perder na memória.
        ponteiro = self.cabeca
        for i in range(index):
            # Estamos verificando o ponteiro é None, caso não, ele dará um erro já usado por Python: IndexError
            if ponteiro:
                ponteiro = ponteiro.next
            else:
                raise IndexError("list index out of range")
        # Aqui nós estaremos com o ponteiro na posição adequada. E verificamos mais uma vez se o ponteiro não é vazio
        # Se não tiver no vazio, retornará o elemento do ponteiro.   
        if ponteiro:
            return ponteiro.data
        else:
            raise IndexError("list index out of range")

    # O set serve para modificar o elemento da lista em uma certa posição
    def set(self, index, elemento):
        pass


    # Do mesmo modo do __getitem__, essa forma especial de função é para utilizar os colchetes para trocar de elemento em uma certa posição da
    # lista. Ou seja, lista[5] = 9
    def __setitem__(self, index, elemento):
        # Trocar elemento é igual ao __getitem__, porém no final ao inves de retornar, iremos substituir
        ponteiro = self.cabeca
        for i in range(index):
            if ponteiro:
                ponteiro = ponteiro.next
            else:
                raise IndexError("list index out of range")
        # Ao invés de retornar, vamos substituir o elemento pelo outro.  
        if ponteiro:
            ponteiro.data = elemento
        else:
            raise IndexError("list index out of range")

lista = Lista_encadeada()