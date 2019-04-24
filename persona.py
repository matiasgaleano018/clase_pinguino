
class Persona:
    edad = 18
    nombre = None
    def __init__(self, la_edad, el_nombre):
        self.edad = la_edad
        self.nombre = el_nombre
        print("Hola soy ", self.nombre,"y tengo ",self.edad," anhos")

    def get_edad(self):
        return self.edad
    
    def set_edad(self, cantidad):
        self.edad = cantidad

    def reducir_edad(self):
        self.edad = self.edad - 1

fulano = Persona(18, "Juan")
