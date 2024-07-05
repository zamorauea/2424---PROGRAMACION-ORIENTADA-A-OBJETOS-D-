class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")

# Creación de objetos
persona1 = Persona("Manuel", 33)
persona1.saludar()

persona2 = Persona("Estefania", 25)
persona2.saludar()

