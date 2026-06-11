from animal import Animal 
class Vaca(Animal):
    def __init__(self, nombre: str, edad: int, raza: str):
        super().__init__(nombre, edad)
        self.__raza = raza

    def hablar(self):
        print("¡Muu!")

    def convertir_a_diccionario(self) -> dict:
        return {
            "especie": "Vaca",
            "nombre": self.obtener_nombre(),
            "edad": self.obtener_edad(),
            "raza": self.__raza
        }