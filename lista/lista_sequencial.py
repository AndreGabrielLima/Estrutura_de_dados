# Listas em são usadas para armazenar vários dados relacionados entre si por meio de uma mesma variável
# Porém, isso não é exclusivo da lista, mas sim a forma como os dados são armazenados e também como são
# realizadas algumas operações, principalmente as operações: busca, inserção e remoção. 

# Para criar uma lista em python, usamos os [] e atribuímos seus valores

lista = [94, 7, 3, 56]

# Após a criação, podemos acessar os valores através de índices lista[1]. O [1] é o índice do elemento

lista[1]

# Dessa forma, python nos permite acessar dados de maneira aleatória, diretamente na memória
# Isso se dá, pq a lista está sendo alocados sequencialmente, um do lado do outro. 
# Porém, em python conseguimos adicionar mais de um tipo de dado numa lista, o que quebra essa sequência.
# Para isso, a linguagem usa a forma de ponteiros para identificar os endereços na memória dos valores
# A notação Big O para essa estrutura é O(1), ou seja, Linear.

# Vamos agora criar uma função de busca linear para se apresentado de maneira mais eficiente.
# A ideia é simples, uma função que lê o que queremos, e procura se é igual ou não ao que está na lista. 
# Começando do índice 0 e indo até o último, encontrando o elemento desejado.

def busca(lista, elem): # A função precisa de dois argumento, a lista para ser feito a busca, e o elmento
    for i in range(len(lista)):
        """Retornará o local do elemento se ele estiver na lista, ou None caso não esteja"""
        if lista[i] == elem:
            return i
    return None

lista_estranha = [8, '5', 32, 0, 'python', 11] # Lista qualquer para fazer o teste
elemento = 50 # Escolha do elemento para fazer a busca 

indice = busca(lista_estranha, elemento) # Chamando a função para buscar na lista passando os parâmetros 

# Laço condicional para testar se a função de busca esta funcionando
if indice is not None:
    print("O índice do elemento {} é {}".format(elemento, indice))
else:
    print("O elemento {} não se encontra na lista".format(elemento))
    

################# IN ENGLISH #################

# Lists in Python are used to store multiple related pieces of data within a single variable.
# However, this is not exclusive to lists, but rather refers to how data is stored and how
# certain operations are performed — mainly the operations of searching, inserting, and deleting.

# To create a list in Python, we use [] and assign its values:

lista = [94, 7, 3, 56]

# After creation, we can access the values through indices like lista[1]. The [1] is the element’s index.

lista[1]

# In this way, Python allows us to access data randomly, directly from memory.
# This happens because the list is allocated sequentially, one element next to the other.
# However, in Python, we can add different data types to a list, which breaks this sequence.
# To handle this, the language uses pointers to identify the memory addresses of each value.
# The Big O notation for this access operation is O(1).

# Now let's create a linear search function to demonstrate this more efficiently.
# The idea is simple: a function that takes a target value and searches whether it exists
# in the list by comparing each element sequentially — starting from index 0 up to the last one.

def search(lst, element):  # The function takes two arguments: the list to search in and the element to find.
    for i in range(len(lst)):
        """Returns the index of the element if it is found in the list, or None if it is not."""
        if lst[i] == element:
            return i
    return None

strange_list = [8, '5', 32, 0, 'python', 11]  # Random list to test the function
element = 50  # Element chosen for the search

index = search(strange_list, element)  # Calling the search function and passing the parameters

# Conditional block to test if the search function is working correctly
if index is not None:
    print("The index of the element {} is {}".format(element, index))
else:
    print("The element {} was not found in the list".format(element))


