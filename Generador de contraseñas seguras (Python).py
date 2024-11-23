import random
import string

def mostrar_menu():
    """Muestra las opciones disponibles para generar una contraseña."""
    print("\n--- Generador de Contraseñas Seguras ---")
    print("1. Generar contraseña (opciones personalizadas)")
    print("2. Salir")

def obtener_opciones():
    """Obtiene las preferencias del usuario para personalizar la contraseña."""
    while True:
        try:
            longitud = int(input("Introduce la longitud de la contraseña (mínimo 8): "))
            if longitud < 8:
                print("La longitud mínima es de 8 caracteres. Intenta nuevamente.")
                continue
            incluir_mayusculas = input("¿Incluir letras mayúsculas? (s/n): ").strip().lower() == 's'
            incluir_numeros = input("¿Incluir números? (s/n): ").strip().lower() == 's'
            incluir_simbolos = input("¿Incluir símbolos? (s/n): ").strip().lower() == 's'
            return longitud, incluir_mayusculas, incluir_numeros, incluir_simbolos
        except ValueError:
            print("Por favor, introduce un número válido.")

def generar_contrasena(longitud, incluir_mayusculas, incluir_numeros, incluir_simbolos):
    """Genera una contraseña basada en las opciones proporcionadas."""
    caracteres = string.ascii_lowercase  # Letras minúsculas
    if incluir_mayusculas:
        caracteres += string.ascii_uppercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_simbolos:
        caracteres += string.punctuation

    if not caracteres:
        raise ValueError("Debe incluir al menos un tipo de carácter en la contraseña.")

    # Genera la contraseña de forma aleatoria
    return ''.join(random.choice(caracteres) for _ in range(longitud))

def main():
    """Función principal para ejecutar el generador de contraseñas."""
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1/2): ").strip()
        if opcion == "1":
            opciones = obtener_opciones()
            try:
                contrasena = generar_contrasena(*opciones)
                print(f"\nTu contraseña segura es: {contrasena}")
            except ValueError as e:
                print(f"Error: {e}")
        elif opcion == "2":
            print("¡Gracias por usar el generador de contraseñas!")
            break
        else:
            print("Opción no válida. Por favor, selecciona 1 o 2.")

if __name__ == "__main__":
    main()
