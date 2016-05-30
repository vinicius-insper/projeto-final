import tkinter as tk
import time 
from Pedidos import cPedido
from firebase import firebase
firebase = firebase.FirebaseApplication('https://smartserver.firebaseio.com/')



class cInicio:
    def __init__(self):
        self.window=tk.Tk()
        self.window.title ('Inicio') 

    def iniciar(self):
        self.frame = tk.Frame(self.window, width=500, height=500, bd=175)
        self.frame.pack()
        
        self.botaomapa = tk.Button(self.frame,text ='Mapa',height=8 ,width= 20 ,bd=20,padx=20)
        self.botaomapa.pack(side=tk.LEFT)
        self.botaomapa.configure(command = mesa.iniciar)
        
        self.botaocozinha = tk.Button(self.frame,text ='Cozinha',height=8 ,width=20 ,bd=20,padx=20)
        self.botaocozinha.pack(side=tk.RIGHT)
        self.botaocozinha.configure(command = cozinha.iniciar)

        self.window.mainloop()

class cCozinha:
    def __init__(self):
        self.variavel = 1

    def iniciar(self):
        self.cozinha = tk.Tk()
        self.cozinha.title("Cozinha")

        self.ativos={}

        self.label1=tk.Label(self.cozinha)
        self.label1.configure(width=49,height=8, text='Para Fazer', bg='red')
        self.label1.grid(row=0,column=1)
        
        self.label2=tk.Label(self.cozinha)
        self.label2.configure(width=49,height=8, text='Fazendo', bg='yellow')
        self.label2.grid(row=0,column=2)
        
        self.label3=tk.Label(self.cozinha)
        self.label3.configure(width=49,height=8, text='Pronto', bg='green')
        self.label3.grid(row=0,column=3)

        self.botao1=tk.Button(self.cozinha,width=6,height=5)
        self.botao1.configure(text='refresh')
        self.botao1.configure(command=lambda:self.buscar_pedido())
        self.botao1.grid(row = 0,column = 0 )
        
        self.variavelrow=1
        self.pedido=0

        self.cozinha.mainloop()
        
    def buscar_pedido(self):
        x = firebase.get(url='/',name='')
        for i in x.keys():
            for j in x[i].keys():
                for k in x[i][j]:
                    if k != 'produto':
                        if x[i][j][k][1] == '':
                            self.criar_botao(x[i][j][k][2]+'\n'+i+'\n'+j,i,j,k) 
                            firebase.put(url='/'+i+'/'+j+'/'+k,name=1,data='a fazer')

    def criar_botao(self, texto,mesa,cadeira,pedidon):        
        B = tk.Button(self.cozinha,width=40,height=5,text=texto) 
        B.grid(row = self.variavelrow , column =1) 
        B.configure(command = lambda:self.para_fazer(B,Bv,mesa,cadeira,pedidon)) 

        Bv = tk.Button(self.cozinha,width=5,height=3,text='cancela',bg='red') 
        Bv.grid(row = self.variavelrow , column =0)
        Bv.configure(command = lambda:self.cancela_pedido(Bv,B,mesa,cadeira,pedidon)) 
        
        self.variavelrow += 1
        self.pedido+=1

        self.ativos[B]=1

    def para_fazer(self,B,Bv,mesa,cadeira,pedidon):
        self.ativos[B]+=1
        B.grid( column= self.ativos[B])
        Bv.destroy()
        if self.ativos[B]==2:
            firebase.put(url='/'+mesa+'/'+cadeira+'/'+pedidon,name=1,data='fazendo')
        if self.ativos[B]==3:
            firebase.put(url='/'+mesa+'/'+cadeira+'/'+pedidon,name=1,data='feito')
        if self.ativos[B] >3:
            firebase.put(url='/'+mesa+'/'+cadeira+'/'+pedidon,name=1,data='entregue')
            B.destroy()
            
    def cancela_pedido(self,Bv,B,mesa,cadeira,pedidon):
        Bv.destroy()
        B.destroy()
        firebase.delete(url='/'+mesa+'/'+cadeira,name=pedidon)

