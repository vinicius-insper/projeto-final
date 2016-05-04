import tkinter as tk 


class inicio :
    
    def __init__ (self,master):
        
        
        self.frame = tk.Frame(master, width=500, height=500, bd=175)
        self.frame.pack()
        
        self.botaomapa = tk.Button(self.frame,text ='Mapa',height=8 ,width= 20 ,bd=20,padx=20)
        self.botaomapa.pack(side=tk.LEFT)
        
        self.botaocozinha = tk.Button(self.frame,text ='Cozinha',height=8 ,width=20 ,bd=20,padx=20)
        self.botaocozinha.pack(side=tk.RIGHT)
        

window=tk.Tk()
window.title ('Inicio')
inicio(window)
window.mainloop()

