import  os
import datetime
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
        d=ME.buscar(dni)
        if(d!=0):
            horas=int(input('Horas Trabajadas '))
            ME.agregarhora(d-1,horas)
            ME.mostrar()
        else:
            print('DNI NO ENCONTRADO O NO PERTENECE AL SECTOR CONTRATADOS')
    def  opcion2 ( self,ME ):
        obra=input('Obra ')
        ME.buscarobra(obra)
    def opcion3(self,ME):
        print('Empleados que necesitan ayuda')
        ME.ayuda()
    def opcion4(self,ME):
      print('----Sueldos----')
      ME.inciso4()
    
        