class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head

        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            return
        
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            return

        new_node.next = self.head
        self.head = new_node


llist = LinkedList()
llist.append("A")
llist.append("B")
llist.prepend("E")
llist.append("S")
llist.append("M")

llist.print_list()
