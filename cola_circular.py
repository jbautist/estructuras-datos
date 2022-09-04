class CircularQueue():
    def __init__(self, capacidad):
        self.colacircular = [None] * capacidad
        self.capacidad = capacidad
        self.frente = self.final = -1


    def enqueue(self, elemento):
        if self.frente == -1:
            self.frente = self.final = 0
            self.colacircular[self.final] = elemento 
        elif None in self.colacircular:
            self.final = (self.final + 1) % self.capacidad
            self.colacircular[self.final] = elemento
        else:
            raise Exception('cola circular llena')
    

    def dequeue(self):
        if self.frente == self.final and self.frente != -1:
            self.colacircular[self.frente] = None
            self.frente = self.final = -1
        elif self.frente != -1:
            self.colacircular[self.frente] = None
            self.frente = (self.frente + 1) % self.capacidad
        else:
            raise Exception('cola circular vacía')
                   

    def front(self):
        if self.frente != -1:
            return self.colacircular[self.frente]
        else:
            raise Exception('cola circular vacía')