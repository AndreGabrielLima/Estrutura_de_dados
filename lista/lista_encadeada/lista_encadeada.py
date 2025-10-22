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
            self.cabeca = Node(elemento)

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

    # O set serve para modificar o elemento da lista em uma certa posição
    def set(self, index, elemento):
        pass
    # Estamos usando esse __getitem__ para fazer uma sobrecarga do operador, um recurso de Orientação a objetos para usar o operador de colchetes
    # para ter um determinado comportamento na classe. Estamos fazendo isso para usar os [], assim usando para achar os elementos nos index, como
    # a linguagem já nos proporciona 'elemento[0]'.  

    def __getitem__(self, index):
        # Igual na função de adicionar, precisaremos de um ponteiro para nos guiar dentro da lista, pois se modificarmos o self.cabeca, isso
        # faria a lista se perder na memória
        ponteiro = self.cabeca
        for i in range(index):
            # Estamos verificando o ponteiro é None, caso não, ele dará um erro já usado por Python: IndexError
            if ponteiro:
                ponteiro = ponteiro.next
            else:
                raise IndexError("list index out of range")
        # Aqui nós estaremos com o ponteiro na posição adequada. E verificamos mais uma vez se o ponteiro não é vazio
        # Se não tiver no vazio, retornará o elemento 
            
        if ponteiro:
            return ponteiro.data
        raise IndexError("list index out of range")


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


    # Agora vamos criar a função para buscar o elemento. Na alocação encadeada a busca é limitada, pois precisamos andar de nó em nó para acessar
    # os elementos, e não de forma aleatória igual na alocação sequencial. 
    def buscar(self, elemento):
        '''Retornando o index do elemento na lista'''
        ponteiro = self.cabeca
        i = 0 # Variável para guardar a posição do elemento
        while(ponteiro): # Enquanto estiver em um nó que é diferente do vazio vamos verificar se o dado do nó é igual ao elemento que queremos
            if ponteiro.data == elemento:
                return i 
            # Se sair do laço IF não sendo igual, avançamos o ponteiro para o próximo e adicionamos mais um na variável I
            ponteiro = ponteiro.next 
            i = i+1
        # Caso o elemento não esteja na lista
        raise ValueError("Esse elemento {} não está na lista ".format(elemento))
 
lista = Lista_encadeada()

lista.adicionar(7)
lista.adicionar(80)
lista.adicionar(56)
print(lista[1])
print(lista.buscar(80))



################# IN ENGLISH #################



# The Linked List and the Sequential List share a common interface,
# since they will provide the same features to the user.
# The difference between them is internal, in terms of algorithm complexity
# and even in how they use computer resources.

# The Linked List is a structure that uses Nodes to store elements.
# Its allocation is not sequential — data can be spread across memory.

from node import Node

class LinkedList:
    
    # A linked list is nothing more than a sequence of Nodes, each connected to the next one,
    # so that each Node knows who its next neighbor is.
    # Therefore, by knowing only the first Node, we can traverse all others.
    # Inside the list, we’ll have a single reference called “head”,
    # which initially receives None because the list is empty.
    # The second attribute (_size) is just for convenience, to keep track of the list’s length.
    
    def __init__(self):
        self.head = None
        self._size = 0  # Here we create the list; from now on, we’ll implement its methods (add, remove, etc.)

    # There are two cases when adding a new element.
    # The first is when the list is empty, meaning the new element will be added at the "end" right away.
    # The second is when the list already has elements, so we have a Node connected to the head.
    # We’ll use a conditional loop to check which case we’re in.

    def add(self, element):
        # We’ll use an auxiliary variable called pointer to help traverse the list
        if self.head:
            # insertion when there are already elements in the list
            pointer = self.head  # This variable points to the memory space of the head
            while(pointer.next):  # This can be read as: while the pointer has a next value, it hasn’t reached the end yet
                pointer = pointer.next  # so if it hasn’t reached the end, move to the next node
            pointer.next = Node(element)  # when the list reaches the end, add the new element as the next Node
        else:
            # first insertion in the list
            self.head = Node(element)

        self._size += 1  # Just increasing the list size counter

    # We still can’t visualize the list’s elements yet.
    # Also, using _size directly is not a good Python practice.
    # Let’s create the special method __len__, which allows us to use len(list) like in standard Python lists.
    # By convention, we’ll use _size (with underscore) to avoid direct external access.
    
    def __len__(self):
        """Returns the length of the list"""
        return self._size 
    
    # Now we’ll create the method to access a specific element in the list.

    def get(self, index):
        pass

    # The set method modifies an element at a specific position in the list
    def set(self, index, element):
        pass

    # We use __getitem__ to overload the [] operator,
    # so that we can access elements by index like: list[0].
    # This is an example of operator overloading in Object-Oriented Programming.

    def __getitem__(self, index):
        # Like in the add() function, we need a pointer to navigate through the list.
        # We don’t modify self.head directly, otherwise we’d lose the list reference.
        pointer = self.head
        for i in range(index):
            # We check if the pointer is None, otherwise Python will raise an IndexError
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")
        # Now the pointer is at the desired position.
        # If it’s not None, we return the element.
        if pointer:
            return pointer.data
        raise IndexError("list index out of range")

    # Similarly to __getitem__, this method lets us replace an element
    # at a specific position using list[index] = value.
    def __setitem__(self, index, element):
        # Replacing an element works like __getitem__, but instead of returning, we assign.
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")
        # Instead of returning, we replace the element.
        if pointer:
            pointer.data = element
        else:
            raise IndexError("list index out of range")

    # Now let’s create a method to search for an element in the list.
    # In a linked list, searching is limited — we must traverse node by node,
    # unlike sequential allocation, where access is direct.
    def search(self, element):
        """Returns the index of an element in the list"""
        pointer = self.head
        i = 0  # variable to store the position of the element
        while(pointer):  # While the node is not None, check if its data matches the target
            if pointer.data == element:
                return i 
            # If not found, move to the next node and increment i
            pointer = pointer.next 
            i += 1
        # If the element is not in the list
        raise ValueError(f"Element {element} is not in the list")

# Example usage
linked_list = LinkedList()

linked_list.add(7)
linked_list.add(80)
linked_list.add(56)
print(linked_list[1])
print(linked_list.search(80))
