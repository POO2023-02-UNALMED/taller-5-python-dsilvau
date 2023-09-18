class Zona:
    def __init__(self, nombre, zoo= None, animales = None):
        self.nombre = nombre
        self.zoo = zoo
        if animales is None:
            self.animales = []
        else:
            self.animales = animales
    def getAnimales(self):
        return self.animales
    def getZoo(self):
        return self.zoo
    def setZoo(self, zoo):
        self.zoo = zoo
    def setAnimales(self, animales):
        self.animales = animales
    def getNombre(self):
        return self.nombre
    def setNombre(self, nombre):
        self.nombre = nombre
    def agregarAnimales(self, animal):
        self.animales.append(animal)
    def cantidadAnimales(self):
        return len(self.animales)
    def __str__(self):
        return self.nombre