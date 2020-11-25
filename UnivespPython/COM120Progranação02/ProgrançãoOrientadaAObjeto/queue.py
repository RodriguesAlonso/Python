class Queue:

    def __init__(self):
        self.fila = []
        self.primeiro = None

    def enqueue(self, item):
        self.fila.append(item)

    def dequeue(self):
        try:
            return self.fila.pop(0)
        except:
            print('fim da fila')

    def isempty(self):
        return len(self.fila) == 0
