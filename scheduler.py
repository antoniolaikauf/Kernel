import time 
import sys
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from datetime import datetime
from termcolor import colored, cprint 
from memory import Memory

'''
Burst_Time would be the time that the proccess need to be executes call BURST TIME
'''
sjf=False
if len(sys.argv) > 2: raise Exception('add more than two parapeters')
if len(sys.argv) == 2: 
  sjf=True
class process:
    def __init__(self, name, memory_required, Burst_Time, arrival_time): 
        self.name=name
        self.memory_required=memory_required
        self.Burst_Time=Burst_Time
        self.remaining_time=Burst_Time
        self.arrival_time=arrival_time
        self.waiting_time=0
        
    def run(self):
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
    def __init__(self, n_process, maxSize=2):
        self.n_process= n_process
        self.maxSize=maxSize
        self.Q=[]
    
    def queue(self):
        if self.maxSize == 0: return 'infinite queue'
        elif len(self.n_process) > self.maxSize:
            self.n_process=self.n_process[:self.maxSize] # fewer elements compared to maxSize
        return self.n_process  #preparation queue follow Algorithms ORR or SORR (the best)
        # queue=[]
        # if len(self.n_process) > self.maxSize: # fewer elements compared to maxSize
        #      self.n_process=self.n_process[:self.maxSize]
        # for i in range(len(self.n_process)):
        #     # start_time = datetime.now()
        #     # print(start_time)
        #     time.sleep(self.n_process[i]['arrival_time'])
        #     queue.append(self.n_process[i])
        #     print(queue)
        # return queue  #preparation queue follow Algorithms ORR or SORR (the best)
    
    # def __str__(self):
    #    return str(self.Q)


class round_robin(scheduler):
    def __init__(self, n_process, maxSize=2, Quantum=5):
        super().__init__(n_process, maxSize)
        self.Quantum=Quantum
    
    def run(self):
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

class Shortest_Job_First(scheduler):
    def __init__(self, n_process, maxSize=2):
        super().__init__(n_process, maxSize)
    
    def run(self):
        L=len(self.n_process) - 1 
        for y in range (L):
            for j in range(L - y):
                if self.n_process[j]['Burst_Time'] > self.n_process[j + 1]['Burst_Time']:
                    self.n_process[j], self.n_process[j + 1] = self.n_process[j + 1] , self.n_process[j]

        for x in self.n_process:
            time.sleep(x['Burst_Time'])
            print(f"process finished:{colored(x['name'],'red')}")

    def graph(self):
        run_time=[x['Burst_Time'] for x in self.n_process]
        n_process=[x['name'] for x in self.n_process]
        fig, ax = plt.subplots() 
        ax.bar(n_process, run_time)
        plt.gca().yaxis.set_major_formatter(mticker.FormatStrFormatter('%.1f s'))
        plt.xlabel('Process')
        plt.ylabel('Burst Time')
        plt.show()


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

maxSize=20
S=scheduler(P,maxSize)
Q=S.queue()

RR= round_robin(Q, maxSize, Quantum=6)
SJF=Shortest_Job_First(Q,maxSize)

# print(SJF.run())
SJF.graph()
# print(RR.run())


# if sjf: S.SJF()
# print(S.round_robin())
# Memory management in Python involves a private heap containing all Python objects and data structures.

