class Zoologico:
  def __init__(self, nombre=None, ubicacion=None):
    self.nombre = nombre
    self.ubicacion = ubicacion
    self.zonas = []

  def getZona(self):
    return self.zonas
  
  def getNombre(self):
    return self.nombre
  
  def getUbicacion(self):
    return self.ubicacion
  
  def agregarZonas(self, nuevaZona):
    self.zonas.append(nuevaZona)

  def cantidadTotalAnimales(self):
    count = 0
    for zona in self.zonas:
      count = count + zona.cantidadAnimales()
    return count
  
