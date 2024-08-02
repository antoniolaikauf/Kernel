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
rr=False
if len(sys.argv) > 2: raise Exception('add more than two parapeters')
if sys.argv[1].upper() == 'SJF': sjf=True
elif sys.argv[1].upper() == 'RR': rr= True
class process:
    def __init__(self, name, memory_required, Burst_Time, arrival_time): 
        self.name=name
        self.memory_required=memory_required
        self.Burst_Time=Burst_Time
        self.remaining_time=Burst_Time
        self.arrival_time=arrival_time
        self.waiting_time=0

class scheduler: # gestione processi
    def __init__(self, n_process, maxSize=2):
        self.n_process= n_process
        self.maxSize=maxSize
        self.Q=[]
    
    #TODO provare a sistemare questo se si riesce 
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
    

'''
 Quantum/time interval is the time the the scheduler give to all process 
'''
class round_robin(scheduler):
    def __init__(self, n_process, maxSize=2, Quantum=5):
        super().__init__(n_process, maxSize)
        self.Quantum=Quantum
    
    def run(self):
        complete_process=[]
        
        while self.n_process != []:
            time.sleep(self.Quantum)
            self.n_process[0]['remaining_time'] -= self.Quantum
            if self.n_process[0]['remaining_time'] <= 0: #remove process from queue 
               self.n_process[0]['remaining_time']=0
               print(f"process finished:{colored(self.n_process[0]['name'],'red')}")
               complete_process.append(self.n_process[0])
               self.n_process.pop(0)
            else: # put porcces at the end of the queue
                print(f"not finished: {colored(self.n_process[0]['name'],'red')}   time left: {colored(self.n_process[0]['remaining_time'],'blue')}s ")
                self.n_process= self.n_process[1:] + [self.n_process[0]] 

        return complete_process

'''
Shortest Job First chi ha il Burst_Time piu basso ha una priorità più alta 
'''
class Shortest_Job_First(scheduler):
    def __init__(self, n_process, maxSize=2):
        super().__init__(n_process, maxSize)
    
    def run(self): 
        L=len(self.n_process) - 1 
        for y in range (L): #sort array
            for j in range(L - y):
                if self.n_process[j]['Burst_Time'] > self.n_process[j + 1]['Burst_Time']:
                    self.n_process[j], self.n_process[j + 1] = self.n_process[j + 1] , self.n_process[j]

        for x in self.n_process: # processes performed 
            time.sleep(x['Burst_Time'])
            print(f"process finished:{colored(x['name'],'red')}")

    def graph(self): #draw graph with burst time 
        run_time=[x['Burst_Time'] for x in self.n_process]
        n_process=[x['name'] for x in self.n_process]
        fig, ax = plt.subplots() 
        ax.bar(n_process, run_time)
        plt.gca().yaxis.set_major_formatter(mticker.FormatStrFormatter('%.1f s'))
        plt.xlabel('Process')
        plt.ylabel('Burst Time')
        plt.show()


P=[process('ps1',256,1,0).__dict__,
   process('ps2',256,1,2).__dict__,
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

maxSize=5
S=scheduler(P,maxSize)
Q=S.queue()
if sjf:
    SJF=Shortest_Job_First(Q,maxSize)
    print(SJF.run())
    SJF.graph()
elif rr:
    RR= round_robin(Q, maxSize, Quantum=6)
    print(RR.run())

# Memory management in Python involves a private heap containing all Python objects and data structures.

