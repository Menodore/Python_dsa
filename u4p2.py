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
    
def ParanthesisChecker(exp):
    open_p="{[(<"
    close_p="}])>"
    s=stack()
    for x in exp:
        if x in open_p:
            s.push(x)
        elif x in close_p:
            if s.isEmpty():
                return False
            if open_p.index(s.pop_stack()) != close_p.index(x):
                return False
    return s.isEmpty()


m = input('ENTER YOUR EXPRESSION:')
if ParanthesisChecker(m) == True:
    print('VALID')
else :
    print('INVALID')
 