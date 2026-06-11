# Sistema de Gestión - Reino Animal (Módulo de Persistencia)

## Propósito del Proyecto
Este sistema demuestra la aplicación práctica de la Programación Orientada a Objetos en Python. Implementa abstracción, herencia y encapsulamiento, integrando un componente seguro para salvaguardar el estado de los objetos localmente en texto plano.

## Tecnologías Utilizadas
- Lenguaje: Python 3
- Formato de Almacenamiento: JSON (Librería nativa)

## Guía de Instalación y Ejecución
1. Asegúrese de contar con un entorno de ejecución Python 3 instalado.
2. Abra la terminal de comandos directamente en la carpeta raíz del proyecto.
3. Ejecute el punto de entrada de la aplicación: `python main.py`
4. El software generará automáticamente el archivo persistente `granja.json` en este mismo directorio.

## Arquitectura y Buenas Prácticas
* **Principio de Responsabilidad Única (SRP):** La lógica de las entidades del Reino Animal se encuentra completamente aislada de los mecanismos de almacenamiento (GestorJSON).
* **Clean Code:** Se implementaron nombres de métodos explícitos, encapsulamiento riguroso mediante atributos privados y un manejo controlado de errores para evitar cierres inesperados durante la manipulación de archivos del sistema.

## Preguntas de reflexion 
1. **¿Por qué creamos una clase GestorJSON en un archivo separado en lugar de poner el código de guardado dentro de la clase Gato o Animal? ¿Qué principio SOLID se estaría violando si lo hiciéramos ahí?**

- Viola el principio de SRP, lo que significa una sola responsabilidad. En este caso le estariamos dando dos responsabilidades distintas a la clase gato o animal, para no violar este principio se crea una clase destinada para guardar los archivos. Si tuvieramos que cambiar de base de datos solo tendriamos que modificar la clase GestorJson, sin tocar nada de una clase que no tiene nada que ver con archivos.

2. **Si vuelves a ejecutar el archivo main.py cambiando el nombre del gato en el código, ¿qué le sucede a la información que ya estaba guardada en el archivo granja.json?** Explica brevemente por qué pasa esto.

- El nombre que le pongamos aparecera nuevo, ya que en el metodo guardar_datos se especifica que se cree o guarde en modo escritura pura "w". Lo que hace que la informacion anterior desaparezca del archivo y contemple lo que escribimos en su lugar, lo que hace que el GestorJSON solo refleje lo que existe en lista de la ultima ejecucion.
