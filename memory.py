
from termcolor import colored, cprint 
import time 

'''
Concorrenza e Sicurezza:
In un sistema operativo reale, la gestione dei processi deve essere thread-safe, in quanto più thread o processi potrebbero tentare di accedere agli stessi dati.
'''

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

Waiting time: Sum of time a process spent waiting in ready queue
'''

# class Kernel: #kernel
#     def __init__(self, sheduler):
#         self.memory= Memory(1024)
#         self.scheduler=sheduler
    
#     def run(self):
#         print(self.memory.allocate(200))
        

class Memory: #allocazione memoria
    def __init__(self,memory):
        self.memory= memory
        self.used_memory=0

    def allocate(self,memory):
        self.used_memory += memory
        if self.used_memory <= self.memory: cprint(f'memoria allocata {memory} memoria disponibile {self.memory - (self.used_memory)}', "cyan")
        else: raise Exception(f'memoria allocata {self.used_memory} supera {memory}')
        
    
    def free(self, memory):
        self.used_memory -= memory
        print(f'memoria liberata di {memory}')