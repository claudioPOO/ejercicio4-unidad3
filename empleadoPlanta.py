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
    def __str__(self):
        s='Nombre {}\n'.format(self.getNombre())+'Dni {}\n'.format(self.getDni())+'Direccion {}\n'.format(self.getDireccion())+'Sueldo Basico {}\n'.format(self.__SueldoBasico)+'Antiguedad {}\n'.format(self.__Antiguedad)
        return s