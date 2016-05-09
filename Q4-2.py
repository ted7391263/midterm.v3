class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def show(self):
        print (self.items)




q = Queue()
q.enqueue('cat')
q.show()
q.enqueue(True)
q.show()
q.enqueue(4)
q.show()
q.dequeue()
q.show()
q.dequeue()
q.show()
q.dequeue()
q.show()
