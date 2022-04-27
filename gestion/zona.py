class Zona:
  def __init__(self, nombre=None, zoo=None):
    self.nombre = nombre
    self.zoo = zoo
    self.animales = []
  
  def getZoo(self):
    return self.zoo
  
  def getNombre(self):
    return self.nombre

  def agregarAnimales(self, nuevoAnimal):
    self.animales.append(nuevoAnimal)
  
  def cantidadAnimales(self):
    return len(self.animales)