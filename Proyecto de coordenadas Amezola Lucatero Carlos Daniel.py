def obtener_coordenadas():
    """Solicita las coordenadas X e Y al usuario y verifica que no sean 0."""
    while True:
        try:
            x = float(input("Ingrese la coordenada X (no puede ser 0): "))
            y = float(input("Ingrese la coordenada Y (no puede ser 0): "))
            
            if x == 0 or y == 0:
                print("Error: Ninguna de las coordenadas puede ser 0. Inténtelo de nuevo.")
            else:
                return x, y  # Coordenadas válidas, retornarlas
        except ValueError:
            print("Error: Debe ingresar valores numéricos. Inténtelo de nuevo.")

def identificar_cuadrante(x, y):
    """Identifica en qué cuadrante está el punto (x, y)."""
    if x > 0 and y > 0:
        return "Cuadrante I"
    elif x < 0 and y > 0:
        return "Cuadrante II"
    elif x < 0 and y < 0:
        return "Cuadrante III"
    elif x > 0 and y < 0:
        return "Cuadrante IV"

def main():
    """Función principal que controla el flujo del programa."""
    print("Identificación del cuadrante de un punto en el plano cartesiano.")
    
    # Obtener las coordenadas válidas del usuario
    x, y = obtener_coordenadas()
    
    # Identificar y mostrar el cuadrante
    cuadrante = identificar_cuadrante(x, y)
    print(f"El punto ({x}, {y}) se encuentra en el {cuadrante}.")

# Ejecutar el programa
if __name__ == "__main__":
    main()
