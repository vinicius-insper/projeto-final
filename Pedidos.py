from firebase import firebase
firebase = firebase.FirebaseApplication('https://smartserver.firebaseio.com')

class Pedido():

    def __init__(self, mesa, cadeira, hora, estado):
        self.mesa = mesa
        self.cadeira = cadeira
        self.hora = hora
        self.estado = estado
        
    def buscar_codigo_nuvem(self, codigo):
        x = firebase.get(url = '/Menu/', name= codigo)
        return x 
        
teste = Pedido(1,1,1,1)
y = teste.registrar_pedido('00')
print (y)