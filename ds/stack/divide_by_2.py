"""
  Use a stack to convert integer to binary

  let us take the value 242

  242/2 = 121   --> 0
  121/2 = 60    --> 1
  60/2 = 30     --> 0
  30/2 = 15     --> 0
  15/2 = 7      --> 1
  7/2 = 3       --> 1
  3/2 = 1       --> 1
  1/2 = 0       --> 1

  11110010 is the binary value of int 242

"""

from stack import Stack

def div_by_2(int_val):
    s = Stack()

    while int_val > 0:
        reminder = int_val % 2
        s.push(reminder)
        int_val = int_val // 2
    
    binary_val = ''
    while not s.is_empty():
        binary_val += str(s.pop())
    
    return binary_val

print(div_by_2(242))