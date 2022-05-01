import re
from getpass import getpass

class Email:
    #Atributos
    __idCuenta = ''
    __dominio = ''
    __tipoDom = ''
    __contrasenia = ''

    #Metodos
    def __init__(self):
        self.__idCuenta = ''
        self.__dominio = ''
        self.__tipoDom = ''
        self.__contrasenia = ''

    def retornaEmail(self):
        return '{}@{}.{}'.format(self.__idCuenta,self.__dominio,self.__tipoDom)

    def getDominio(self):
        return self.__dominio

    def crearCuenta(self,correo,contra=''):
        #Validar correo
        if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$',correo.lower()):
            #Divido elementos
            i = correo.find('@')
            j = correo[i:].find('.')
            print(correo[:i])
            print(correo[i+1:i+j])
            print(correo[i+j+1:])

            self.__idCuenta = correo[:i]
            self.__dominio = correo[i+1:i+j]
            self.__tipoDom = correo[i+j+1:]

            print('Su correo es: {}'.format(self.retornaEmail()))
            if contra== '':
                print('Configure su contrasenia ')
                self.__setcontra()
            else:
                self.__contrasenia = contra
            print ("La cuenta se creo con exito!")
            return False #No hubo error retorno false
        else:
            print ("Correo electronico incorrecto, reintente.")
            return True #Hubo un error retorno true

    def __setcontra(self):
        contra = getcontra('Ingrese contrasenia: ')
        contra2 = getcontra('Reingrese contrasenia: ')
        while(contra != contra2):
            print('Las password no coincide, reinente.')
            contra = getcontra('Ingrese contrasenia: ')
            contra2 = getcontra('Reingrese contrasenia: ')
        print('contrasenia configurada con exito!')
        self.__contrasenia = contra

    def changecontra(self):
        oldcontra = getcontra('Ingrese su contrasenia actual FIN para salir: ')
        while(oldcontra != self.__contrasenia and oldcontra.lower() != 'fin'):
            print('Su contrasenia es incorrecta.')
            oldcontra = getcontra('Ingrese su contrasenia actual o FIN para salir: ')
        if(oldcontra.lower() != 'fin'):
            print('Configure su nueva contrasenia: ')
            self.__setcontra()
