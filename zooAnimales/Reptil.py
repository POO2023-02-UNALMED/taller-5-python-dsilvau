from zooAnimales.animal import Animal

class Reptil(Animal):

    listado = list()
    iguanas = 0
    serpientes = 0

    def __init__(self, nombre, edad, habitat, genero, colorEscamas, largoCola, zona = None):
        super().__init__(nombre, edad, habitat, genero, zona)
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola
        Reptil.listado.append(self)

    def getColorEscamas(self):
        return self._colorEscamas

    def setColorEscamas(self, colorEscamas):
        self._colorEscamas = colorEscamas

    def getLargoCola(self):
        return self._largoCola

    def setLargoCola(self, largoCola):
        self._largoCola = largoCola

    @classmethod
    def crearIguana(cls, nombre, edad, genero, zona = None):
        iguana = Reptil(nombre, edad, "humedal", genero, "verde", 3, zona)
        cls.iguanas += 1

    @classmethod
    def crearSerpiente(cls, nombre, edad, genero, zona = None):
        serpiente = Reptil(nombre, edad, "jungla", genero, "blanco", 1, zona)
        cls.serpientes += 1

    @classmethod
    def cantidadReptiles(cls):
        return len(cls.listado)

    def movimiento(self):
        return "reptar"