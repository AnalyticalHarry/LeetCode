


class counter:
    
    def __init__ (self, init):
        self.current = init 
        self.init = init
    
    def increment(self):
        self.current += 1
        return self.current 
    
    def decrement(self):
        self.current -= 1
        return self.current
        
    def reset(self):
        self.current = self.init
        return self.current 

counter = counter(5)
print(counter.increment())
print(counter.decrement())
print(counter.reset())  
