import math
from termcolor import colored
'''
quando un processo viene creato viene creato nella RAM e ad ogni pagina viene data un fraim nella SSD (fino a quando la sua memoria non finisce) e all'interno di questi fraim c'è la pagina 
processo occupa 200bytes di memoria quindi neanche un KB di memoria verra allocata semplicemnete in una pagina, ma se supera la quantita di memoria
di una pagina allora il rimanente verra allocata li e se non occupa interamnete quella pagina allora quella pagina avrà dello spazio free (questo viene chiamato internal fragmentation)
perche le grandezze delle pagine sono fisse 

Memoria Virtuale: è uno spazio che si trova sul disco rigido o SSD e viene usata quando lo spazio nella RAM viene esaurito 
Paging: divide la memoria SSD e RAM in blocchi fissi chiamati FRAME in RAM e PAGINE nella SSD 
'''

class Memory: #allocazione memoria
    def __init__(self):
        self.Memoria_Virtuale= int(8e6)  # MB SSD page 
        self.Memoria_Fisica= int(4e6) # MB RAM frame 
        self.M_pages=int(4e3) #bits KB 
        self.page_table= None
        self.table_id=0

    def PT(self): # page table 
         self.page_table=[{'pages SSD':x, 'frame RAM': x if x < self.Memoria_Fisica / self.M_pages else None ,'NameP':None}  for x in range(int(self.Memoria_Virtuale / self.M_pages)) ]
         return self.page_table

    def allocate(self,memory,process):
        pages_need=math.ceil(memory / self.M_pages) #frame for process 
        for x in range(self.table_id, self.table_id + pages_need):
            if self.page_table[x]['frame RAM'] != None:self.page_table[x]['NameP'] =  process #allocate physical memory (frame) to process
            else: raise MemoryError('non abbastanza memoria')
        self.table_id += pages_need #sum for id table 
    
    def deallocate(self,process,memory):
        for x in self.page_table:
            if x['NameP'] == process: x['NameP'] = None
        return math.floor(memory / self.M_pages) # tot frame liberati
        

# virtual_address generato dalla cpu composto da Virtual page number (20 bits) and page offset (12 bits).

#  https://www2.cs.uregina.ca/~hamilton/courses/330/notes/memory/paging.html