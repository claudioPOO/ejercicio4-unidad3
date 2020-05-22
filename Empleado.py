class Empleado:
    __Dni=0
    __Nombre=''
    __Direccion=''
    __Telefono=''
    def __init__(self,Dni,Nombre,Direccion,Telefono):
        self.__Dni=int(Dni)
        self.__Nombre=Nombre
        self.__Direccion=Direccion
        self.__Telefono=Telefono
    def getNombre(self):
        return self.__Nombre
    def getDni(self):
        return self.__Dni
    def getDireccion(self):
        return self.__Direccion
    def getTelefono(self):
        return self.__Telefono
    def MostrarDatos(self,band):
        if(band==True):
            print('Nombre: {}'.format(self.__Nombre))
            print('Telefono {} '.format(self.__Telefono))
        else:
            print('Nombre: {}'.format(self.__Nombre))
            print('Dni {}'.format(self.__Dni))
            print('Direccion {} '.format(self.__Direccion))