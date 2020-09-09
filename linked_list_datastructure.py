class LinkedList:
    def __init__(self, nodes = None):
        self.head = None # creating the starting point of the linked list
        if nodes is not None:
            node = Node(data = nodes.pop(0))
            self.head = node
            for element in nodes:
                node.next = Node(data = element)
                node = node.next
    
    def __repr__(self): # only to have a more helpful representation of the objects
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append('None')
        return '-->'.join(nodes)
    

class Node: # creating the two main elements of the node data and next pointer
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self): # only to have a more helpful representation of the objects
        return self.data

llist = LinkedList(['a', 'b', 'c', 'd', 'e'])


print(llist)