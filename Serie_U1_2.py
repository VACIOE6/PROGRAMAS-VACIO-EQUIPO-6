class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def setnombre(self):
        self.nombre = nombre

    def setedad(self):
        self.edad = edad

    def getnombre(self):
        return self.nombre
    
    def getedad(self):
        return self.edad
    
    def presentar(self):
        print(f'su nombre es {self.nombre} y su edad es {self.edad}\n')

    def mayoredad(self):
        if self.edad >= 18:
            print("True")
        
        else:
            print("False")

    def mayoredades(self):
        if persona1.edad >= persona2.edad:
            return print(f'{persona1.nombre} es mayor y {persona2.nombre} es menor')
        else:
            return print(f'{persona2.nombre} es mayor y {persona1.nombre} es menor')

persona1 = Persona("JAVIER PEREZ LOPEZ", 17)
persona1.presentar()

persona2 = Persona("ALONSO RAMIREZ JAIBO", 40)
persona2.presentar()

persona1.mayoredad()
persona2.mayoredad()
persona1.mayoredades()
persona2.mayoredades()