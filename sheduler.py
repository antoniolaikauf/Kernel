import time 
from termcolor import colored, cprint 
from memory import Memory
'''
Burst_Time would be the time that the proccess need to be executes call BURST TIME
'''
class process:
    def __init__(self, name, memory_required, Burst_Time): # Burst_Time is in milliseconds
        self.name=name
        self.memory_required=memory_required
        self.Burst_Time=Burst_Time
        self.remaining_time=Burst_Time

    # def __str__(self):
    #     return {'name':self.name}
    
    # def __repr__(self):
    #    return  process.__str__(self)
        
    def run(self,Quantum): # Quantum is in milliseconds
        T=max(self.remaining_time,Quantum)
        T-=Quantum
        time.sleep(T * 0.1) # milliseconds
        if T == 0 : cprint(f'finished execution: {self.name}','red')
        else : cprint(f'not finished: {self.name}, time left:{T * 0.1:.2f}s' ,'blue')
        return T

'''
 Quantum is the time the the scheduler give to all process 
 Shortest Job First chi ha il Burst_Time piu basso ha una priorità più alta 
'''
class scheduler: # gestione processi
    def __init__(self, n_process, Quantum=5, maxSize=2):
        self.n_process= n_process
        self.maxSize=maxSize
        self.Quantum=Quantum
        self.Q=[]
    
    def bulbe_sort(self):
        L=len(self.n_process) - 1
        for y in range(L):
            for j in range((L) - y):
                if self.n_process[j]['Burst_Time'] > self.n_process[j + 1]['Burst_Time']: 
                    self.n_process[j]['Burst_Time'] , self.n_process[j + 1]['Burst_Time'] = self.n_process[j + 1]['Burst_Time'], self.n_process[j]['Burst_Time'] 
        return self.n_process
    
    def queue(self):
        self.Q=self.n_process[:self.maxSize] #start queue
        return self.Q

    # TODO sistemare tutto questo processo deve fare il ciclo ad ogni elemento e togliere gli elementi che hanno finito con il tempo 
    def methods_queue(self):
        E=[]
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

P=[process('process1',256,50).__dict__,
   process('process2',256,90).__dict__,
   process('process3',256,10).__dict__,
   process('process4',256,33).__dict__,]

# M=Memory(1024) # simulazione di 1 KB RAM 
# for x in P:
#     x.run(10)
#     M.allocate(x.memory_required)

S=scheduler(P,2)
S.bulbe_sort()
print(S.queue())
# Memory management in Python involves a private heap containing all Python objects and data structures.

