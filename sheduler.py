'''
In SJF, the CPU is allocated to the 
process with smallest burst time. When the CPU becomes available, it is assigned to the process 
that has the smallest next CPU burst tipo di priorità

'''

import time 
from termcolor import colored, cprint 
from memory import Memory
'''
Burst_Time would be the time that the proccess need to be executes call BURST TIME
'''

# arrival time 
class process:
    def __init__(self, name, memory_required, Burst_Time): # Burst_Time is in milliseconds
        self.name=name
        self.memory_required=memory_required
        self.Burst_Time=Burst_Time
        self.remaining_time=Burst_Time
        self.waiting_time=0

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
 Quantum/time interval is the time the the scheduler give to all process 
 Shortest Job First chi ha il Burst_Time piu basso ha una priorità più alta 
'''
class scheduler: # gestione processi
    def __init__(self, n_process, Quantum=5, maxSize=2):
        self.n_process= n_process
        self.maxSize=maxSize
        self.Quantum=Quantum * 10 # s instead ms
        self.Q=[]
    
    def bulbe_sort(self):
        pass
        # L=len(self.n_process) - 1
        # for y in range(L): #time O(n**2)
        #     for j in range((L) - y):
        #         if self.n_process[j]['Burst_Time'] > self.n_process[j + 1]['Burst_Time']: 
        #             self.n_process[j]['Burst_Time'] , self.n_process[j + 1]['Burst_Time'] = self.n_process[j + 1]['Burst_Time'], self.n_process[j]['Burst_Time'] 
        # return self.n_process
    
    def queue(self):
        if self.maxSize <= 0: return 'infinite queue'
        elif len(self.n_process) < self.maxSize: # fewer elements compared to maxSize
            return self.n_process
        else: 
            self.n_process=self.n_process[:self.maxSize]
            return self.n_process  #preparation queue follow Algorithms ORR or SORR (the best)


    # TODO sistemare tutto questo processo deve fare il ciclo ad ogni elemento e togliere gli elementi che hanno finito con il tempo 
    def round_robin(self):
        complete_process=[]
        while self.n_process != []: # methods n queue
            for x in self.n_process:
                x['remaining_time']-= self.Quantum
                if  x['remaining_time'] <= 0 :
                    x['remaining_time']= 0 
                    self.n_process.remove(x)
                    complete_process.append(x)
        return (complete_process, self.n_process)
    
    def __str__(self):
       return str(self.Q)

P=[process('process1',256,50).__dict__,
   process('process2',256,90).__dict__,
   process('process3',256,10).__dict__,
   process('process4',256,33).__dict__,]

# M=Memory(8192) # simulazione di 1 KB RAM 
# for x in P:
#     x.run(10)
#     M.allocate(x.memory_required)

S=scheduler(P,maxSize=5)
# S.bulbe_sort()
S.queue()
print(S.round_robin())
# Memory management in Python involves a private heap containing all Python objects and data structures.

