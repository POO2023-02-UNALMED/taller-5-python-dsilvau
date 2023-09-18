from zooAnimales.animal import Animal

class Anfibio(Animal):

    listado = list()
    ranas = 0
    salamandras = 0

    def __init__(self, nombre, edad, habitat, genero, colorPiel, venenoso, zona = None):
        super().__init__(nombre, edad, habitat, genero, zona)
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._colorPiel = colorPiel
        self._venenoso = venenoso
        Anfibio.listado.append(self)

    def getColorPiel(self):
        return self._colorPiel

    def setColorPiel(self, colorPiel):
        self._colorPiel = colorPiel

    def isVenenoso(self):
        return self._venenoso

    def setVenenoso(self, venenoso):
        self._venenoso = venenoso

    @classmethod
    def crearRana(cls, nombre, edad, genero, zona = None):
        rana = Anfibio(nombre, edad, "selva", genero, "rojo", True, zona)
        cls.ranas += 1

    @classmethod
    def crearSalamandra(cls, nombre, edad, genero, zona = None):
        salamandra = Anfibio(nombre, edad, "selva", genero, "negro y amarillo", False, zona)
        cls.salamandras += 1

    @classmethod
    def cantidadAnfibios(cls):
        return len(cls.listado)

    def movimiento(self):
        return "saltar"