import time 
'''
time would be the time that the proccess need to be executes call BURST TIME
'''
class process:
    def __init__(self, name, memory_required, Burst_Time): 
        self.name=name
        self.memory_required=memory_required
        self.Burst_Time=Burst_Time

    def __str__(self):
        return f"Process(name={self.name}, memory_required={self.memory_required}, time={self.Burst_Time})"
    
    def __repr__(self):
        return self.__str__()
        
    def run(self):
        print(f'{self.name}')   

class scheduler: # gestione processi
    def __init__(self, n_process, Quantum=5, maxSize=2):
        self.n_process= n_process
        self.maxSize=maxSize
        self.Quantum=Quantum
        self.Q=[]
        
    def queue(self):
        self.Q=self.n_process[:self.maxSize] #start queue
        return self.Q
    
    def methods_queue(self):
        if self.maxSize <= 0: return 'infinite queue'
        if len(self.n_process) < self.maxSize: # fewer elements compared to maxSize
            return self.Q
        else:     
            for x in  range(self.maxSize, len(self.n_process)): # methods n queue
                self.Q.append(self.n_process[x])
                self.Q.pop(0)
            return self.Q
    
    def __str__(self):
       return str(self.Q)

P=[process('process1',200,10),
   process('process2',200,100),
   process('process3',200,20),
   process('process4',200,33),
   process('process5',200,56)]


S=scheduler(P,10)
S.queue()
S.methods_queue()
print(S)

