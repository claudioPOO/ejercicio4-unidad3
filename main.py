
import os
from claseMenu import Menu
from ManejadorEmpleado import ManejaEmpleados
from empleadoContratado import Econtratado





if __name__ == '__main__':
   input()
   cantidad=int(input('Cantidad de Empleados que posee la Empresa: '))
   hora=int(input('Valor por hora de empleados contratados '))
   Econtratado.Valorxhora=hora
   ME=ManejaEmpleados(cantidad)   
   ME.cargarEmpleados() 
   menu = Menu()
   salir = False
   while not salir:
        print("\n------------Menu------------\n1. Registrar Horas\n2. Total de tarea\n3. Ayuda\n4. Calcular Sueldo\n0. Salir")
        op = int(input('Ingrese una opcion: '))
        os.system('cls') 
        menu.opcion(op,ME)
        salir = op == 0
