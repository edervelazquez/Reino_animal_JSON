from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nombre: str, edad: int):
        self.__nombre = nombre
        self.__edad = edad

    @abstractmethod
    def hablar(self):
        pass

    # Métodos para exponer atributos privados al momento de serializar
    def obtener_nombre(self) -> str:
        return self.__nombre

    def obtener_edad(self) -> int:
        return self.__edad 