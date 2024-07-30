import time 

class process:
    pass

class Kernel: #kernel
    pass

class Memory: #allocazione memoria
    def __init__(self,memory):
        self.memory= memory

    def allocate(self):
        pass
    
    def free(self):
        pass

class scheduler: #gestione processi
    def __init__(self,element, maxSize=5):
        self.element=element
        self.maxSize=maxSize
        self.Q=[]

    def queue(self):
        self.Q=self.element[:self.maxSize]
        return ' initialize_queue '
    
    def methods_queue(self):
        if self.maxSize <= 0: return 'infinite queue'
        if len(self.element) < self.maxSize: # fewer elements compared to maxSize
            return self.Q
        else:     
            for x in self.element[len(self.Q):]:
                self.Q.append(x)
                self.Q.pop(0)
            return self.Q
        

S=scheduler([1,2])
print(S.queue())
print(S.methods_queue())
        
# Q = []

# def queue(x,element, maxSize=5): # queue
#     if maxSize <=0: return 'infinite queue'
#     if x <= element:  
#         if len(Q) < maxSize:
#             Q.append(x)
#         else:
#             Q.pop(0)  
#             Q.append(x)
#         return queue(x + 1, element, maxSize)
#     return Q


# print(queue(0, 20, 5))