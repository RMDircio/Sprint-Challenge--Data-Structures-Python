class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
       # get the current value at the head
       node = self.head
       # set the head to None to start the list backwards
       self.head = None

       # while there is a node in the list
       while node:
           # put the current node(LinkedList (self)) at the head of the new(reversed) list
           ''' Since I am working in the LinkedList class, I can use "self" to call any function that 
           is part of the LinkedList class.'''
           # call LL class (self.) with adding to head function
           # brings the last elemnet (node.value) to the head of the list
           self.add_to_head(node.value)
           # reset node to the next node in the old list
           node = node.next_node
        
        







