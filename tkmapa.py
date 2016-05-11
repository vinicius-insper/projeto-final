import tkinter as tk 
from Pedidos import Pedido
from firebase import firebase

class Mapa:
    def __init__(self):
        self.string=''
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
        self.mesa2.configure(command= lambda:self.comando2())
        self.mesa2.configure(text='mesa 2')
        self.mesa2.configure(width= 14, height= 6)
        self.mesa2.configure(bg='yellow')
        self.mesa2.grid(row=2,column=0)
        
        self.mesa3=tk.Button(self.mapa)
        self.mesa3.configure(command= lambda:self.comando3())
        self.mesa3.configure(text='mesa 3')
        self.mesa3.configure(width= 14, height= 6)
        self.mesa3.configure(bg='yellow')
        self.mesa3.grid(row=4,column=0)
        
        self.mesa4=tk.Button(self.mapa)
        self.mesa4.configure(command= lambda:self.comando4())
        self.mesa4.configure(text='mesa 4')
        self.mesa4.configure(width= 14, height= 6)
        self.mesa4.configure(bg='yellow')
        self.mesa4.grid(row=0,column=2)
        
        self.mesa5=tk.Button(self.mapa)
        self.mesa5.configure(command= lambda:self.comando5())
        self.mesa5.configure(text='mesa 5')
        self.mesa5.configure(width= 14, height= 6)
        self.mesa5.configure(bg='yellow')
        self.mesa5.grid(row=2,column=2)
        
        self.mesa6=tk.Button(self.mapa)
        self.mesa6.configure(command= lambda:self.comando6())
        self.mesa6.configure(text='mesa 6')
        self.mesa6.configure(width= 21, height= 6)
        self.mesa6.configure(bg='yellow')
        self.mesa6.grid(row=4,column=2)
        
        self.mesa7=tk.Button(self.mapa)
        self.mesa7.configure(command= lambda:self.comando7())
        self.mesa7.configure(text='mesa 7')
        self.mesa7.configure(width= 21, height= 6)
        self.mesa7.configure(bg='yellow')
        self.mesa7.grid(row=0,column=4)
        
        self.mesa8=tk.Button(self.mapa)
        self.mesa8.configure(command= lambda:self.comando8())
        self.mesa8.configure(text='mesa 8')
        self.mesa8.configure(width= 21, height= 6)
        self.mesa8.configure(bg='yellow')
        self.mesa8.grid(row=2,column=4)
        
        self.mesa9=tk.Button(self.mapa)
        self.mesa9.configure(command= lambda:self.comando9())
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
        
    def comando3(self):
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
        
    def comando4(self):
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
        
    def comando5(self):
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
        
    def comando6(self):
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
        
    def comando7(self):
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
        
    def comando8(self):
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
        
    def comando9(self):
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
        self.b1.configure(command=lambda:self.botao1())
        self.b1.configure(text='1')
        self.b1.configure(width=14,height=6)
        self.b1.grid(row=1,column=0)
        
        self.b2=tk.Button(self.teclado)
        self.b2.configure(command=lambda:self.botao2())
        self.b2.configure(text='2')
        self.b2.configure(width=14,height=6)
        self.b2.grid(row=1,column=1)
        
        self.b3=tk.Button(self.teclado)
        self.b3.configure(command=lambda:self.botao3())        
        self.b3.configure(text='3')
        self.b3.configure(width=14,height=6)
        self.b3.grid(row=1,column=2)
        
        self.b4=tk.Button(self.teclado)
        self.b4.configure(command=lambda:self.botao4())
        self.b4.configure(text='4')
        self.b4.configure(width=14,height=6)
        self.b4.grid(row=2,column=0)
        
        self.b5=tk.Button(self.teclado)
        self.b5.configure(command=lambda:self.botao5())
        self.b5.configure(text='5')
        self.b5.configure(width=14,height=6)
        self.b5.grid(row=2,column=1)
        
        self.b6=tk.Button(self.teclado)
        self.b6.configure(command=lambda:self.botao6())
        self.b6.configure(text='6')
        self.b6.configure(width=14,height=6)
        self.b6.grid(row=2,column=2)
        
        self.b7=tk.Button(self.teclado)
        self.b7.configure(command=lambda:self.botao7())
        self.b7.configure(text='7')
        self.b7.configure(width=14,height=6)
        self.b7.grid(row=3,column=0)
        
        self.b8=tk.Button(self.teclado)
        self.b8.configure(command=lambda:self.botao8())
        self.b8.configure(text='8')
        self.b8.configure(width=14,height=6)
        self.b8.grid(row=3,column=1)
        
        self.b9=tk.Button(self.teclado)
        self.b9.configure(command=lambda:self.botao9())
        self.b9.configure(text='9')
        self.b9.configure(width=14,height=6)
        self.b9.grid(row=3,column=2)
        
        self.b0=tk.Button(self.teclado)
        self.b0.configure(command=lambda:self.botao0())
        self.b0.configure(text='0')
        self.b0.configure(width=14,height=6)
        self.b0.grid(row=4,column=1)
        
        self.bok=tk.Button(self.teclado)
        self.bok.configure(command=lambda:self.ok())
        self.bok.configure(text='OK')
        self.bok.configure(width=14,height=6)
        self.bok.configure(bg='green')
        self.bok.grid(row=4,column=0)
        
        self.bcancela=tk.Button(self.teclado)
        self.bcancela.configure(command=lambda:self.cancela())
        self.bcancela.configure(text='CANCELA')
        self.bcancela.configure(width=14,height=6)
        self.bcancela.configure(bg='red')
        self.bcancela.grid(row=4,column=2)
        
        self.string=''
        
        self.teclado.mainloop()
        
    def botao1(self):
        self.string=self.string+'1'
        self.codigo.configure(text=self.string) 
        
    def botao2(self):
        self.string=self.string+'2'
        self.codigo.configure(text=self.string)
        
    def botao3(self):
        self.string=self.string+'3'
        self.codigo.configure(text=self.string) 
        
    def botao4(self):
        self.string=self.string+'4'
        self.codigo.configure(text=self.string) 
        
    def botao5(self):
        self.string=self.string+'5'
        self.codigo.configure(text=self.string) 
        
    def botao6(self):
        self.string=self.string+'6'
        self.codigo.configure(text=self.string) 
        
    def botao7(self):
        self.string=self.string+'7'
        self.codigo.configure(text=self.string) 
        
    def botao8(self):
        self.string=self.string+'8'
        self.codigo.configure(text=self.string) 
        
    def botao9(self):
        self.string=self.string+'9'
        self.codigo.configure(text=self.string) 
        
    def botao0(self):
        self.string=self.string+'0'
        self.codigo.configure(text=self.string) 
        
    def cancela(self):
        self.string='' 
        self.codigo.configure(text=self.string)
        
    def ok(self):
        x = Pedido.buscar_codigo_nuvem(self, self.string)  
        print(x)
        self.string='' 
        self.codigo.configure(text=self.string)        
        return x
        
    
                

class mesa:
    def __init__(self,numero):
        self.numero=numero
    
  #  def registrar_pedido(self,mesa):
        


mapa=Mapa() 