class cMesa:
    def __init__(self):
        self.nMesa = 'x'
        
    def iniciar(self):
        self.string=''
        self.mapa= tk.Tk()
        self.mapa.title('Mapa Restaurante') 
        self.mapa.configure(bg='green')

        self.mesa1=tk.Button(self.mapa)
        self.mesa1.configure(command= lambda: self.callback_mesa(1), text='mesa 1', width= 14, height= 6, bg='yellow')   
        self.mesa1.grid(row=0,column=0)
        
        self.mesa2=tk.Button(self.mapa)
        self.mesa2.configure(command= lambda: self.callback_mesa(2), text='mesa 2', width= 14, height= 6, bg='yellow')
        self.mesa2.grid(row=2,column=0)
        
        self.mesa3=tk.Button(self.mapa)
        self.mesa3.configure(command= lambda: self.callback_mesa(3), text='mesa 3', width= 14, height= 6, bg='yellow')
        self.mesa3.grid(row=4,column=0)
        
        self.mesa4=tk.Button(self.mapa)
        self.mesa4.configure(command= lambda: self.callback_mesa(4), text='mesa 4', width= 14, height= 6, bg='yellow')
        self.mesa4.grid(row=0,column=2)
        
        self.mesa5=tk.Button(self.mapa)
        self.mesa5.configure(command= lambda: self.callback_mesa(5), text='mesa 5', width= 14, height= 6, bg='yellow')
        self.mesa5.grid(row=2,column=2)
        
        self.mesa6=tk.Button(self.mapa)
        self.mesa6.configure(command= lambda: self.callback_mesa(6), text='mesa 6', width= 14, height= 6, bg='yellow')
        self.mesa6.grid(row=4,column=2)
      
        self.mesa7=tk.Button(self.mapa)
        self.mesa7.configure(command= lambda: self.callback_mesa(7), text='mesa 7', width= 21, height= 6, bg='yellow')
        self.mesa7.grid(row=0,column=4)
        
        self.mesa8=tk.Button(self.mapa)
        self.mesa8.configure(command= lambda: self.callback_mesa(8), text='mesa 8', width= 21, height= 6, bg='yellow')
        self.mesa8.grid(row=2,column=4)
       
        self.mesa9=tk.Button(self.mapa)
        self.mesa9.configure(command= lambda: self.callback_mesa(9), text='mesa 9', width= 21, height= 6, bg='yellow')
        self.mesa9.grid(row=4,column=4)
     
        self.mapa.mainloop()

    def callback_mesa(self, numero):
        self.nMesa = numero
        if self.nMesa <= 6:
            cadeira.criar_4_cadeiras()
            str(self.nMesa)
        else:
            cadeira.criar_6_cadeiras()
            str(self.nMesa)

