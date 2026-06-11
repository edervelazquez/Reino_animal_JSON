from gato import Gato
from gestor_datos import GestorJSON
from vaca import Vaca

def main():
    print("=== INICIANDO RECUPERACIÓN DESDE EL DISCO DURO ===")
    
    # 1. Instanciamos el gestor y traemos los datos planos (diccionarios)
    base_datos = GestorJSON()
    lista_diccionarios = base_datos.cargar_datos()
    
    # Si el archivo estaba vacío o no existía, detenemos el programa elegantemente
    if not lista_diccionarios:
        print("No hay datos para procesar. Ejecuta primero tu script de guardado.")
        return

    # Aquí guardaremos los objetos reales e inteligentes una vez "resucitados"
    lista_objetos_vivos = []

    # 2. El ciclo de Reconstrucción (Mapeo de Diccionario a Objeto)
    for datos in lista_diccionarios:
        
        # Evaluamos el campo 'especie' para saber qué constructor mandar a llamar
        if datos["especie"] == "Gato":
            
            # Extraemos los valores del diccionario y se los pasamos al __init__ de Gato
            nuevo_gato = Gato(
                nombre=datos["nombre"],
                edad=datos["edad"],
                color_pelaje=datos["color_pelaje"]
            )
            lista_objetos_vivos.append(nuevo_gato)
        elif datos["especie"] == "Vaca":
            
            nueva_vaca = Vaca(
                nombre=datos["nombre"],
                edad=datos["edad"],
                raza=datos["raza"]
            )
            # El objeto genérico ahora es una instancia real de la clase Vaca. ¡Ha vuelto a la vida!
           
            lista_objetos_vivos.append(nueva_vaca) 
            

    # =========================================================================
    # 3. DEMOSTRACIÓN POLIMÓRFICA EN LA RAM
    # =========================================================================
    print("\n=== OBJETOS INTELIGENTES EN MEMORIA RAM ===")
    
    for animal in lista_objetos_vivos:
        # Imprimimos el tipo de clase real usando type()
        print(f"-> Detectado un objeto de la clase: {type(animal).__name__}")
        print(f"   Nombre: {animal.obtener_nombre()} | Edad: {animal.obtener_edad()} años")
        
        # Demostración de que recuperó su COMPORTAMIENTO (Método)
        print("   Acción del animal: ", end="")
        animal.hablar()  # Esto imprimirá "¡Miau!" o "¡Moo!"
        print("-" * 40)

if __name__ == "__main__":
    main()