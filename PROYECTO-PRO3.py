#ABSTRACCION
class EMPLEADO:
        def __init__(self, cedula, nombre, apellido, edad):
            #ATRIBUTOS
            self.__cedula = cedula
            self.nombre = nombre
            self.apellido = apellido
            self.edad = edad
            #METODOS
        def presentacion(self):
            print(f'SR: {self.apellido} {self.nombre}')
            print(f'CEDULA: {self.__cedula}')
            print(f'EDAD: {self.edad}')
        #ENCAPSULAMIENTO
        def getcedula(self):
            print(self.__cedula)

class DIRECTOR_EJEC(EMPLEADO):
    def __init__(self, cedula, nombre, apellido, edad, puesto, titulos):
           super().__init__(cedula, nombre, apellido, edad)
           self.__puesto= puesto
           self.__titulos= titulos
    
    def presentar_Direc(self):
        print(f'NOMBRE: {self.apellido} {self.nombre}')
        print(f'EDAD: {self.edad} AÑOS')
    #ENCAPSULAMIENTO
    def getpuesto(self):
        print(self.__puesto)
    def gettitulos(self):
        print(self.__titulos)
    pass

                

class GERENTE(EMPLEADO):
    def __init__(self, cedula, nombre, apellido, edad, puesto, Merc):
           super().__init__(cedula, nombre, apellido, edad)
           self.__puesto= puesto
           self.__Merc= Merc
    
    def presentar_Geren(self):
        print(f'NOMBRE: {self.apellido} {self.nombre}')
        print(f'EDAD: {self.edad} AÑOS')
    
    #ENCAPSULAMIENTO
    def getpuesto(self):
        print(self.__puesto)
    def getLog(self):
        print(self.__Merc)
        pass

                

class ASISTENTE(EMPLEADO):
    def __init__(self, cedula, nombre, apellido, edad, puesto, ventas):
           super().__init__(cedula, nombre, apellido, edad)
           self.__puesto= puesto
           self.__ventas= ventas
    
    def presentar_AsisVent(self):
        print(f'NOMBRE: {self.apellido} {self.nombre}')
        print(f'EDAD: {self.edad} AÑOS')
    #ENCAPSULAMIENTO
    def getpuesto(self):
        print(self.__puesto)
    def getvent(self):
        print(self.__ventas)
        pass
        

print(''' 
          ⚠                                      ⚠
          ⚠ BIENVENIDO AL REGISTRO DE LA EMPRESA ⚠
          ⚠ INGRESE SU CEDULA PARA VER SUS DATOS ⚠
          ⚠                                      ⚠
          
            ''')
opcion=int(input())

if opcion==20560464:
            
            EMPLEADO_1 = DIRECTOR_EJEC(20560464, "MANUEL","RAMOS", 21, "DIRECTOR EJECUTIVO", 512) #INSTANCIAR
            EMPLEADO_1.presentar_Direc()
            EMPLEADO_1.getcedula()
            EMPLEADO_1.getpuesto()
            A = input('DECEA SABER EL NUMERO DE TITULOS DE LA EMPRESA EN CIRCULACION DE BOLSA, PRESIONA "SI" PARA SABER Y "NO" PARA SALIR: ')
            if A== 'SI':
                print('LA EMPRESA TIENE ACTUALMENTE:')
                EMPLEADO_1.gettitulos() 
                print('ACCIONES EN CIRCULACION DE BOLSA')


     
elif opcion==21560007:

            EMPLEADO_2 = GERENTE(21560000, "DANIEL", "TABACO", 20, "GERENTE", 471) #INSTANCIAR
            EMPLEADO_2.presentar_Geren()
            EMPLEADO_2.getcedula()
            EMPLEADO_2.getpuesto
            A = input('DECEA SABER EL NUMERO CAJAS DE MERCACIA RECIBIDAS, PRESIONA "SI" PARA SABER Y "NO" PARA SALIR: ')
            if A== 'SI':
                print('LA EMPRESA A RECIBIDO ACTUALMENTE:')
                EMPLEADO_2.getLog() 


elif opcion==21560068:

            EMPLEADO_3 = ASISTENTE(21560001, "SALVADOR", "BELLO", 20, "ASISTENTE DE VENTAS", 780) #INSTANCIAR
            EMPLEADO_3.presentar_AsisVent()
            EMPLEADO_3.getcedula()
            EMPLEADO_3.getpuesto()
            A = input('DECEA SABER EL NUMERO DE VENTAS REALIZADAS, PRESIONA "SI" PARA SABER Y "NO" PARA SALIR: ')
            if A== 'SI':
                print('LA EMPRESA TIENE ACTUALMENTE:')
                EMPLEADO_3.getvent() 
                print('VENTAS REALIZADAS')

                   
else:
            print("Opcion invalida")
pass

