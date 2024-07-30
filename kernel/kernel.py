import time 

class process:
    def __init__(self, name, memory_required):
        self.name=name
        self.memory_required=memory_required

    def __str__(self):
        return f"Process(name={self.name}, memory_required={self.memory_required})"
    
    def __repr__(self) -> str:
        return self.__str__()
        
    def run(self):
        print(f'{self.name} terminated')      
    
class scheduler: #gestione processi
    def __init__(self, n_process, maxSize=5):
        self.n_process= n_process
        self.maxSize=maxSize
        self.Q=[]
        
    def queue(self):
        n=0
        if self.n_process <= self.maxSize: n = self.n_process
        else : n = self.maxSize
        self.Q=[process(x,200) for x in range(n)] #start queue
        return self.Q
    
    def methods_queue(self):
        if self.maxSize <= 0: return 'infinite queue'
        if self.n_process < self.maxSize: # fewer elements compared to maxSize
            return self.Q
        else:     
            for x in  range(self.maxSize, self.n_process + 1): # methods n queue
                y=process(x,200)
                self.Q.append(y)
                self.Q.pop(0)
            return self.Q
    
    def __str__(self):
       return str(self.Q)
     
# class Kernel: #kernel
#     def __init__(self, sheduler):
#         self.memory= Memory(1024)
#         self.scheduler=sheduler
    
#     def run(self):
#         print(self.memory.allocate(200))
        
# M=Memory(1024)

# class Memory: #allocazione memoria
#     def __init__(self,memory):
#         self.memory= memory
#         self.used_memory=0

#     def allocate(self,space):
#         self.used_memory += space
#         if self.used_memory <= self.memory: print(f'memoria allocata {space} memoria disponibile {  self.memory - (self.used_memory + space) }')
#         else: print(f'memoria allocata {self.used_memory} supera {space}')
    
#     def free(self, space):
#         self.used_memory -= space
#         print(f'memoria liberata di {space}')

S=scheduler(20)
S.queue()
S.methods_queue()
print(S)
# K=Kernel(S)
# K.run()
# print(S.queue())
# print(S.methods_queue())

# for x in range(20):
#     S=scheduler(x)
#     S.element.run()
    # print(S.queue())

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