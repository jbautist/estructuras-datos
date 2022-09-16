def maxheapify(array, tamaño, nodo_padre):
    # Declarando los nodos.
    nodo_izq = 2 * nodo_padre + 1
    nodo_der = 2 * nodo_padre + 2
    nodo_grande = nodo_padre

    # Buscando el nodo más grande.
    if nodo_izq < tamaño and array[nodo_izq] > array[nodo_grande]:
        nodo_grande = nodo_izq
    if nodo_der < tamaño and array[nodo_der] > array[nodo_grande]:
        nodo_grande = nodo_der
    
    # Si el nodo padre no es el más grande, intercambiarlo por el más grande y ordenar el heap.
    if nodo_grande != nodo_padre:
        array[nodo_padre], array[nodo_grande] = array[nodo_grande], array[nodo_padre]
        maxheapify(array, tamaño, nodo_grande)
    

class MaxHeap():
    def __init__(self):
        self.maxheap = []


    def insert(self, elemento):
        # Si el heap ya tiene elementos, después de insertar el nuevo elemento ordena el heap.
        if len(self.maxheap) == 0:
            self.maxheap.append(elemento)
        else:
            self.maxheap.append(elemento)
            tamaño = len(self.maxheap)
            for i in range((tamaño // 2) -1, -1, -1):
                maxheapify(self.maxheap, tamaño, i)


    def deletenode(self, elemento):
        # Busca el elemento a eliminar, lo intercambia por el último, lo elimina y ordena el heap.
        i = 0
        for i in range(0, len(self.maxheap)):
            if self.maxheap[i] == elemento:
                break
        
        self.maxheap[i], self.maxheap[-1] = self.maxheap[-1], self.maxheap[i]

        self.maxheap.pop()

        tamaño = len(self.maxheap)
        for i in range((tamaño // 2) -1, -1, -1):
            maxheapify(self.maxheap, tamaño, i)


# Ejemplo:
#
# heapmax1 = MaxHeap()
#
# heapmax1.insert(42)
# heapmax1.insert(38)
# heapmax1.insert(29)
# heapmax1.insert(22)
# heapmax1.insert(20)
# heapmax1.insert(17)
# heapmax1.insert(8)
# heapmax1.insert(12)
#
# heapmax1.deletenode(20)
#
# print(heapmax1.maxheap)