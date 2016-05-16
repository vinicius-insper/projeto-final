import tkinter as tk

class gui_cozinha :
 
    def __init__(self,window, ativos):
        self.ativos = ativos

        self.label1=tk.Label(window,width=49,height=8, text='Para Fazer', bg='red')
        self.label1.grid(row=0,column=0)
        
        self.label2=tk.Label(window,width=49,height=8, text='Fazendo', bg='yellow' )
        self.label2.grid(row=0,column=1)
        
        self.label3=tk.Label(window,width=49,height=8, text='Pronto', bg='green' )
        self.label3.grid(row=0,column=2)

        self.botao1=tk.Button(window,width=4,height=5)
        self.botao1.configure(command=lambda:self.criar_botao())
        self.botao1.grid(row = 0,column = 3 )
    
        self.variavelcolumn=0
        self.variavelrow=1
        self.pedido=0
    
    def criar_botao(self):
        #print(self.pedido)
        #B = str(self.pedido)
        B = tk.Button(window,width=40,height=5,text=str(self.pedido)) 
        B.grid(row = self.variavelrow , column = self.variavelcolumn)
        B.configure(command = lambda:self.para_fazer(self.pedido)) 
        self.variavelrow += 1
        self.pedido+=1

        self.ativos.append(B)
        print(self.ativos)

        
    
    def para_fazer(self, i):
        self.ativos[i].variavelcolumn+=1
        self.ativos[i].grid(row=self.ativos[i].variavelrow, column= self.ativos[i].variavelcolumn)
        if self.variavelcolumn >2:
            self.ativos[i].destroy()
            self.ativos[i].variavelcolumn=0
        
       
window=tk.Tk()
window.title ("Cozinha")
gui_cozinha(window, [])
window.mainloop()
