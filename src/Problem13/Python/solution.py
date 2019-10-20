class MaxStack:
    def __init__(self):
        self.stack = []

    def __len__(self):
        return len(self.stack)
    
    def push(self, val):
        self.stack.append(val)

    def pop(self):
        return self.stack.pop()

    def max(self):
        temp = self.stack[:]
        currMax = 0
        while not (len(temp) == 0):
            tempo = temp.pop()
            if currMax <= tempo:
                currMax = tempo
        return currMax

s = MaxStack()
s.push(1)
s.push(2)
s.push(3)
s.push(2)
print(s.max())
# 3
s.pop()
s.pop()
print(s.max())
# 2
