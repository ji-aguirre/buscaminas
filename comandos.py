from buscaminas import Tablero

class Juego():
	def __init__(self,alto,largo,cantminas):

		self.tablero = Tablero()
		self.banderas_restantes = self.tablero.cant_minas
		self.pos_banderas = []
		self.cuadros_restantes = self.tablero.alto * self.tablero.largo
		self.tablero.inicializar(alto,largo,cantminas)
	#Jugar en la posicion x,y
	def jugada(self,x,y):
		jugada = self.tablero.chequear_posicion(x,y)
		self.cuadros_restantes -=1
		return jugada
	# Poner bandera en la posicion x,y
	def marcar_posicion(self,x,y):
		self.pos_banderas.append("{},{}".format(x,y))
		self.banderas_restantes -=1
		self.cuadros_restantes -=1
		return True
	#Guardar estado de la partida para volver mas tarde
	def guardar_partida(self):
		return True
	#Cargar una partida guardada desde un archivo
	def cargar_partida(self):
		return True	
	#Reinicia la partida con un nuevo tablero
	def reiniciar_juego(self):
		return True

	def exit(self):
		return 0



