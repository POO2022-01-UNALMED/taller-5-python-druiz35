class Animal:
  __totalAnimales = 0
  def __init__(self, nombre, edad, habitat, genero):
    self.nombre = nombre
    self.edad = edad
    self.habitat = habitat
    self.genero = genero
    self.zona = []
    Animal.__totalAnimales += 1
  
  def getHabitat(self):
    return self.habitat
  
  def getGenero(self):
    return self.genero
  
  def getNombre(self):
    return self.nombre
  
  def getEdad(self):
    return self.edad
  
  
  @staticmethod
  def totalPorTipo():
    from .mamifero import Mamifero
    from .ave import Ave
    from .reptil import Reptil  
    from .pez import Pez
    from .anfibio import Anfibio
    nMamiferos = Mamifero.cantidadMamiferos()
    nAves = Ave.cantidadAves()
    nReptiles = Reptil.cantidadReptiles()
    nPeces = Pez.cantidadPeces()
    nAnfibios = Anfibio.cantidadAnfibios()
    mensaje = "Mamiferos: " + str(nMamiferos)+ "\nAves: " + str(nAves) + "\nReptiles: " + str(nReptiles)+ "\nPeces: " + str(nPeces)+ "\nAnfibios: " + str(nAnfibios)
    return mensaje
  
  
  def toString(self):
    if len(self.zona) == 0:
        mensaje_1 = "Mi nombre es " + self.nombre + ", tengo una edad de " + str(self.edad) + ", habito en " + self.habitat + " y mi genero es " + self.genero
        return mensaje_1
    else:
        mensaje_2 = "Mi nombre es " + self.nombre + ", tengo una edad de " + str(self.edad) + ", habito en " + self.habitat + " y mi genero es " + self.genero + ", la zona en la que me ubico es " + self.zona[0].getNombre() + ", en el " + self.zona[0].getZoo().getNombre()
        return mensaje_2