from termcolor import colored, cprint 
import time

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
        self.Memoria_Virtuale= int(8e6)  # MB SSD phisical memory 
        self.Memoria_Fisica= int(4e6) # MB RAM logical memory 
        self.M_pages=int(4e3) #bits KB 
        self.page_table= None
        self.used_memory=0

    def allocate(self,memory):
        # in pages x dovrebbe esserci la rappresentazione di bits es 00000001 fino ad arrivare 11111111 
        # ogni pages ha vari address (offset) 
        self.page_table=[{'pages SSD':x, 'frame RAM': None}  for x in range(int(self.Memoria_Virtuale / self.M_pages)) ] #map of memory
        for x in range(self.Memoria_Fisica // self.M_pages):
            memory -= self.M_pages
            self.page_table[x]['frame RAM'] = x
            if memory <= 0: break

        print(self.page_table)
        # if self.used_memory <= self.memory: cprint(f'memoria allocata {memory} memoria disponibile {self.memory - (self.used_memory)}', "cyan")
        # else: raise Exception(f'memoria allocata {self.used_memory} supera {memory}')


M=Memory()
M.allocate(5e3)


# virtual_address generato dalla cpu composto da Virtual page number (20 bits) and page offset (12 bits).

'''
In a paging memory management system, the virtual address space is divided into fixed-size blocks called pages, which are mapped to physical memory frames. The virtual address consists of two parts: the page number and the offset within the page.
Calculating the Page Number and Offset
Given:
Virtual address space: 32 bits (4 GB)
Page size: 2^8 bytes (256 bytes)
Page size: 2^8 bytes = 256 bytes
Number of pages: 2^32 / 2^8 = 2^24 pages
Page number: 2^24 bits (24 bits)
Offset: 2^8 bits (8 bits)
To calculate the physical address:
Page number = virtual address / page size
Offset = virtual address % page size
For example, if the virtual address is 0x12345678:
Page number = 0x12345 (18 bits)
Offset = 0x78 (8 bits)
The page number is used to index the page table, which stores the mapping between virtual pages and physical frames. The offset is combined with the base address of the physical frame to obtain the final physical address.
Page Table Size
The size of the page table depends on the number of entries and the size of each entry.
Given:
Number of pages: 2^24
Entry size: 4 bytes (32 bits)
Page table size = Number of entries × Entry size
Page table size = 2^24 × 4 bytes = 2^24 × 2^2 bytes = 2^26 bytes = 64 MB
In summary, with a 32-bit virtual address space and 256-byte pages, the page number is 24 bits, the offset is 8 bits, and the page table size for a process with 2^24 pages using 4-byte entries is 64 MB

'''
#  https://www2.cs.uregina.ca/~hamilton/courses/330/notes/memory/paging.html

# Swapping: Sposta i processi tra memoria fisica e memoria secondaria (disco) per ottimizzare l'uso della memoria.
# Allocazione della Memoria: Gestisce come e dove vengono allocati i blocchi di memoria, per evitare la frammentazione e garantire l'efficienza.
# Context Switching: Gestisce il salvataggio e il ripristino dello stato dei processi quando il CPU scheduler cambia da un processo a un altro.