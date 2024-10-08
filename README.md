Objetivo del programa:
El programa tiene como propósito interactuar con el usuario para validar si una palabra que ingresa tiene entre 4 y 8 letras. Además, asegura que la palabra solo contenga letras y no esté vacía. El programa permite ingresar palabras continuamente hasta que el usuario decida salir escribiendo "salir".

Estructura del programa:
Función validar palabra:

¿Qué hace?: Se asegura de que la palabra ingresada no esté vacía y que solo contenga letras (sin números ni símbolos).
Mensajes al usuario: Si la palabra no es válida, muestra un mensaje indicando el problema (por ejemplo, si contiene números o está vacía).
¿Por qué es importante?: Evita que el programa falle al trabajar con palabras no válidas.
Función verificar palabra:

¿Qué hace?: Revisa cuántas letras tiene la palabra. Si tiene entre 4 y 8 letras, está bien. Si tiene menos de 4 letras, indica que faltan letras, y si tiene más de 8, dice que sobran letras.
Mensajes al usuario: Dependiendo de la longitud de la palabra, muestra un mensaje adecuado, como "La palabra es correcta" o "Sobran letras".
Función solicitarpalabra:

¿Qué hace?: Controla todo el proceso. Pide al usuario que ingrese una palabra, la valida y luego verifica su longitud. Si el usuario escribe "salir", el programa termina.
Interactividad: Permite que el usuario siga ingresando palabras hasta que quiera salir.
Flujo del programa:
El programa solicita una palabra al usuario.
Valida que la palabra sea correcta (no vacía y sin caracteres no permitidos).
Si la palabra es válida, verifica su longitud y muestra el mensaje correspondiente (si es correcta, corta o larga).
El proceso se repite hasta que el usuario escriba "salir".

Función obtenercoordenadas():

Solicita las coordenadas al usuario. Asegura que el usuario no ingrese 0 en ninguna de las coordenadas, porque si una coordenada es 0, el punto estaría en un eje, no en un cuadrante.
Si el usuario ingresa algo que no es un número o ingresa 0, el programa le pedirá que lo intente de nuevo.
Función identificar cuadrante(x, y):

Usa las coordenadas que se ingresaron y decide en qué cuadrante está el punto.
El plano tiene cuatro cuadrantes:
Cuadrante I: X y Y positivos.
Cuadrante II: X negativo, Y positivo.
Cuadrante III: X y Y negativos.
Cuadrante IV: X positivo, Y negativo.
Función main():

Controla el flujo del programa. Pide las coordenadas al usuario, identifica el cuadrante y luego muestra en cuál está.
