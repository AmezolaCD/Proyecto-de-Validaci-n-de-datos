def validar_palabra(palabra):
    """Valida que la palabra solo contenga letras y no esté vacía."""
    if not palabra:
        print("Error: No se ha ingresado ninguna palabra.")
        return False
    if not palabra.isalpha():
        print("Error: Solo se permiten letras.")
        return False
    return True

def verificar_palabra(palabra):
    """Verifica si la palabra tiene una longitud correcta y muestra los mensajes correspondientes."""
    longitud = len(palabra)
    
    if 4 <= longitud <= 8:
        print(f"La palabra es correcta. Tiene {longitud} letras.")
    elif longitud < 4:
        print(f"Hacen falta letras. Solo tiene {longitud} letras.")
    else:
        print(f"Sobran letras. Tiene {longitud} letras.")

def solicitar_palabra():
    """Solicita una palabra al usuario y la veriica, permitiendo salir con la palabra 'salir'."""
    while True:
        palabra = input("Ingrese una palabra (o escriba 'salir' para terminar): ").strip().lower()

        if palabra == 'salir':
            print("Saliendo del programa...")
            break
        
        if validar_palabra(palabra):
            verificar_palabra(palabra)

# Iniciar el programa
solicitar_palabra()
