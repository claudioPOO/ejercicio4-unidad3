import csv
import numpy as np
from Empleado import Empleado
from empleadoPlanta import Eplanta
from empleadoContratado import Econtratado
from empleadoExterno import Eexternos
from datetime import datetime
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
            return self.__arreEmp[i]
        else:
            return 0                       
    def buscaobra(self,obra):
        i=0
        band=0
        while(i<len(self.__arreEmp))and(band==0):
            if(isinstance(self.__arreEmp[i],Eexternos)==True):
                if(self.__arreEmp[i].geTarea().lower()==obra.lower()):
                    fechafincontrato=self.__arreEmp[i].getFinaliza()
                    fechafinContrato=datetime.strptime(fechafincontrato,'%d/%m/%y')
                    fechaactual=datetime.today()
                    if(fechaactual<fechafinContrato):
                        print('Costo de la Obra {}'.format(self.__arreEmp[i].getCostoObra()))
                    else:
                        print('Obra Ya Finalizada')    
                    band=1
                else:
                 i=i+1
            else:
                i=i+1
        if(band==0):
            print('No se encontro la obra')
    def ayuda(self):
        for i in range(self.__indice):
         if(self.__arreEmp[i].Sueldo()<25000):
             band=False
             print(self.__arreEmp[i].MostrarDatos(band))
    def inciso4(self):
          for i in range(self.__indice):
              band=True
              print(self.__arreEmp[i].MostrarDatos(band))
          