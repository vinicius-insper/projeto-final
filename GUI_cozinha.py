import tkinter as tk

class gui_cozinha :
 
    def __init__(self,window):   
       
        self.label1=tk.Label(window,width=49,height=8, text='Para Fazer', bg='red')
        self.label1.grid(row=0,column=0)
        
        self.label2=tk.Label(window,width=49,height=8, text='Fazendo', bg='yellow' )
        self.label2.grid(row=0,column=1)
        
        self.label3=tk.Label(window,width=49,height=8, text='Pronto', bg='green' )
        self.label3.grid(row=0,column=2)
    
        self.botao=tk.Button(window,width=40,height=5)
        self.botao.grid(row = 1,column= 0)
        self.botao.configure(command = self.botao)

       
window=tk.Tk()
window.title ("Cozinha")
gui_cozinha(window)
window.mainloop()

