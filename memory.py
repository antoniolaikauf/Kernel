from termcolor import colored, cprint 
import time 


# class Memory:
#     def __init__(self):
#         self.Memoria_Virtuale = 32 # KB
#         self.Memoria_Fisica = 16 # KB
#         self.M_pages = 4 # KB per pagina
#         self.page_table = []
#         self.free_frames = list(range(self.Memoria_Fisica // self.M_pages))

#     def allocate(self, memory):
#         num_pages = (memory + self.M_pages - 1) // self.M_pages  # Round up division
#         total_pages = int(self.Memoria_Virtuale / self.M_pages)
        
#         # Initialize page table with None values
#         self.page_table = [{'pages SSD': i, 'frame RAM': None} for i in range(total_pages)]
        
#         # Allocate frames to pages
#         for page in range(num_pages):
#             if self.free_frames:
#                 frame = self.free_frames.pop(0)
#                 self.page_table[page]['frame RAM'] = frame
#             else:
#                 print("No more frames available.")
#                 break
        
#         print(self.page_table)

# # Test the Memory class
# M = Memory()
# M.allocate(20)  # Allocate 8 KB of memory

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
'''
quando un processo viene creato viene creato nella RAM e ad ogni pagina viene data un fraim nella SSD (fino a quando la sua memoria non finisce) e all'interno di questi fraim c'è la pagina 
processo occupa 200bytes di memoria quindi neanche un KB di memoria verra allocata semplicemnete in una pagina, ma se supera la quantita di memoria
di una pagina allora il rimanente verra allocata li e se non occupa interamnete quella pagina allora quella pagina avrà dello spazio free (questo viene chiamato internal fragmentation)
perche le grandezze delle pagine sono fisse 

Memoria Virtuale: è uno spazio che si trova sul disco rigido o SSD e viene usata quando lo spazio nella RAM viene esaurito 
Paging: divide la memoria SSD e RAM in blocchi fissi chiamati FRAME in RAM e PAGINE nella SSD 
Quando un processo accede a un indirizzo di memoria virtuale, il sistema operativo traduce questo indirizzo in un indirizzo fisico utilizzando la tabella delle pagine.

'''

class Memory: #allocazione memoria
    def __init__(self):
        self.Memoria_Virtuale= 32 # KB SSD phisical memory 
        self.Memoria_Fisica= 16 # KB RAM logical memory 
        self.M_pages=4
        self.page_table= None
        self.used_memory=0

    def allocate(self,memory):
        # in pages x dovrebbe esserci la rappresentazione di bits es 00000001 fino ad arrivare 11111111 
        # ogni pages ha vari address  
        self.page_table=[{'pages SSD':x, 'frame RAM': None}  for x in range(int(self.Memoria_Virtuale / self.M_pages)) ] #map of memory
        for x in range(self.Memoria_Fisica // self.M_pages):
            memory -= self.M_pages
            if memory >= 0 : self.page_table[x]['frame RAM'] = x
            else :break

        print(self.page_table)
        # self.used_memory += memory
        # if self.used_memory <= self.memory: cprint(f'memoria allocata {memory} memoria disponibile {self.memory - (self.used_memory)}', "cyan")
        # else: raise Exception(f'memoria allocata {self.used_memory} supera {memory}')


M=Memory()
M.allocate(20)

# Swapping: Sposta i processi tra memoria fisica e memoria secondaria (disco) per ottimizzare l'uso della memoria.
# Allocazione della Memoria: Gestisce come e dove vengono allocati i blocchi di memoria, per evitare la frammentazione e garantire l'efficienza.
# Context Switching: Gestisce il salvataggio e il ripristino dello stato dei processi quando il CPU scheduler cambia da un processo a un altro.