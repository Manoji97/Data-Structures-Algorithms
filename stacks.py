class stack:
    def __init__(self):
        self.stack = []
        
    def is_empty(self):
        return len(self.stack) == 0
    
    def push(self,data):
        self.stack.append(data)
    
    def peek(self):
        return self.stack[-1]
    
    def pop(self):
        return self.stack.pop()

    def show_size(self):
        return len(self.stack)
    
class Queue:
    def __init__(self):
        self.queue = []
        
    def is_empty(self):
        return len(self.queue) == 0
    
    def enqueue(self,data):
        self.queue.append(data)
    
    def peek(self):
        return self.queue[0]
    
    def dequeue(self):
        a =  self.queue[0]
        del self.queue[0]
        return a
    
    def show_size(self):
        return len(self.queue)
    

    
    
    
    
    
    