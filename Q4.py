class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        return self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def show(self):
        print (self.items)

q = Queue()
print(q)
print(q.isEmpty())
q.enqueue(4)
q.enqueue('dog')
q.show()
print(q.isEmpty())
q.dequeue()
print(q.size())

