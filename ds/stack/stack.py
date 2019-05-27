# Stack data structure

class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if not self.items == []:
            return self.items[-1]

    def is_empty(self):
        return self.items == []
    
    def get_stacks(self):
        return self.items
