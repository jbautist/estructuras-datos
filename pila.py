class Stack():
    def __init__(self):
        self.pila = []
    
    
    def push(self, elemento):
        self.pila.append(elemento)


    def pop(self):
        try:
            self.pila.pop()
        except IndexError:
            raise Exception('pila vacía')


    def top(self):
        try:
            return self.pila[-1]
        except IndexError:
            raise Exception('pila vacía')