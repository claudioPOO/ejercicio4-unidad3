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
        def getMontoSeguro(cls):
            return cls.Montoseguro
        def getCostoObra(self):
            return self.__CostoObra
        def geTarea(self):
            return self.__Tarea
        def __init__(self,Dni,Nombre,Direccion,Telefono,tarea,inicio,fin,costo):
            super().__init__(Dni,Nombre,Direccion,Telefono)
            self.__Tarea=tarea
            self.__Finicio=inicio
            self.__Ffinaliza=fin
            self.__CostoObra=int(costo)
        def SueldoE(self):
            sueldo= self.getCostoObra() - self.getMontoV() - self.getMontoSeguro()
            return sueldo
        def __str__(self):
            s='Nombre {}\n'.format(self.getNombre())+'Dni {}\n'.format(self.getDni())+'Direccion {}\n'.format(self.getDireccion())+'Tarea {}\n'.format(self.__Tarea)+'Fecha Inicio {}\n'.format(self.__Finicio)+'Fecha Fin {}\n'.format(self.__Ffinaliza)+'Costo de la obra {}'.format(self.__CostoObra)
            return s