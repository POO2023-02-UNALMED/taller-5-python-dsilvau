from zooAnimales.animal import Animal

class Mamifero(Animal):

    listado = list()
    caballos = 0
    leones = 0

    def __init__(self, nombre, edad, habitat, genero, pelaje, patas, zona = None):
        super().__init__(nombre, edad, habitat, genero, zona)
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = zona
        self._pelaje = pelaje
        self._patas = patas
        Mamifero.listado.append(self)


    def isPelaje(self):
        return self._pelaje

    def setPelaje(self, pelaje):
        self._pelaje = pelaje

    def getPatas(self):
        return self._patas

    def setPatas(self, patas):
        self._patas = patas

    @classmethod
    def crearCaballo(cls, nombre, edad, genero, zona = None):
        caballo = Mamifero(nombre, edad, "pradera", genero, True, 4, zona)
        cls.caballos += 1

    @classmethod
    def crearLeon(cls, nombre, edad, genero, zona = None):
        leon = Mamifero(nombre, edad, "selva", genero, True, 4, zona)
        cls.leones += 1

    @classmethod
    def cantidadMamiferos(cls):
        return len(cls.listado)