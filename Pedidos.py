from firebase import firebase
codigos = cMenu()
firebase = firebase.FirebaseApplication('https://smartserver.firebaseio.com/')
class cPedido():

    def __init__(self, nMesa, nCadeira):
        self.mesa = nMesa
        self.cadeira = nCadeira
        
    def buscar_e_colocar_codigo_FB(self, string, hora, status, n_pedido):
        for i in codigos.lista_codigos:
            if i == string:
                z = codigos.menu_codigos[string]
                x = z.keys()
                for e in x:
                    x = e
                y = z.values()
                for e in y:
                    y = e
                pedido_ = [hora, status, x, y]
                firebase.put(url = 'mesa{0}/cadeira{1}'.format(self.mesa, self.cadeira), name = 'pedido numero {0}'.format(n_pedido), data = pedido_)
                
    def iterar(self):
        lista='CADEIRA {0} \n'.format(self.cadeira)
        soma = 0 
        x= firebase.get(url='/mesa{0}/'.format(self.mesa),name= 'cadeira{0}'.format(self.cadeira))
        for i in x.values():
            if i[2] != 'produto':
                lista+=i[2]+str(i[3])+'\n'
                j= i[3]
                soma+=(j)
        lista+='total = '+str(soma)+'\n'
        lista+='c/ serviço = '+str("{0:.2f}".format(soma*1.1))
        return [lista,soma*1.1] 
