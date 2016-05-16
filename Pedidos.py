from BancodeDados import cMenu
from firebase import firebase
codigos = cMenu()
firebase = firebase.FirebaseApplication('https://smartserver.firebaseio.com/')
class cPedido():

    def __init__(self, nMesa, nCadeira):
        self.mesa = nMesa
        self.cadeira = nCadeira
        self.novo_pedido = 0
        
    def buscar_e_colocar_codigo_FB(self, string):
    	for i in codigos.lista_codigos:
    		if i == string:
    			z = codigos.menu_codigos[string]
    			firebase.put(url = 'mesa{0}/'.format(self.mesa), name = 'cadeira{0}'.format(self.cadeira), data = z)
