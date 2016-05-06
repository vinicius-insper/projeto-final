class Menu:
	def __init__(self):
		self.menu_codigos = {}
		self.menu_codigos['000'] = {'Coca Cola': 3.50}
		self.menu_codigos['001'] = {'Guarana': 3.50}
		self.menu_codigos['002'] = {'Citrus': 3.50}
		self.menu_codigos['003'] = {'Agua': 3.00}
		self.menu_codigos['004'] = {'Sucos': 4.50}
		self.menu_codigos['005'] = {'Batata Frita': 9.00}
		self.menu_codigos['006'] = {'Polenta Frita': 10.00}
		self.menu_codigos['007'] = {'Mandioca Frita': 9.50}
		self.menu_codigos['008'] = {'Burguer': 8.50}
		self.menu_codigos['009'] = {'X-Burguer': 9.50}
		self.menu_codigos['010'] = {'Frango': 9.50}
		self.menu_codigos['011'] = {'X-Frango': 10.50}
		self.menu_codigos['012'] = {'Ovo': 1.50}
		self.menu_codigos['013'] = {'Bacon': 1.50}
		self.menu_codigos['014'] = {'Salada': 1.50}
		self.menu_codigos['015'] = {'MilkShake': 5.50}


from firebase import firebase
menu = Menu()
firebase = firebase.FirebaseApplication('https://smartserver.firebaseio.com')
result = firebase.put('/', name = 'Menu', data = menu.menu_codigos)
print(result)
  
