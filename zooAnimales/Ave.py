from zooAnimales.animal import Animal

class Ave(Animal):

    listado = list()
    halcones = 0
    aguilas = 0

    def __init__(self, nombre, edad, habitat, genero, colorPlumas, zona = None):
        super().__init__(nombre, edad, habitat, genero, zona)
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._colorPlumas = colorPlumas
        Ave.listado.append(self)

    def getColorPlumas(self):
        return self._colorPlumas

    def setColorPlumas(self, colorPlumas):
        self._colorPlumas = colorPlumas

    @classmethod
    def crearHalcon(cls, nombre, edad, genero, zona = None):
        halcon = Ave(nombre, edad, "montanas", genero, "cafe glorioso", zona)
        cls.halcones += 1

    @classmethod
    def crearAguila(cls, nombre, edad, genero, zona = None):
        aguila = Ave(nombre, edad, "montanas", genero, "blanco y amarillo", zona)
        cls.aguilas += 1

    @classmethod
    def cantidadAves(cls):
        return len(cls.listado)

    def movimiento(self):
        return "volar"