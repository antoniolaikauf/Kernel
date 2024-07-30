'''
Gestione dei Processi:
Un vero scheduler di kernel deve gestire varie operazioni sui processi, come creazione, terminazione, sospensione, e ripresa.

La priorità varia da -20 (priorità più alta) a +19 (priorità più bassa). Il valore di default è 10
Un processo in attesa da più tempo viene favorito rispetto ad un processo che attende da meno tempo. A parità di attesa, un processo a priorità più alta viene favorito rispetto ad un processo a priorità più bassa.
A tal scopo, ad ogni processo è associato un contatore, inizializzato al valore della priorità statica.


Priorità e Preemption:
I moderni sistemi operativi spesso usano la priorità per determinare l'ordine di esecuzione dei processi e supportano la preemption, dove i processi possono essere interrotti per passare ad altri con priorità più alta.

Concorrenza e Sicurezza:
In un sistema operativo reale, la gestione dei processi deve essere thread-safe, in quanto più thread o processi potrebbero tentare di accedere agli stessi dati.

Tempo di Esecuzione e Scheduling Algorithms:
Algoritmi di scheduling più avanzati (Round-Robin, Shortest Job Next, ecc.) considerano vari parametri come il tempo di esecuzione, il tempo di arrivo, e la durata per determinare l'ordine dei processi.
'''

import time 

#i processori devono avere dei tempo in modo tale se non è completatto si interrompe il processo
'''
For example, if the time slot is 100 milliseconds, and job1 takes a total time of 250 ms to complete, the round-robin scheduler will suspend the job after 100 ms and give other jobs their time on the CPU.
Once the other jobs have had their equal share (100 ms each), job1 will get another allocation of CPU time and the cycle will repeat
Job1 = Total time to complete 250 ms (quantum 100 ms).
quantum è il tempo condiviso tra tutti i processi I processi sono mantenuti in una coda circolare.
Questo significa che quando un processo termina il suo quantum e non ha finito di eseguire, viene rimesso in fondo alla coda, permettendo al prossimo processo in fila di utilizzare la CPU.
First allocation = 100 ms.
Second allocation = 100 ms.
Third allocation = 100 ms but job1 self-terminates after 50 ms.
Total CPU time of job1 = 250 ms
'''

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