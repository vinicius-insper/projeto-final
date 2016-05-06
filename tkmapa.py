import tkinter as tk

class mapa:
    def __init__(self):
        self.mapa= tk.Tk()
        self.mapa.title('Mapa Restaurante')
        self.mapa.configure(bg='green')
        self.iniciar() 
        
    def iniciar(self):
        self.mesa1=tk.Button(self.mapa)
        self.mesa1.configure(command= lambda:self.comando1()) 
        self.mesa1.configure(text='mesa 1')
        self.mesa1.configure(width= 14, height= 6)
        self.mesa1.configure(bg='yellow')
        self.mesa1.grid(row=0,column=0)
        
        self.mesa2=tk.Button(self.mapa)
        self.mesa2.configure(command= lambda:self.comando1())
        self.mesa2.configure(text='mesa 2')
        self.mesa2.configure(width= 14, height= 6)
        self.mesa2.configure(bg='yellow')
        self.mesa2.grid(row=2,column=0)
        
        self.mesa3=tk.Button(self.mapa)
        self.mesa3.configure(command= lambda:self.comando1())
        self.mesa3.configure(text='mesa 3')
        self.mesa3.configure(width= 14, height= 6)
        self.mesa3.configure(bg='yellow')
        self.mesa3.grid(row=4,column=0)
        
        self.mesa4=tk.Button(self.mapa)
        self.mesa4.configure(command= lambda:self.comando1())
        self.mesa4.configure(text='mesa 4')
        self.mesa4.configure(width= 14, height= 6)
        self.mesa4.configure(bg='yellow')
        self.mesa4.grid(row=0,column=2)
        
        self.mesa5=tk.Button(self.mapa)
        self.mesa5.configure(command= lambda:self.comando1())
        self.mesa5.configure(text='mesa 5')
        self.mesa5.configure(width= 14, height= 6)
        self.mesa5.configure(bg='yellow')
        self.mesa5.grid(row=2,column=2)
        
        self.mesa6=tk.Button(self.mapa)
        self.mesa6.configure(command= lambda:self.comando2())
        self.mesa6.configure(text='mesa 6')
        self.mesa6.configure(width= 21, height= 6)
        self.mesa6.configure(bg='yellow')
        self.mesa6.grid(row=4,column=2)
        
        self.mesa7=tk.Button(self.mapa)
        self.mesa7.configure(command= lambda:self.comando2())
        self.mesa7.configure(text='mesa 7')
        self.mesa7.configure(width= 21, height= 6)
        self.mesa7.configure(bg='yellow')
        self.mesa7.grid(row=0,column=4)
        
        self.mesa8=tk.Button(self.mapa)
        self.mesa8.configure(command= lambda:self.comando2())
        self.mesa8.configure(text='mesa 8')
        self.mesa8.configure(width= 21, height= 6)
        self.mesa8.configure(bg='yellow')
        self.mesa8.grid(row=2,column=4)
        
        self.mesa9=tk.Button(self.mapa)
        self.mesa9.configure(command= lambda:self.comando2())
        self.mesa9.configure(text='mesa 9')
        self.mesa9.configure(width= 21, height= 6)
        self.mesa9.configure(bg='yellow')
        self.mesa9.grid(row=4,column=4)
        
        self.label1=tk.Label(self.mapa)
        self.label1.configure(height=3)
        self.label1.grid(row=1)
        
        self.label2=tk.Label(self.mapa)
        self.label2.configure(height=3)
        self.label2.grid(row=3)
        
        self.label3=tk.Label(self.mapa)
        self.label3.configure(width=7)
        self.label3.grid(column=1)
        
        self.label4=tk.Label(self.mapa)
        self.label4.configure(width=7)
        self.label4.grid(column=3)
        
        self.mapa.mainloop()
        
    def comando1(self):
        self.mesa=tk.Tk()
        self.mesa.title('mesa')
        self.mesa.configure(bg='green')
        
        self.cliente1=tk.Button(self.mesa)
        self.cliente1.configure(command=lambda:self.teclado1())
        self.cliente1.configure(text='cadeira 1')
        self.cliente1.configure(width=14,height=6)
        self.cliente1.configure(bg='yellow')
        self.cliente1.grid(row=0, column=0)
        
        self.cliente2=tk.Button(self.mesa)
        self.cliente2.configure(command=lambda:self.teclado1())
        self.cliente2.configure(text='cadeira 2')
        self.cliente2.configure(width=14,height=6)
        self.cliente2.configure(bg='yellow')
        self.cliente2.grid(row=0,column=1)
        
        self.cliente3=tk.Button(self.mesa)
        self.cliente3.configure(command=lambda:self.teclado1())        
        self.cliente3.configure(text='cadeira 3')
        self.cliente3.configure(width=14,height=6)
        self.cliente3.configure(bg='yellow')
        self.cliente3.grid(row=1,column=0)
        
        self.cliente4=tk.Button(self.mesa)
        self.cliente4.configure(command=lambda:self.teclado1())
        self.cliente4.configure(text='cadeira 4')
        self.cliente4.configure(width=14,height=6)
        self.cliente4.configure(bg='yellow')
        self.cliente4.grid(row=1,column=1)
        
        self.fecharmesa=tk.Button(self.mesa)
        self.fecharmesa.configure(text='fechar conta mesa')
        self.fecharmesa.configure(width=20,height=6)
        self.fecharmesa.configure(bg='blue')
        self.fecharmesa.grid(row=2,column=0)
        
        self.fecharind=tk.Button(self.mesa)
        self.fecharind.configure(text='fechar conta por pessoa')
        self.fecharind.configure(width=20,height=6)
        self.fecharind.configure(bg='red')
        self.fecharind.grid(row=2,column=1)
        
        self.mesa.mainloop()
        
    def comando2(self):
        self.mesa=tk.Tk()
        self.mesa.title('mesa')
        self.mesa.configure(bg='green')
        
        self.cliente1=tk.Button(self.mesa)
        self.cliente1.configure(command=lambda:self.teclado1())
        self.cliente1.configure(text='cadeira 1')
        self.cliente1.configure(width=14,height=6)
        self.cliente1.configure(bg='yellow')
        self.cliente1.grid(row=0, column=0)
        
        self.cliente2=tk.Button(self.mesa)
        self.cliente2.configure(command=lambda:self.teclado1())
        self.cliente2.configure(text='cadeira 2')
        self.cliente2.configure(width=14,height=6)
        self.cliente2.configure(bg='yellow')
        self.cliente2.grid(row=0,column=1)
        
        self.cliente3=tk.Button(self.mesa)
        self.cliente3.configure(command=lambda:self.teclado1())
        self.cliente3.configure(text='cadeira 3')
        self.cliente3.configure(width=14,height=6)
        self.cliente3.configure(bg='yellow')
        self.cliente3.grid(row=1,column=0)
        
        self.cliente4=tk.Button(self.mesa)
        self.cliente4.configure(command=lambda:self.teclado1())
        self.cliente4.configure(text='cadeira 4')
        self.cliente4.configure(width=14,height=6)
        self.cliente4.configure(bg='yellow')
        self.cliente4.grid(row=1,column=1)
        
        self.cliente5=tk.Button(self.mesa)
        self.cliente5.configure(command=lambda:self.teclado1())
        self.cliente5.configure(text='cadeira 5')
        self.cliente5.configure(width=14,height=6)
        self.cliente5.configure(bg='yellow')
        self.cliente5.grid(row=2,column=0)
        
        self.cliente6=tk.Button(self.mesa)
        self.cliente6.configure(command=lambda:self.teclado1())
        self.cliente6.configure(text='cadeira 6')
        self.cliente6.configure(width=14,height=6)
        self.cliente6.configure(bg='yellow')
        self.cliente6.grid(row=2,column=1)
        
        self.fecharmesa=tk.Button(self.mesa)
        self.fecharmesa.configure(text='fechar conta mesa')
        self.fecharmesa.configure(width=20,height=6)
        self.fecharmesa.configure(bg='blue')
        self.fecharmesa.grid(row=3,column=0)
        
        self.fecharind=tk.Button(self.mesa)
        self.fecharind.configure(text='fechar conta por pessoa')
        self.fecharind.configure(width=20,height=6)
        self.fecharind.configure(bg='red')
        self.fecharind.grid(row=3,column=1)
        
        self.mesa.mainloop()
        
        
    def teclado1(self):
        self.teclado=tk.Tk()
        self.teclado.title('teclado')
        
        self.codigo=tk.Label(self.teclado)
        self.codigo.grid(row=0)
        
        self.b1=tk.Button(self.teclado)
        self.b1.configure(text='1')
        self.b1.configure(width=14,height=6)
        self.b1.grid(row=1,column=0)
        
        self.b2=tk.Button(self.teclado)
        self.b2.configure(text='2')
        self.b2.configure(width=14,height=6)
        self.b2.grid(row=1,column=1)
        
        self.b3=tk.Button(self.teclado)
        self.b3.configure(text='3')
        self.b3.configure(width=14,height=6)
        self.b3.grid(row=1,column=2)
        
        self.b4=tk.Button(self.teclado)
        self.b4.configure(text='4')
        self.b4.configure(width=14,height=6)
        self.b4.grid(row=2,column=0)
        
        self.b5=tk.Button(self.teclado)
        self.b5.configure(text='5')
        self.b5.configure(width=14,height=6)
        self.b5.grid(row=2,column=1)
        
        self.b6=tk.Button(self.teclado)
        self.b6.configure(text='6')
        self.b6.configure(width=14,height=6)
        self.b6.grid(row=2,column=2)
        
        self.b7=tk.Button(self.teclado)
        self.b7.configure(text='7')
        self.b7.configure(width=14,height=6)
        self.b7.grid(row=3,column=0)
        
        self.b8=tk.Button(self.teclado)
        self.b8.configure(text='8')
        self.b8.configure(width=14,height=6)
        self.b8.grid(row=3,column=1)
        
        self.b9=tk.Button(self.teclado)
        self.b9.configure(text='9')
        self.b9.configure(width=14,height=6)
        self.b9.grid(row=3,column=2)
        
        self.b0=tk.Button(self.teclado)
        self.b0.configure(text='0')
        self.b0.configure(width=14,height=6)
        self.b0.grid(row=4,column=1)
        
        self.bok=tk.Button(self.teclado)
        self.bok.configure(text='OK')
        self.bok.configure(width=14,height=6)
        self.bok.configure(bg='green')
        self.bok.grid(row=4,column=0)
        
        self.bcancela=tk.Button(self.teclado)
        self.bcancela.configure(text='CANCELA')
        self.bcancela.configure(width=14,height=6)
        self.bcancela.configure(bg='red')
        self.bcancela.grid(row=4,column=2)
                
mapa=mapa()


















