from .animal import Animal
class Reptil(Animal):
  __listado = []
  serpientes = 0
  iguanas = 0
  def __init__(self, nombre=None, edad=None, habitat=None, genero=None, colorEscamas=None, largoCola=None):
    super().__init__(nombre, edad, habitat, genero)
    self.colorEscamas = colorEscamas
    self.largoCola = largoCola
    Reptil.__listado.append(self)
  
  def getColorEscamas(self):
    return self.colorEscamas
  
  def getLargoCola(self):
    return self.largoCola
  
  @classmethod
  def cantidadReptiles(cls):
    return len(cls.__listado)
  
  @classmethod
  def crearIguana(cls, nombre, edad, genero):
    iguana = Reptil(nombre, edad, "humedal", genero, "verde", 3)
    Reptil.iguanas += 1
    return iguana
  
  @classmethod
  def crearSerpiente(cls, nombre, edad, genero):
    serpiente = Reptil(nombre, edad, "jungla", genero, "blanco", 1)
    Reptil.serpientes += 1
    return serpiente