import csv
import numpy as np
from Empleado import Empleado
from empleadoPlanta import Eplanta
from empleadoContratado import Econtratado
from empleadoExterno import Eexternos
class ManejaEmpleados:
    __arreEmp=None
    __indice=0
    def __init__(self,cantidad):
        self.__arreEmp=np.empty(cantidad,dtype=Empleado)
        self.__indice=0
    def cargarEmpleados(self):
        archi=open('Planta.csv')
        reader=csv.reader(archi,delimiter=';')
        for fila in reader:
            UnEmpleado=Eplanta(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5])
            self.__arreEmp[self.__indice]=UnEmpleado
            self.__indice=self.__indice+1
        archi.close()  
        archi=open('Contratados.csv')
        reader=csv.reader(archi,delimiter=';')
        for fila in reader:
             
             UnEmpleado=Econtratado(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],fila[6])
             self.__arreEmp[self.__indice]=UnEmpleado
             self.__indice=self.__indice+1
        archi.close()
        archi=open('externos.csv')
        reader=csv.reader(archi,delimiter=';')
        for fila in reader:
            UnEmpleado=Eexternos(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],fila[6],fila[7])
            self.__arreEmp[self.__indice]=UnEmpleado
            self.__indice=self.__indice+1
        archi.close()    
    def mostrar(self):
        for i in range(self.__indice):
            if(isinstance(self.__arreEmp[i],Eplanta)==True):
                print(self.__arreEmp[i])
            else:
                if(isinstance(self.__arreEmp[i],Econtratado)==True):
                  print(self.__arreEmp[i])
                else:
                    if(isinstance(self.__arreEmp[i],Eexternos)==True):
                        print(self.__arreEmp[i])
    def buscar(self,dni):
        i=0
        band=0
        while(i<len(self.__arreEmp))and(band==0):
            if(isinstance(self.__arreEmp[i],Econtratado)==True):
                if(self.__arreEmp[i].getDni()==dni):
                    band=1
                else:
                    i=i+1
            else:
                    i=i+1
        if(band!=0):
            return i+1
        else:
            return 0

    def agregarhora(self,indice,hora):
        self.__arreEmp[indice].sethora(hora)                        
    def buscaobra(self,obra):
        i=0
        band=0
        while(i<len(self.__arreEmp))and(band==0):
            if(isinstance(self.__arreEmp[i],Eexternos)==True):
                if(self.__arreEmp[i].geTarea().lower()==obra.lower()):
                    if(int(self.__arreEmp[i].getCostoObra())!=0):
                        print('El costo de la obra es: {}'.format(self.__arreEmp[i].getCostoObra())) 
                
                    else:
                        print('Obra finalizada')
                    band=1     
                else:
                 i=i+1
            else:
                i=i+1
        if(band==0):
            print('No se encontro la obra')
    def ayuda(self):
        for i in range(self.__indice):
            if(isinstance(self.__arreEmp[i],Eplanta)==True):
                if(self.__arreEmp[i].Sueldo()<25000):
                    print(self.__arreEmp[i].DatosAyuda())
            else:
                if(isinstance(self.__arreEmp[i],Econtratado)==True):
                    if(self.__arreEmp[i].SueldoC()<25000):
                        print(self.__arreEmp[i].DatosAyuda())
                else:
                    if(isinstance(self.__arreEmp[i],Eexternos)==True):
                        if(self.__arreEmp[i].SueldoE()<25000):
                            print(self.__arreEmp[i].DatosAyuda())
    def inciso4(self):
          for i in range(self.__indice):
            if(isinstance(self.__arreEmp[i],Eplanta)==True):
                print('Nombre: {}\n'.format(self.__arreEmp[i].getNombre())+'Sueldo {}\n'.format(self.__arreEmp[i].Sueldo())+'Telefono {} \n'.format(self.__arreEmp[i].getTelefono()))
            else:
                if(isinstance(self.__arreEmp[i],Econtratado)==True):   
                     print('Nombre: {}\n'.format(self.__arreEmp[i].getNombre())+'Sueldo {}\n'.format(self.__arreEmp[i].SueldoC())+'Telefono {} \n'.format(self.__arreEmp[i].getTelefono()))
                else:
                    if(isinstance(self.__arreEmp[i],Eexternos)==True):
                         print('Nombre: {}\n'.format(self.__arreEmp[i].getNombre())+'Sueldo {}\n'.format(self.__arreEmp[i].SueldoE())+'Telefono {} \n'.format(self.__arreEmp[i].getTelefono()))