from .animal import Animal
class Ave(Animal):
  __listado = []
  halcones = 0
  aguilas = 0
  def __init__(self, nombre=None, edad=None, habitat=None, genero=None, colorPlumas=None):
    super().__init__(nombre, edad, habitat, genero)
    self.colorPlumas = colorPlumas
    Ave.__listado.append(self)
  
  def getColorPlumas(self):
    return self.colorPlumas
    
  @classmethod
  def cantidadAves(cls):
    return len(cls.__listado)
  
  @classmethod
  def crearHalcon(cls, nombre, edad, genero):
    halcon = Ave(nombre, edad, "montanas", genero, "cafe glorioso")
    Ave.halcones += 1
    return halcon
  
  @classmethod
  def crearAguila(cls, nombre, edad, genero):
    aguila = Ave(nombre, edad, "montanas", genero, "blanco y amarillo")
    Ave.aguilas += 1
    return aguila