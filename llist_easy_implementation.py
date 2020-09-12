
# Node Operations:
# has next() gives out a boolean True or False if there is a next node or not, basically return True for any note than the last node


class Node(object):

    def __init__ (self, d, n = None): # d = passing in a piece of data, n = optionally, we can pass in the next node and if theres is no next node to pass in it's set to none
        self.data = d
        self.next_node = n

    def get_next (self): # we're just returning self.next_node
        return self.next_node

    def set_next (self, n): # we pass in self.next_node and it equals n
        self.next_node = n

    def get_data (self):
        return self.data

    def set_data (self, d):
        self.data = d


class LinkedList (object):

    def __init__(self, r = None): # if there is no root node passed in it's set to none by default for probably the most cases by new linkedlists
        self.root = r
        self.size = 0 # size will be initalized to zero

    def get_size (self): # get_size() want to get the size of the list, the size in this case is the number of nodes in the list
        return self.size

    def add (self, d): # we've adding this new piece of data 'd' to a new node at the very beginning of the list
        new_node = Node (d, self.root) # creating a new node with the data using self.root as the next node
        self.root = new_node # we set our root pointer to this new node because the new node is becoming the root
        self.size += 1 # we increment the size by 1

    def remove (self, d): # first we have to iterate through the list to find and can than remove it
        this_node = self.root
        prev_node = None # we need the previous node to delete a node

        while this_node: # means basically while we are not at the end of the list, because only the last node will have no next node
            if this_node.get_data() == d: # if this nodes data is the data we are looking for:
                if prev_node: # and if we are not in the root node
                    prev_node.set_next(this_node.get_next()) # we are going to bypass this_node every time we iterate through the list
                else: 
                    self.root = this_node.get_next() # if the data we are lloking for is in the root node we set the root pointer to the node after the root
                self.size -= 1 # decrement the size by 1
                return True		# data removed
            else: 
                prev_node = this_node # if not we are going to increment the previos node to this node
                this_node = this_node.get_next() # and this node to next node
        return False  # data not found

    def find (self, d):
        this_node = self.root
        while this_node:
            if this_node.get_data() == d:
                return d
            else:
                this_node = this_node.get_next()
        return None
        

def main():
    myList = LinkedList()
    myList.add(5)
    myList.add(8)
    myList.add(12)
    print("size="+str(myList.get_size()))
    myList.remove(8)
    print("size="+str(myList.get_size()))
    print(myList.remove(12))
    print("size="+str(myList.get_size()))
    print(myList.find(5))

main()