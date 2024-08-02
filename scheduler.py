import time 
import sys
from datetime import datetime
from termcolor import colored, cprint 
from memory import Memory
'''
Burst_Time would be the time that the proccess need to be executes call BURST TIME
'''
SJF=False
if len(sys.argv) > 2: raise Exception('add more than two parapeters')
if len(sys.argv) == 2: 
  SJF=True
class process:
    def __init__(self, name, memory_required, Burst_Time, arrival_time): # Burst_Time is in milliseconds
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
        
    def run(self): # Quantum is in milliseconds
        # T=max(self.remaining_time,Quantum)
        # T-=Quantum
        # time.sleep(T * 0.1) # milliseconds
        # if self.memory_required == 0 : cprint(f'finished execution: {self.name}','red')
        # else : cprint(f'not finished: {self.name}, time left:{self.remaining_time * 0.1:.2f}s' ,'blue')
        pass

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
    
    def bulbe_sort(self): # implementazione SJF 
        L=len(self.n_process) - 1
        for y in range(L): #time O(n**2)
            for j in range((L) - y):
                if self.n_process[j]['Burst_Time'] > self.n_process[j + 1]['Burst_Time']: 
                    self.n_process[j] , self.n_process[j + 1] = self.n_process[j + 1], self.n_process[j] 
        print(self.n_process)
        return self.n_process
    
    def queue(self):
        queue=[]
        if self.maxSize == 0: return 'infinite queue'
        elif len(self.n_process) > self.maxSize:
            self.n_process=self.n_process[:self.maxSize] # fewer elements compared to maxSize
        return self.n_process  #preparation queue follow Algorithms ORR or SORR (the best)
        # if len(self.n_process) > self.maxSize: # fewer elements compared to maxSize
        #      self.n_process=self.n_process[:self.maxSize]
        # for i in range(len(self.n_process)):
        #     # start_time = datetime.now()
        #     # print(start_time)
        #     time.sleep(self.n_process[i]['arrival_time'])
        #     queue.append(self.n_process[i])
        #     print(queue)
        # return queue  #preparation queue follow Algorithms ORR or SORR (the best)

    def round_robin(self):
        complete_process=[]
        
        while self.n_process != []: # methods n queue
            time.sleep(self.Quantum)
            self.n_process[0]['remaining_time'] -= self.Quantum
            if self.n_process[0]['remaining_time'] <= 0: #rimozione processo dalla ueue
               self.n_process[0]['remaining_time']=0
               print(f"process finished:{colored(self.n_process[0]['name'],'red')}")
               complete_process.append(self.n_process[0])
               self.n_process.pop(0)
            else:
                print(f"not finished: {colored(self.n_process[0]['name'],'red')}   time left: {colored(self.n_process[0]['remaining_time'],'blue')}s ")
                self.n_process= self.n_process[1:] + [self.n_process[0]] # elemento aggiunto alla coda della queue

        return complete_process
    
    def __str__(self):
       return str(self.Q)

P=[process('ps1',256,5,0).__dict__,
   process('ps2',256,9,2).__dict__,
   process('ps3',256,1,2).__dict__,
   process('ps4',256,5,0).__dict__,
   process('ps5',256,5,0).__dict__,
   process('ps6',256,20,0).__dict__,
   process('ps7',256,17,0).__dict__,
   process('ps8',256,3,0).__dict__,
   process('ps9',256,8,0).__dict__,
   process('ps10',256,25,0).__dict__,
   process('ps11',256,3,0).__dict__,
   process('ps12',256,3,2).__dict__,]

# M=Memory(8192) # simulazione di 1 KB RAM 
# for x in P:
#     x.run(10)
#     M.allocate(x.memory_required)


S=scheduler(P,maxSize=4)
if SJF: S.bulbe_sort()
S.queue()
print(S.round_robin())
# Memory management in Python involves a private heap containing all Python objects and data structures.

