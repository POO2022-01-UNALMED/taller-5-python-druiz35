from .animal import Animal
class Pez(Animal):
  __listado = []
  bacalaos = 0
  salmones = 0
  def __init__(self, nombre=None, edad=None, habitat=None, genero=None, colorEscamas=None, cantidadAletas=None):
    super().__init__(nombre, edad, habitat, genero)
    self.colorEscamas = colorEscamas
    self.cantidadAletas = cantidadAletas
    Pez.__listado.append(self)
  
  def getColorEscamas(self):
    return self.colorEscamas
  
  def getCantidadAletas(self):
    return self.cantidadAletas
  
  @classmethod
  def cantidadPeces(cls):
    return len(Pez.__listado)
  
  @classmethod
  def crearBacalao(cls, nombre, edad, genero):
    bacalao = Pez(nombre, edad, "oceano", genero, "rojo", 6)
    Pez.bacalaos += 1
    return bacalao
  
  @classmethod
  def crearSalmon(cls, nombre, edad, genero):
    salmon = Pez(nombre, edad, "selva", genero, True, 4)
    Pez.salmones += 1
    return salmon