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
        if self.maxSize <= 0: return 'infinite queue'
        # if self.element <= self.maxSize :
        #     if len(self.Q) < self.maxSize:
        #         self.Q.append(self.element)
        #     else:
        #         self.Q.pop(0)
        #         self.Q.append(self.element)
        # return self.Q
        


        
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