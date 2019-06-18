#Questao4.py
class Carro(object):
	def __init__(self, consumoCombustivel): 
		self.consumoCombustivel = consumoCombustivel
		self.nivelCombustivel = 0

	def andar(self, distancia):
		if(distancia/self.consumoCombustivel > self.nivelCombustivel):
			print("Impossível percorrer toda a distancia!")
			print("Voce pode percorrer no maximo "+str(self.nivelCombustivel*self.consumoCombustivel)+"km")
		else:
			self.nivelCombustivel -= distancia/self.consumoCombustivel

	def obterGasolina(self):
		print(str(self.nivelCombustivel)+" litros")

	def adicionarGasolina(self, quantidade):
		self.nivelCombustivel = self.nivelCombustivel + quantidade