class cCadeira:
    
    def __init__(self):
        self.nCadeira = 'y'

    def criar_4_cadeiras(self):
        self.tela=tk.Tk()
        self.tela.title('mesa')
        self.tela.configure(bg='green')
        
        self.cliente1=tk.Button(self.tela)
        self.cliente1.configure(command= lambda: self.callback_cadeira(1), text='cadeira 1', width=14,height=6, bg='yellow')
        self.cliente1.grid(row=0, column=0)
        
        self.cliente2=tk.Button(self.tela)
        self.cliente2.configure(command= lambda: self.callback_cadeira(2), text='cadeira 2', width=14,height=6, bg='yellow')
        self.cliente2.grid(row=0,column=1)
        
        self.cliente3=tk.Button(self.tela)
        self.cliente3.configure(command= lambda: self.callback_cadeira(3), text='cadeira 3', width=14,height=6, bg='yellow')        
        self.cliente3.grid(row=1,column=0)
        
        self.cliente4=tk.Button(self.tela)
        self.cliente4.configure(command= lambda: self.callback_cadeira(4), text='cadeira 4', width=14,height=6, bg='yellow')
        self.cliente4.grid(row=1,column=1)
        
        self.fecharmesa=tk.Button(self.tela)
        self.fecharmesa.configure(text='fechar conta mesa', width=20,height=6, bg='blue')
        self.fecharmesa.configure(command=self.fechar_conta_mesa)
        self.fecharmesa.grid(row=3,column=0)
        
        self.fecharind=tk.Button(self.tela)
        self.fecharind.configure(text='fechar conta por pessoa', width=20,height=6, bg='red')
        self.fecharind.configure(command=self.fechar_conta_indiv)
        self.fecharind.grid(row=3,column=1)
        
        self.tela.mainloop()

    def criar_6_cadeiras(self):
        self.tela=tk.Tk()
        self.tela.title('mesa')
        self.tela.configure(bg='green')

        self.cliente1=tk.Button(self.tela)
        self.cliente1.configure(command= lambda: self.callback_cadeira(1), text='cadeira 1', width=14,height=6, bg='yellow')
        self.cliente1.grid(row=0, column=0)
        
        self.cliente2=tk.Button(self.tela)
        self.cliente2.configure(command= lambda: self.callback_cadeira(2), text='cadeira 2', width=14,height=6, bg='yellow')
        self.cliente2.grid(row=0,column=1)
        
        self.cliente3=tk.Button(self.tela)
        self.cliente3.configure(command= lambda: self.callback_cadeira(3), text='cadeira 3', width=14,height=6, bg='yellow')        
        self.cliente3.grid(row=1,column=0)
        
        self.cliente4=tk.Button(self.tela)
        self.cliente4.configure(command= lambda: self.callback_cadeira(4), text='cadeira 4', width=14,height=6, bg='yellow')
        self.cliente4.grid(row=1,column=1)
 
        self.cliente5=tk.Button(self.tela)
        self.cliente5.configure(command= lambda: self.callback_cadeira(5), text='cadeira 5', width=14,height=6, bg='yellow')
        self.cliente5.grid(row=2,column=0)
        
        self.cliente6=tk.Button(self.tela)
        self.cliente6.configure(command= lambda: self.callback_cadeira(6), text='cadeira 6', width=14,height=6, bg='yellow')
        self.cliente6.grid(row=2,column=1)

        self.fecharmesa=tk.Button(self.tela)
        self.fecharmesa.configure(text='fechar conta mesa', width=20,height=6, bg='blue')
        self.fecharmesa.configure(command=self.fechar_conta_mesa)
        self.fecharmesa.grid(row=3,column=0)
        
        self.fecharind=tk.Button(self.tela)
        self.fecharind.configure(text='fechar conta por pessoa', width=20,height=6, bg='red')
        self.fecharind.configure(command=self.fechar_conta_indiv)
        self.fecharind.grid(row=3,column=1)

        self.tela.mainloop()

    def callback_cadeira(self, numero):
        self.nCadeira = str(numero)
        teclado.criar_teclado()
        
    def fechar_conta_indiv(self):        
        self.relatório=tk.Tk()
        self.relatório.title('Conta')
        
        self.somamesa=0
        
        self.zerar=tk.Button(self.relatório)  
        self.zerar.grid(column=5,row=2)
        self.zerar.configure(text='Tem Certeza?')
        self.zerar.configure(width=20,height=3,bg='blue')
        self.zerar.configure(command=self.zerar_firebase)
        
        if mesa.nMesa <7:            
            for i in range(1,5):
                x=cPedido(mesa.nMesa,i)
                self.conta=tk.Label(self.relatório)
                self.conta.configure(width=100)
                self.conta.configure(text=(x.iterar()[0]))
                self.conta.grid(row=i) 
                self.somamesa+=x.iterar()[1]
        
        else:
            for i in range(1,7):
                x=cPedido(mesa.nMesa,i)
                self.conta=tk.Label(self.relatório)
                self.conta.configure(width=100)
                self.conta.configure(text=(x.iterar()[0]))
                self.conta.grid(row=i) 
                self.somamesa+=x.iterar()[1]

    def fechar_conta_mesa(self):
        self.fechar_conta_indiv()
        self.conta=tk.Label(self.relatório)            
        self.conta.configure(text='Total da mesa = '+'{0:.2f}'.format(self.somamesa))
        self.conta.grid(row=8)
        
        self.relatório.mainloop()
            
    def zerar_firebase(self):
        mesa1={}
        mesa1['cadeira1']={'produto':[1,2,'produto',0]}
        mesa1['cadeira2']={'produto':[1,2,'produto',0]}
        mesa1['cadeira3']={'produto':[1,2,'produto',0]}
        mesa1['cadeira4']={'produto':[1,2,'produto',0]}
        
        mesa2={}
        mesa2['cadeira1']={'produto':[1,2,'produto',0]}
        mesa2['cadeira2']={'produto':[1,2,'produto',0]}
        mesa2['cadeira3']={'produto':[1,2,'produto',0]}
        mesa2['cadeira4']={'produto':[1,2,'produto',0]}
        mesa2['cadeira5']={'produto':[1,2,'produto',0]}
        mesa2['cadeira6']={'produto':[1,2,'produto',0]}
        if mesa.nMesa<7:
            firebase.put(url='/', name='mesa{0}'.format(mesa.nMesa),data=mesa1)
        else:
            firebase.put(url='/', name='mesa{0}'.format(mesa.nMesa),data=mesa2)

