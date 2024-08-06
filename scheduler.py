import time 
import sys
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
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
    
    '''
    Example: name, arrival time, burst time 
              ps1    0              5
              ps2    1              4
              ps3    2              2
    With a quantum of 2, 
    the start queue is formed by ps1 and ps2.
    In the first cycle, ps1 executes and ps3 arrives.
    In the second cycle, ps2 executes.
    In the third cycle, ps3 executes and exits the queue.
    In the fourth cycle, ps1 executes.
    In the fifth cycle, ps2 executes and exits the queue.
    In the sixth cycle, ps1 executes and exits the queue.
    So the queue must always check if a process is arriving, but I don't know how to do this in Python because `time.sleep` blocks the code.
    '''

    '''
    In JSF, there is a queue used to hold the processes, but they are not executed in order. Instead, they are scheduled based on a priority, 
    which can be the burst time. In JSF, the process with the shortest burst time starts first. If a process with a shorter burst time arrives 
    while another process is already executing, the current process can be stopped to allow the new process to execute.
    '''
    

'''
 Quantum/time interval is the time the the scheduler give to all process 
'''

class round_robin(scheduler):
    def __init__(self, n_process, maxSize=2, Quantum=5):
        super().__init__(n_process, maxSize)
        self.Quantum=Quantum
        self.G=[] #G =graph
        self.complete_process=[]
        self.Completion_time = 0 # how much time you need for every process to be compleated 
        self.T_process={}
            
    def run(self):
        while self.n_process != []:
            # Completion_time 
            if self.n_process[0]['remaining_time'] < self.Quantum: self.Completion_time+=self.n_process[0]['remaining_time']
            else: self.Completion_time+=self.Quantum
            self.T_process[self.n_process[0]['name']] = {'Completion_time':self.Completion_time}

            self.G.append({'name':self.n_process[0]['name'], 'time':self.n_process[0]['remaining_time']}) # for graph 

            time.sleep(self.Quantum)
            # burst time - quantum 
            self.n_process[0]['remaining_time'] -= self.Quantum
            if self.n_process[0]['remaining_time'] <= 0: #remove process from queue 
               self.n_process[0]['remaining_time']=0
               print(f"process finished:{colored(self.n_process[0]['name'],'red')}")
               self.complete_process.append(self.n_process[0])
               self.n_process.pop(0)
            else: # put porcces at the end of the queue
                print(f"not finished: {colored(self.n_process[0]['name'],'red')}   time left: {colored(self.n_process[0]['remaining_time'],'blue')}s ")
                self.n_process= self.n_process[1:] + [self.n_process[0]]

        for T in self.complete_process:  # formula for Time_Turnaround and waiting time 
            self.T_process[T['name']]['Time_Turnaround'] = self.T_process[T['name']]['Completion_time'] -  T['arrival_time'] #this is the time a when a process is completed when enter the queue formula Time_Turnaround = Completion_time - arrival_time
            self.T_process[T['name']]['Waitng_time'] = self.T_process[T['name']]['Time_Turnaround'] - T['Burst_Time'] #This is the time a process spends waiting in the queue # formula Waitng_time = Time_Turnaround - Burst_Time
        
        # average time of the scheduler 
        Average_Wait_time=sum(self.T_process[x]['Waitng_time'] for x in self.T_process) / len(self.T_process)
        print(f"Average Waiting Time: {colored('{:.2f}'.format(Average_Wait_time),'cyan')}")

        return self.complete_process
    
    def graph(self): #Gantt chart
        x=[j['name'] for j in self.G]
        y = [i['time'] for i in self.G]
        fig,ax=plt.subplots()
        ax.plot(x, y, 'ro')
        plt.gca().yaxis.set_major_formatter(mticker.FormatStrFormatter('%.1f s'))

        plt.text(0.99, 1.05, 'From top to bottm', horizontalalignment='right', verticalalignment='top', transform = ax.transAxes, backgroundcolor='0.75')
        plt.text(0.99, 1.10, 'Quantum=' + str(self.Quantum), horizontalalignment='right', verticalalignment='top', transform = ax.transAxes, backgroundcolor='0.75')
        plt.xlabel('process')
        plt.ylabel('Run time - Quantum')
        plt.show()

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

    def graph(self): # draw graph with burst time 
        run_time=[x['Burst_Time'] for x in self.n_process]
        n_process=[x['name'] for x in self.n_process]
        fig, ax = plt.subplots() 
        ax.bar(n_process, run_time)
        plt.gca().yaxis.set_major_formatter(mticker.FormatStrFormatter('%.1f s'))
        plt.xlabel('Process')
        plt.ylabel('Burst Time')
        plt.show()

# name, memory, burst time, arrival time 
P=[process('ps1',1000000,5,1).__dict__,
   process('ps2',1000000,4,2).__dict__,
   process('ps3',1000000,2,3).__dict__,
   process('ps4',1000000,6,4).__dict__,]

'''
   process('ps5',1000000,5,6).__dict__,
   process('ps6',1000000,20,8).__dict__,
   process('ps7',1000000,17,9).__dict__,
   process('ps8',1000000,3,10).__dict__,
   process('ps9',1000000,8,11).__dict__,
   process('ps10',1000000,25,13).__dict__,
   process('ps11',1000000,3,14).__dict__,
   process('ps12',1000000,3,16).__dict__,

'''

maxSize=20
S=scheduler(P,maxSize)
Q=S.queue()
if sjf:
    SJF=Shortest_Job_First(Q,maxSize)
    print(SJF.run())
    SJF.graph()
elif rr:
    M=Memory() # memory
    M.PT()
    for x in P:
        M.allocate(x['memory_required'],x['name'])
    print(M.page_table)
    RR= round_robin(Q, maxSize, Quantum=6)
    print(RR.run()) # algoritmo
    # RR.graph() #grafico 