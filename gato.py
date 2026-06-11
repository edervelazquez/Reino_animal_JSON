from animal import Animal

class Gato(Animal):
    def __init__(self, nombre: str, edad: int, color_pelaje: str):
        super().__init__(nombre, edad)
        self.__color_pelaje = color_pelaje

    def hablar(self):
        print("¡Miau!")
    # El traductor: Convierte el objeto en un diccionario compatible con JSON
    def convertir_a_diccionario(self) -> dict:
        return {
            "especie": "Gato",
            "nombre": self.obtener_nombre(),
            "edad": self.obtener_edad(),
            "color_pelaje": self.__color_pelaje
        }
 