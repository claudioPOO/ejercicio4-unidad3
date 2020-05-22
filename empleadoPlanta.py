from Empleado import Empleado
class Eplanta(Empleado):
    __SueldoBasico=0.0
    __Antiguedad=0
    def __init__(self,Dni,Nombre,Direccion,Telefono,sb,ant):
        super().__init__(Dni,Nombre,Direccion,Telefono)
        self.__SueldoBasico=float(sb)
        self.__Antiguedad=int(ant)
    def Sueldo(self):
        porc=self.__SueldoBasico*(0.01)
        sueldo=int(self.__SueldoBasico+porc*self.__Antiguedad)
        return sueldo
    def getSueldoBasico(self):
        return self.__SueldoBasico
    def getAntiguedad(self):
        return self.__Antiguedad
    def MostrarDatos(self,band):
        if(band==True):
            super().MostrarDatos(band)
            print('Sueldo: {}'.format(self.Sueldo()))
        else:
            super().MostrarDatos(band)