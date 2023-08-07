# Archivo de modelos y lista de modelos
class ListaModelos:
	def __init__(self):
		self._lista = []

	# Añado a la lista el elemento que se pasa por parámetro
	def add(self, value):
		self._lista.append(value)
		
	# Devuelvo el número de elementos que contiene la lista
	def count(self):
		total = 0
		for i in self._lista:
			total += 1
		return total
	
	# Me devuelve el item que estén activo
	def getItem(self, codigo):
		for elem in self._lista:
			if (codigo == elem.codigo) and (elem.activo == True):
				return elem

class Modelos:
	def __init__(self, codigo, descripcion):
		self.codigo = codigo
		self.descripcion = descripcion
		self.activo = True
	
	# Activamos o desactivamos según el valor del parámetro value
	def activar(self, value):
		self.activo = value





