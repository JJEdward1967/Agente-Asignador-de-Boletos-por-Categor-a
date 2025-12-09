# Script: agente asignador de boletos para un evento
# Comentarios y mensajes en español para quien aprende Python

def calcular_boletos(categoria):
    """
    Devuelve la cantidad de boletos según la categoría.
    Usa condicionales if / elif / else.
    Si la categoría no es válida devuelve 0 e imprime un mensaje de error.
    """
    cat = categoria.lower().strip()
    if cat == "standard":
        return 2
    elif cat == "standard_plus":
        return 4
    elif cat == "platino":
        return 10
    else:
        # Mensaje de error para categoría no válida
        print(f"Categoría '{categoria}' no válida. No se asignaron boletos.")
        return 0

def imprimir_boletos(categoria, cantidad):
    """
    Imprime cada boleto usando un bucle for.
    Ejemplo: Boleto 1 - categoría platino
    Al final muestra la cantidad total de boletos generados para esa categoría.
    """
    if cantidad <= 0:
        print("No hay boletos para mostrar.\n")
        return

    # Imprimir cada boleto numerado
    for i in range(1, cantidad + 1):
        print(f"Boleto {i} - categoría {categoria}")

    # Mensaje final con total de boletos generados
    print(f"Total de boletos generados para la categoría '{categoria}': {cantidad}\n")

def main():
    """
    Bucle principal que pide la categoría al usuario hasta que escriba 'salir'.
    """
    print("Agente asignador de boletos. Escribe 'salir' para terminar.\n")
    while True:
        entrada = input("Ingrese la categoría (standard, standard_plus, platino): ").strip()
        if entrada.lower() == "salir":
            print("Saliendo del programa. ¡Hasta luego!")
            break

        # Calcular y mostrar los boletos para la categoría ingresada
        cantidad = calcular_boletos(entrada)
        imprimir_boletos(entrada, cantidad)

if __name__ == "__main__":
    main()