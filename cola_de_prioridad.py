# Cola de prioridad implementada con una estructura max heap
# donde el elemento más grande es el de mayor prioridad.


def maxheapify(array, tamaño, nodo_padre):
    nodo_izq = 2 * nodo_padre + 1
    nodo_der = 2 * nodo_padre + 2
    nodo_grande = nodo_padre

    if nodo_izq < tamaño and array[nodo_izq] > array[nodo_grande]:
        nodo_grande = nodo_izq
    if nodo_der < tamaño and array[nodo_der] > array[nodo_grande]:
        nodo_grande = nodo_der

    if nodo_grande != nodo_padre:
        array[nodo_padre], array[nodo_grande] = array[nodo_grande], array[nodo_padre]
        maxheapify(array, tamaño, nodo_grande)


class ColaPrioridad():
    def __init__(self):
        self.colaprioridad = []

    
    def insert(self, elemento):
        # Si la cola ya tiene elementos, después de insertar el nuevo elemento ordena el heap.
        if len(self.colaprioridad) == 0:
            self.colaprioridad.append(elemento)
        else:
            tamaño = len(self.colaprioridad)
            self.colaprioridad.append(elemento)
            for i in range((tamaño // 2) -1, -1, -1):
                maxheapify(self.colaprioridad, tamaño, i)


    def delete(self):
        # Intercambia el primer elemento (el de mayor prioridad) por el último elemento,
        # lo elimina y ordena el heap desde la raíz.
        self.colaprioridad[0], self.colaprioridad[-1] = self.colaprioridad[-1], self.colaprioridad[0]
        self.colaprioridad.pop()
        maxheapify(self.colaprioridad, len(self.colaprioridad), 0)


    def front(self):
        return self.colaprioridad[0]


# Ejemplo:
#
# colaprio1 = ColaPrioridad()
#
# colaprio1.insert(29)
# colaprio1.insert(22)
# colaprio1.insert(42)
# colaprio1.insert(20)
# colaprio1.insert(17)
# colaprio1.insert(8)
# colaprio1.insert(12)
# colaprio1.insert(38)
#
# colaprio1.delete()
# colaprio1.delete()
#
# print(colaprio1.colaprioridad)