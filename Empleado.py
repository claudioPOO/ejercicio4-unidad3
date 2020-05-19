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
    def DatosAyuda(self):
        s='Nombre {} \n'.format(self.__Nombre)+'Direccion {}\n'.format(self.__Direccion)+'Dni {}\n'.format(self.__Dni)
        return s