from .animal import Animal
class Mamifero(Animal):
  __listado = []
  __caballos = 0
  __leones = 0
  def __init__(self, nombre=None, edad=None, habitat=None, genero=None, pelaje=None, patas=None):
    super().__init__(nombre, edad, habitat, genero)
    self.pelaje = pelaje
    self.patas = patas
    Mamifero.__listado.append(self)
  
  def isPelaje(self):
    return self.pelaje
  
  def getPatas(self):
    return self.patas
  
  @classmethod
  def cantidadMamiferos(cls):
    return len(Mamifero.__listado)
  
  @classmethod
  def crearCaballo(cls, nombre, edad, genero):
    caballo = Mamifero(nombre, edad, "pradera", genero, True, 4)
    Mamifero.__caballos += 1
    return caballo
  
  @classmethod
  def crearLeon(cls, nombre, edad, genero):
    leon = Mamifero(nombre, edad, "selva", genero, True, 4)
    Mamifero.__leones += 1
    return leon