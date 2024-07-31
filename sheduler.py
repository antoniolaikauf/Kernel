import time 
from termcolor import colored, cprint 
'''
Burst_Time would be the time that the proccess need to be executes call BURST TIME
'''
class process:
    def __init__(self, name, memory_required, Burst_Time): # Burst_Time is in milliseconds
        self.name=name
        self.memory_required=memory_required
        self.Burst_Time=Burst_Time
        self.remaining_time=Burst_Time

    def __str__(self):
        return f"name={self.name}, remaining_time={self.remaining_time})"
        
    def run(self,Quantum): # Quantum is in milliseconds
        T=max(self.remaining_time,Quantum)
        T-=Quantum
        time.sleep(T * 0.1) # milliseconds
        if T == 0 : cprint(f'finished execution: {self.name}','red')
        else : cprint(f'not finished: {self.name}, time left:{T * 0.1:.2f}s' ,'blue')
        return T

'''
 Quantum is the time the the scheduler give to all process 
'''
class scheduler: # gestione processi
    def __init__(self, n_process, Quantum=5, maxSize=2):
        self.n_process= n_process
        self.maxSize=maxSize
        self.Quantum=Quantum
        self.Q=[]
        
    def queue(self):
        self.Q=self.n_process[:self.maxSize] #start queue
        return self.Q
    
    # TODO sistemare tutto questo processo deve fare il ciclo ad ogni elemento e togliere gli elementi che hanno finito con il tempo 
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

for x in P:
    x.run(10)


# S=scheduler(P,10)
# S.queue()
# S.methods_queue()
# print(S)

