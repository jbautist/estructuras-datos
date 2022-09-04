class Queue():
    def __init__ (self):
        self.cola = []
        
    
    def enqueue(self, elemento):
        self.cola.append(elemento)
            
    
    def dequeue(self):
        try:
            self.cola.pop(0)
        except IndexError:
            raise Exception('cola vacía')


    def front(self):
        try:
            return self.cola[0]
        except IndexError:
            raise Exception('cola vacía')