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


Q=[]
def queue(x,maxSize=5): #first in first out
    if maxSize <=0: return ' queue infinite'
    if len(Q) < maxSize: Q.append(x)
    else:
        Q.insert(0,x)
        Q.pop(-1)
    return Q

for x in range(10):
    print(queue(x,5))
    # time.sleep(1)

