lst1 = [2, 3, 1, 4, 5]

class stack:
    
    def __init__(self):
        self.stack = []
    
    def isEmpty(self):
        return len(self.stack) == 0

    def push(self, e):
        self.stack.append(e)

    def pop_stack(self):
        if not self.isEmpty():
            return self.stack.pop()
    def returnSTK(self):
        return self.stack
    def revSTK(self):
        return self.stack[::-1]

stk1 = stack()
stk2 = stack()

while len(lst1) > 0:
    l1 = min(lst1)
    stk1.push(l1)
    s = lst1.pop()
    if s > l1:    
        stk2.push(s)

'''print("Sorted stack 1:")
while not stk1.isEmpty():
    print(stk1.pop_stack())

print("Sorted stack 2:")
while not stk2.isEmpty():
    print(stk2.pop_stack())'''


for x in stk1.revSTK():
    if x not in stk2.returnSTK():
        stk2.push(x)


print('Final sorted stack :', stk2.revSTK())
