#BUSCAMINAS
import random


class Tablero():
	def __init__(self):
		self.largo = 0
		self.alto = 0
		self.cant_minas = 0
		self.pos_minas = {}
		self.tablero = None

	def __getitem__(self,tup):
		x,y = tup
		return self.tablero[y][x]

	def mostrar_tablero(self):
		for linea in self.tablero:
			for char in linea:
				if char == -1:
					print("*"," |",end='\0')
				else:
					print(char,' |',end = '\0')
			print()
	def poblar_tablero(self):

		i = 0
		while i < self.cant_minas:

			random_x = random.choice(range(1,self.largo))
			random_y = random.choice(range(1,self.alto))
			self.pos_minas["{},{}".format(random_x,random_y)] = True			

#			if (random_x,random_y) in self.pos_minas:
#				new_random_x = random.choice(range(1,self.largo))
#				new_random_y = random.choice(range(1,self.alto))
#				self.pos_minas[(new_random_x,new_random_y)] = True

			i +=1

		return self.pos_minas

	def dibujar_tablero(self):
		minas = self.poblar_tablero()
		x = 0
		y = 0

		tablero_y = [] 
		for y in range(0,self.alto):
			tablero_x = []

			for x in range(self.largo):

				if "{},{}".format(x,y) in minas:
					tablero_x.append(-1)
				else:
					tablero_x.append(0) 

			tablero_y.append(tablero_x)

		self.tablero = tablero_y

	def calcular_adyacentes(self):
		print("Entro en calcular_adyacentes")
		for y in range(len(self.tablero)):
			for x in range(len(self.tablero[y])):

				if self.tablero[y][x] == -1:
					if 0 <= x+1 < self.largo and 0 <= x-1 < self.largo and 0<=y-1<=self.alto and 0<=y+1< self.alto: 
						if self.tablero[y][x+1] >= 0:
							self.tablero[y][x+1] += 1
						if self.tablero[y][x-1] >= 0:
							self.tablero[y][x-1] += 1
						if self.tablero[y+1][x+1] >= 0:
							self.tablero[y+1][x+1] += 1
						if self.tablero[y+1][x-1] >= 0:
							self.tablero[y+1][x-1] += 1
						if self.tablero[y-1][x-1] >= 0:
							self.tablero[y-1][x-1] += 1
						if self.tablero[y-1][x+1] >= 0:
							self.tablero[y-1][x+1] += 1
						if self.tablero[y-1][x] >= 0:
							self.tablero[y-1][x] += 1
						if self.tablero[y+1][x] >= 0:
							self.tablero[y+1][x] += 1

	def chequear_posicion(self,x,y):

		if "{},{}".format(x,y) in self.pos_minas:
			print("EXPLOTASTE!")
			return True
		return False
	def inicializar(self,largo,alto,cant_minas):
		self.alto = alto
		self.largo = largo
		self.cant_minas = cant_minas

		self.poblar_tablero()
		self.dibujar_tablero()
		self.calcular_adyacentes()
		return self.tablero

def main():

	tablero = Tablero()
	tablero.inicializar(10,10,15)
	tablero.mostrar_tablero()
	tablero.chequear_posicion(3,7)

#main()

