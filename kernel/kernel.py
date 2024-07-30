import time 


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
    pass

Q = []

def queue(x,element, maxSize=5): # queue
    if maxSize <=0: return 'infinite queue'
    if x <= element:  
        if len(Q) < maxSize:
            Q.append(x)
        else:
            Q.pop(0)  
            Q.append(x)
        return queue(x + 1, element, maxSize)
    return Q


print(queue(0, 20, 5))