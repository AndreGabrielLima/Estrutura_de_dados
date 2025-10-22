# Uma lista sequencial de memória é preciso reservar um espaço de memória alocado sequencialmente para ser inserido.

# A ideia de Alocação Encadeada ou Alocação Dinâmica de memória é permitir que os elementos sejam armazenados em espaços 
# quaisquer da memória. Além disso, eles só seriam alocados no momento que fosse preciso. É preciso apenas ver como unir a lista.
# Para isso, surge a ideia de um Nó para unir essas listas. 

# O Nó é como se fosse um envelope, em que dentro haverá o dado, ou seja, o elemento, e fora está a posição do próximo Nó.
# Dessa forma, os elementos não precisam ficar alocados sequencialmente, mas podem ficar jogados na memória, sendo identificados
# através dos nós onde esta a posição dos elementos.

# Caso não esteja entendendo, vamos pensar essa ideia de Nó como se fosse um trem. Cada vagão existe de maneira independente
# e podem estar em qualquer lugar, igual os nós podem estar em qualquer lugar. Dentro de cada vagão podemos guardar objetos, 
# assim como em um Nó podemos armazenar dados de interesse. Cada vagão possui um gancho que liga ao outro, igual que em cada Nó
# possui um espaço na memória que conhece onde está o Nó seguinte. A diferença entre o trem e o lógica do Nó, é que no trem
# você consegue andar para trás e para frente, enquanto no Nó você só anda para frente, pois não há um espaço que guarda o Nó anterior
# apenas o que vem em seguida. Isso nós podemos resolver guardando o Nó atual em uma variável, mas veremos isso mais para frente. 

class Node:
    # Aqui estamos inicializando a classe Node
    def __init__(self, data): # Vimos que o Nó (Node) armazena duas especificações, que é o elemento(dado) e o endereço do próximo Nó
        self.data = data
        self.next = None

# Este é o código que será usado para criação do Nó. A lista encadeada irá fazer uso desse arquivo através do import para conseguir usar.
# O que dá para fazer e verificar o uso do Nó é criar instâncias para ligar os Nós e entender como funciona.

# Teste do nó

no1 = Node(5) # Instância = objeto da classe. É como se fosse o corpo onde será usado.
no2 = Node(9)

print(no1.data) # Irá mostrar o dado que está em no1
print(no1.next) # Irá mostrar None pois não foi feita a ligação dos Nós

no1.next = no2 # Aqui estamos fazendo a ligação do Nó no1 para o no2
print(no1.next) # Agora é possível ver onde está localizado o no2 na memória

print(no1.next.data) # Aqui estamos pedindo o dado do próximo Nó, ou seja, virá o dado de no2 que é 9'''



################# IN ENGLISH #################



# A sequential memory list requires reserving a block of memory allocated sequentially for inserting elements.

# The idea of Linked Allocation or Dynamic Memory Allocation is to allow elements to be stored
# in any available memory space. They are only allocated when needed. The key challenge is how to connect them.
# For that, we use the concept of a Node to link these elements together.

# A Node works like an envelope — inside it, we have the data (the element), and outside,
# we have the position (or reference) of the next Node.
# This way, elements don’t need to be stored sequentially in memory;
# instead, they can be scattered, and each Node knows where the next Node is located.

# If this sounds confusing, imagine the concept of a Node as a train.
# Each wagon exists independently and could be anywhere, just like Nodes in memory.
# Inside each wagon, we can store objects (our data),
# and each wagon has a hook that connects to the next one — similar to how a Node stores a reference to the next Node.
# The difference between a train and a Node structure is that, in a train, you can move both forward and backward,
# but in a singly linked list (Node), you can only move forward,
# since each Node only knows the next Node, not the previous one.
# We could solve this by storing the current Node in a variable, but we’ll see that later.

# This is the code used to create a Node. A linked list will import this file to use the Node structure.
# To test how it works, we can create instances to connect Nodes and understand the logic.

# Test

node1 = Node(5)  # Instance = object of the class. It’s like the body that will be used.
node2 = Node(9)

print(node1.data)  # This will show the data stored in node1
print(node1.next)  # This will show None since the Nodes are not yet linked

node1.next = node2  # Here we link node1 to node2
print(node1.next)   # Now we can see where node2 is located in memory

print(node1.next.data)  # This prints the data of the next Node — in this case, node2's data, which is 9
