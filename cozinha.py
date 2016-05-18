import time
import tkinter as tk

class gui_cozinha :
 
    def __init__(self):
        self.window=tk.Tk()
        self.window.title ("Cozinha")        
        
        self.ativos={}

        self.label1=tk.Label(self.window,width=49,height=8, text='Para Fazer', bg='red')
        self.label1.grid(row=0,column=0)
        
        self.label2=tk.Label(self.window,width=49,height=8, text='Fazendo', bg='yellow' )
        self.label2.grid(row=0,column=1)
        
        self.label3=tk.Label(self.window,width=49,height=8, text='Pronto', bg='green' )
        self.label3.grid(row=0,column=2)

        self.botao1=tk.Button(self.window,width=4,height=5)
        self.botao1.configure(command=lambda:self.criar_botao())
        self.botao1.grid(row = 0,column = 3 )
        
        self.variavelrow=1
        self.pedido=0
        
        self.window.mainloop()
    
    def criar_botao(self):        
        B = tk.Button(self.window,width=40,height=5,text=str(self.pedido)+'\n') 
        B.grid(row = self.variavelrow , column =0)
        B.configure(command = lambda:self.para_fazer(B,Bv)) 
        
#        self.fica_vermelho(B)

        Bv = tk.Button(self.window,width=5,height=3,text='cancela',bg='red') 
        Bv.grid(row = self.variavelrow , column =1)
        Bv.configure(command = lambda:self.cancela_pedido(Bv,B)) 
        
        self.variavelrow += 1
        self.pedido+=1

        self.ativos[B]=0 
#        time.sleep(10)
#        B.configure(bg='red')

        
    
    def para_fazer(self,B,Bv):
        self.ativos[B]+=1
        B.grid( column= self.ativos[B])
        Bv.destroy()
        if self.ativos[B] >2:
            B.destroy()
            
    def cancela_pedido(self,Bv,B):
        Bv.destroy()
        B.destroy()
        
#    def fica_vermelho(self,B):
#        t0=time.time()
#        while time.time() - t0 < 2:
#            print('ola')
#        B.configure(bg='red')
