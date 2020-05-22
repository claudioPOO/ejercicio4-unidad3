from Empleado import Empleado
class Eexternos(Empleado):
        MontoViatico=int(100)
        Montoseguro=int(5000)                
        __CostoObra=0
        __Tarea=''
        __Finicio=''
        __Ffinaliza=''
        @classmethod
        def getMontoV(cls):
            return cls.MontoViatico
        @classmethod
        def getMontoSeguro(cls):
            return cls.Montoseguro
        def getCostoObra(self):
            return self.__CostoObra
        def geTarea(self):
            return self.__Tarea
        def getFinaliza(self):
            return self.__Ffinaliza
        def __init__(self,Dni,Nombre,Direccion,Telefono,tarea,inicio,fin,costo):
            super().__init__(Dni,Nombre,Direccion,Telefono)
            self.__Tarea=tarea
            self.__Finicio=inicio
            self.__Ffinaliza=fin
            self.__CostoObra=int(costo)
        def Sueldo(self):
            sueldo= self.getCostoObra() - self.getMontoV() - self.getMontoSeguro()
            return sueldo
        def MostrarDatos(self,band):
            if(band==True):
             super().MostrarDatos(band)
             print('Sueldo: {}'.format(self.Sueldo()))
            else:
             super().MostrarDatos(band)