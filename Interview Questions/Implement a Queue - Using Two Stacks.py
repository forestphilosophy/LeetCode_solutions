class Queue2Stacks(object):
    
    def __init__(self):
        
        # Two Stacks
        self.stack = []
     
    def enqueue(self,element):
        
        self.stack.insert(0,element)
        
    def dequeue(self):
        
        return self.stack.pop()
