from Empleado import Empleado
class Econtratado(Empleado):
    Valorxhora=150
    __Finicio=''
    __Fincontrato=''
    __cantHoras=0
    @classmethod
    def getValorxhora(cls):
        return cls.Valorxhora
    def __init__(self,Dni,nombre,direccion,telefono,inicio,fin,horas):
        super().__init__(Dni,nombre,direccion,telefono)
        self.__Finicio=inicio
        self.__Fincontrato=fin
        self.__cantHoras=int(horas)
    def getFinicio(self):
        return self.__Finicio
    def getFinC(self):
        return self.__Fincontrato
    def getCantH(self):
        return self.__cantHoras
    def sethora(self,hora):
        self.__cantHoras=self.__cantHoras+hora
    def SueldoC(self):
        sueldo=self.__cantHoras*self.getValorxhora()
        return sueldo
    def __str__(self):
        s='Nombre {}\n'.format(self.getNombre())+'Dni {}\n'.format(self.getDni())+'Direccion {}\n'.format(self.getDireccion())+'Fecha inicio {}\n'.format(self.__Finicio)+'Fin de contrato {}\n'.format(self.__Fincontrato)+'Horas {}\n'.format(self.__cantHoras)+'Valor de Hora {}'.format(self.getValorxhora())
        
        return s
    
    