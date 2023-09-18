from zooAnimales.animal import Animal

class Pez(Animal):

    listado = list()
    salmones = 0
    bacalaos = 0

    def __init__(self, nombre, edad, habitat, genero, colorEscamas, cantidadAletas, zona = None):
        super().__init__(nombre, edad, habitat, genero, zona)
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas
        Pez.listado.append(self)

    def getColorEscamas(self):
        return self._colorEscamas

    def setColorEscamas(self, colorEscamas):
        self._colorEscamas = colorEscamas

    def getCantidadAletas(self):
        return self._cantidadAletas

    def setCantidadAletas(self, cantidadAletas):
        self._cantidadAletas = cantidadAletas

    @classmethod
    def crearSalmon(cls, nombre, edad, genero, zona = None):
        salmon = Pez(nombre, edad, "oceano", genero, "rojo", 6, zona)
        cls.salmones += 1

    @classmethod
    def crearBacalao(cls, nombre, edad, genero, zona = None):
        bacalao = Pez(nombre, edad, "oceano", genero, "gris", 6, zona)
        cls.bacalaos += 1

    @classmethod
    def cantidadPeces(cls):
        return len(cls.listado)

    def movimiento(self):
        return "nadar"