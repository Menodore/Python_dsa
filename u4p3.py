#creation of queue class

class Q:
    def __init__(self):
        self.queue=[]
    
    def ifEmpty(self):
        return len(self.queue)==0
    def enqueue(self,item):
        self.queue.append(item)
    def dequeue(self):
        if self.ifEmpty():
            print("Underflow")
        else:
            self.queue.pop(0)
    def display(self):
        return self.queue[::-1]


a=Q()

a.enqueue(5)
a.enqueue(4)
a.enqueue(34)

a.dequeue()

print(a.display())