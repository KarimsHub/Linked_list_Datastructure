class Node:
    def __init__(self, value, nextNode = None):
        self.value = value
        self.nextNode = nextNode

class LinkedList:
    def __init__(self,head = None):
        self.head = head

    def insert(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            return
    
        currentNode = self.head
        while True:
            if currentNode is None:
                currentNode.nextNode = Node
                break
            currentNode = currentNode.nextNode

    def printllist(self):
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.value)
            currentNode = currentNode.nextNode
        print('None')


llist = LinkedList()
llist.printllist()
llist.insert('3')
llist.printllist()