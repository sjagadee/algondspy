from stack import Stack

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