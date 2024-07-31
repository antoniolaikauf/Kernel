
from termcolor import colored, cprint 
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


FIFO (First In, First Out)
In un sistema FIFO, i processi vengono eseguiti nell'ordine in cui arrivano. Questo approccio è semplice e garantisce che ogni processo venga eseguito in modo equo. Tuttavia, presenta alcune limitazioni:
Starvation: Processi a lungo termine possono rimanere in attesa se ci sono sempre nuovi processi che arrivano.
Non ottimale: Non tiene conto delle esigenze specifiche dei processi, come la loro urgenza o importanza.
Introduzione della Priorità
Nei sistemi di scheduling con priorità, i processi non vengono semplicemente gestiti in ordine di arrivo. Ecco come funziona:
Coda di Priorità: Invece di una semplice coda FIFO, i processi possono essere inseriti in una coda di priorità. In questa coda, i processi con priorità più alta vengono eseguiti prima di quelli con priorità più bassa, indipendentemente dall'ordine di arrivo.
Preemption: Se un processo di alta priorità arriva mentre un processo di bassa priorità è in esecuzione, il sistema può interrompere (preempt) il processo in esecuzione e dare la precedenza a quello di alta priorità.
Sistemi Misti: Alcuni sistemi utilizzano una combinazione di FIFO e priorità. Ad esempio, possono utilizzare FIFO per i processi con la stessa priorità, mentre i processi con priorità diverse vengono gestiti in base alla loro urgenza.

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