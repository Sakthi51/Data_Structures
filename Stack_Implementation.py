#Reference (https://www.youtube.com/watch?v=pMh_OX3ipHE)

stack = []
top = -1
class Stack_implementation():
    def __init__(self):
        self.stack = []
        self.top = -1

    def push(self, value):
        self.top+=1
        self.stack.append((value))

    def pop(self):
        if self.stack == -1:
            print("Stack is empty now")
        self.top-=1
        x = self.stack.pop()
        return x

    def peek(self):
        return self.stack[self.top]

    def print_stack(self):
        for i in range(self.top, -1, -1):
            if i == self.top:
                print("--->", self.stack[i], "<---")
            else:
                print(self.stack[i])

s = Stack_implementation()
s.push('S')
s.push('A')
s.push('K')
s.push('T')
s.push('H')
s.push('I')
# s.print_stack()

# s_stack=s.stack
# x = ''
# for i in range(len(s_stack)):
#     x += s.pop()
# print(x)
top_s = s.top    #The value of top stored
s_stack=s.stack  #The value of s object stored in s_stack as list
x=''
for i in range(top_s, -1, -1):
    x += s_stack[i]
print(x)

