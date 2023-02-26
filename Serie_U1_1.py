#Declaracion de la cles Persona y sus atributos
class Persona: #Aqui se hace la clase nueva.
    #Propiedades/Atributos
    nombre = " "
    apellido = "Zepeda Bello"
    DNI = 1876156

    #Metodos
    def esMayorDeEdad(self):
        print(f'Es mayor de edad: TRUE')

    def esMenorDeEdad(self):
        print(f'Es menor de edad: FALSE')

    def metodo(self):
        print(f'La persona se llama {Constructor.nombre}, sus apellidos son {Constructor.apellido} tiene {constructor} años y su DNI es {Constructor.DNI}')

    def metodo2(self):
        print(f'No se pueden mostrar datos personales')

Constructor = Persona()
Constructor.nombre = "Chava"

constructor = input("¿Cuantos años tiene?")

if constructor >= "18":
    Constructor.esMayorDeEdad()
    Constructor.metodo() 

else:
    Constructor.esMenorDeEdad()
    Constructor.metodo2()