from gato import Gato
from gestor_datos import GestorJSON
from vaca import Vaca 

def main():
    # 1. Instanciamos el objeto en la memoria RAM
    mi_gato = Gato("Garfield", 5, "Naranja")
    mi_gato2 = Gato("Con Botas", 3, "Azul")
    mi_vaca = Vaca("Daisy", 4, "Holstein")
    # 2. Preparamos las estructuras de datos limpias
    lista_animales = [mi_gato, mi_gato2, mi_vaca]
    datos_a_guardar = []
    
    # 3. Ciclo de transformación (Serialización de objetos a diccionarios)
    for animal in lista_animales:
        datos_a_guardar.append(animal.convertir_a_diccionario())

    # 4. Delegamos la persistencia física al gestor especializado
    base_datos = GestorJSON()
    base_datos.guardar_datos(datos_a_guardar)

if __name__ == "__main__":
    main()
