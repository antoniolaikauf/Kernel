'''
|p1|p1|p2|p3|p4|p5|p1|p2|p3|p4|p5|p2|p3|p4|p5|p2|p3|p4|p5|p2|p3|p3|
0  4  8 12 16  20 24 28 32 36 40 44 48 52 56 60 64 68 69 72 75 79 80


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
    def __init__(self, name, memory_required, Burst_Time,arrival_time): # Burst_Time is in milliseconds
        self.name=name
        self.memory_required=memory_required
        self.Burst_Time=Burst_Time
        self.remaining_time=Burst_Time
        self.arrival_time=arrival_time
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
        self.Quantum=Quantum 
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
        queue=[]
        if self.maxSize <= 0: return 'infinite queue'
        if len(self.n_process) > self.maxSize: # fewer elements compared to maxSize
             self.n_process=self.n_process[:self.maxSize]
        for i in range(len(self.n_process)):
            queue.append(self.n_process[i])
            time.sleep(self.n_process[i]['arrival_time'])
        print(queue)
        return queue  #preparation queue follow Algorithms ORR or SORR (the best)

    def round_robin(self):
        complete_process=[]
        
        while self.n_process != []: # methods n queue
            self.n_process[0]['remaining_time'] -= self.Quantum
            if self.n_process[0]['remaining_time'] <= 0: #rimozione processo dalla ueue
               self.n_process[0]['remaining_time']=0
               complete_process.append(self.n_process[0])
               self.n_process.pop(0)
            else:
                self.n_process= self.n_process[1:] + [self.n_process[0]] # elemento aggiunto alla coda della queue
            time.sleep(self.Quantum) 
            print(self.n_process)

        # return complete_process
    
    def __str__(self):
       return str(self.Q)

P=[process('process1',256,5,0).__dict__,
   process('process2',256,9,2).__dict__,
   process('process3',256,1,2).__dict__,
   process('process4',256,3,2).__dict__,]

# M=Memory(8192) # simulazione di 1 KB RAM 
# for x in P:
#     x.run(10)
#     M.allocate(x.memory_required)


S=scheduler(P,maxSize=7)
# S.bulbe_sort()
S.queue()
# print(S.round_robin())
# Memory management in Python involves a private heap containing all Python objects and data structures.

