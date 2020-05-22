import  os
from datetime import date
from empleadoContratado import Econtratado
class Menu :
    __switcher = None
    def  __init__ ( self ):
        self.__switcher  = { 1 : self.opcion1 ,
                            2 : self. opcion2 ,
                            3: self. opcion3,
                            4: self .opcion4,
                            0: self. salir
                         }
    def  getSwitcher ( self ):
        return self. __switcher
    def  opcion ( self , op,ME):
        func = self . __switcher . get ( op , lambda : print ( "Opción no válida" ))
        func ( ME )
    def  salir ( self,ME):
        print ( 'Salir' )
    def  opcion1 (self, ME):
        dni=int(input('DNI para registrar horas '))
        os.system('cls')
        d=ME.buscar(dni)
        if(isinstance(d,Econtratado)==True):
            horas=int(input('Horas Trabajadas '))
            d.sethora(horas)
            band=True
        else:
            print('DNI NO ENCONTRADO O NO PERTENECE AL SECTOR CONTRATADOS')
    def  opcion2 ( self,ME ):
        obra=input('Obra ')
        ME.buscaobra(obra)
    def opcion3(self,ME):
        print('Empleados que necesitan ayuda')
        ME.ayuda()
    def opcion4(self,ME):
      print('----Sueldos----')
      ME.inciso4()
    
        
