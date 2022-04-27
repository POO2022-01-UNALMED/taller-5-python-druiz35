from .animal import Animal
class Anfibio(Animal):
  __listado = []
  __ranas = 0
  __salamandras = 0
  def __init__(self, nombre=None, edad=None, habitat=None, genero=None, colorPiel=None, venenoso=None):
    super().__init__(nombre, edad, habitat, genero)
    self.colorPiel = colorPiel
    self.venenoso = venenoso
    Anfibio.__listado.append(self)
  
  def getColorPiel(self):
    return self.colorPiel
  
  def isVenenoso(self):
    return self.venenoso
    
  @classmethod
  def cantidadAnfibios(cls):
    return len(cls.__listado)
  
  @classmethod
  def crearRana(cls, nombre, edad, genero):
    rana = Anfibio(nombre, edad, "selva", genero, "rojo", True)
    Anfibio.__ranas += 1
    return rana
  
  @classmethod
  def crearSalamandra(cls, nombre, edad, genero):
    salamandra = Anfibio(nombre, edad, "selva", genero, "negro y amarillo", False)
    Anfibio.__salamandras += 1
    return salamandra