from BancodeDados import cMenu
from firebase import firebase
codigos = cMenu()
firebase = firebase.FirebaseApplication('https://smartserver.firebaseio.com/')
class cPedido():

    def __init__(self, nMesa, nCadeira):
        self.mesa = nMesa
        self.cadeira = nCadeira
        
    def buscar_e_colocar_codigo_FB(self, string):
        for i in codigos.lista_codigos:
            if i == string:
                z = codigos.menu_codigos[string]
                x = z.keys()
                for e in x:
                    x = e
                y = z.values()
                for e in y:
                    y = e
                firebase.put(url = 'mesa{0}/cadeira{1}'.format(self.mesa, self.cadeira), name = x , data = y)