class cTeclado:
    def __init__(self):
        self.n_pedido = 1
        
    def criar_teclado(self): 
        self.teclado=tk.Tk()
        self.teclado.title('teclado')

        self.codigo=tk.Label(self.teclado)
        self.codigo.grid(row=0)
        
        self.b1=tk.Button(self.teclado)
        self.b1.configure(command= lambda: self.botao(1), text='1', width=14,height=6)
        self.b1.grid(row=1,column=0)
        
        self.b2=tk.Button(self.teclado)
        self.b2.configure(command= lambda: self.botao(2), text='2', width=14,height=6)
        self.b2.grid(row=1,column=1)
        
        self.b3=tk.Button(self.teclado)
        self.b3.configure(command= lambda: self.botao(3), text='3', width=14,height=6) 
        self.b3.grid(row=1,column=2)
        
        self.b4=tk.Button(self.teclado)
        self.b4.configure(command= lambda: self.botao(4), text='4', width=14,height=6)
        self.b4.grid(row=2,column=0)
        
        self.b5=tk.Button(self.teclado)
        self.b5.configure(command= lambda: self.botao(5), text='5', width=14,height=6)
        self.b5.grid(row=2,column=1)
        
        self.b6=tk.Button(self.teclado)
        self.b6.configure(command= lambda: self.botao(6), text='6', width=14,height=6)
        self.b6.grid(row=2,column=2)
        
        self.b7=tk.Button(self.teclado)
        self.b7.configure(command= lambda: self.botao(7), text='7', width=14,height=6)
        self.b7.grid(row=3,column=0)
        
        self.b8=tk.Button(self.teclado)
        self.b8.configure(command= lambda: self.botao(8), text='8', width=14,height=6)
        self.b8.grid(row=3,column=1)
        
        self.b9=tk.Button(self.teclado)
        self.b9.configure(command= lambda: self.botao(9), text='9', width=14,height=6)
        self.b9.grid(row=3,column=2)
        
        self.b0=tk.Button(self.teclado)
        self.b0.configure(command= lambda: self.botao(0), text='0', width=14,height=6)
        self.b0.grid(row=4,column=1)
        
        self.bok=tk.Button(self.teclado)
        self.bok.configure(command=self.ok, text='OK', width=14,height=6, bg='green')
        self.bok.grid(row=4,column=0)
        
        self.bcancela=tk.Button(self.teclado)
        self.bcancela.configure(command=self.cancela, text='CANCELA', width=14,height=6, bg='red')
        self.bcancela.grid(row=4,column=2)
        
        self.string=''
        
        self.teclado.mainloop()

    def botao(self, numero):
        self.string=self.string+str(numero)
        self.codigo.configure(text=self.string) 
        
    def cancela(self):
        self.string='' 
        self.codigo.configure(text=self.string)

    def ok(self):
        pedido = cPedido(mesa.nMesa, cadeira.nCadeira)
        t = time.localtime()
        pedido.buscar_e_colocar_codigo_FB(self.string, time.asctime(t), '', self.n_pedido)
        self.n_pedido += 1
        self.string='' 
        self.codigo.configure(text=self.string)

cadeira = cCadeira()
teclado = cTeclado()
mesa = cMesa()
cozinha = cCozinha()
inicio = cInicio()
inicio.iniciar()
