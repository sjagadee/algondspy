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

    def add_at_kth_pos(self, data, pos):
        new_node = Node(data)
        cur = self.head
        prev = None
        counter = 0
        index = pos - 1

        if self.head == None and pos == 1:
            self.head = new_node
            return
        elif pos == 1:
            new_node.next = cur
            self.head = new_node
        else:
            while counter < index and cur:
                prev = cur
                cur = cur.next
                counter += 1
            prev.next = new_node
            new_node.next = cur

    def get_nth_data(self, pos):
        cur = self.head
        counter = 0
        index = pos - 1

        while cur:
            if counter == index:
                return cur.data
            counter += 1
            cur = cur.next
        
        return None


llist = LinkedList()
llist.append("A")
llist.append("B")
llist.prepend("E")
llist.append("S")
llist.append("M")

llist.add_at_kth_pos("N", 10)

llist.print_list()

print("The 4rd element of the list: ", llist.get_nth_data(4))
