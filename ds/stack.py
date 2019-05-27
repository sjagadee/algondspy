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

s = Stack()
print(s.is_empty())
s.push('A')
s.push('B')
s.push('C')
s.push('D')

print("Get Stack", s.get_stacks())
print("Pop", s.pop())
print("Peek", s.peek())
print("Get Stack", s.get_stacks())