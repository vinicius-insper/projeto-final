import tkinter as tk 



class inicio :
    
    def __init__ (self,toplevel):
        #cria a interface do tkinter 
        self.frame = tk.Frame(toplevel, width=500, height=500, bd=175)
        self.frame.pack()
        
        #cria um botao para ser direcionado ao mapa
        self.botaomapa = tk.Button(self.frame,text ='Mapa',height=8 ,width= 20 ,bd=20,padx=20)
        self.botaomapa.pack(side=tk.LEFT)
        
        #cria uma botao para ser direcionado a cozinha 
        self.botaocozinha = tk.Button(self.frame,text ='Cozinha',height=8 ,width=20 ,bd=20,padx=20)
        self.botaocozinha.pack(side=tk.RIGHT)
        self.botaocozinha.configure(command = lambda:self.cozinha())
        
        
    def cozinha(self):
        import GUI_cozinha
        GUI_cozinha(window)
        window.mainloop()
            

        

window=tk.Tk()
window.title ('Inicio')
inicio(window)
window.mainloop()

