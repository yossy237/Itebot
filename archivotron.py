# Función que busca una palabra en un arreglo fijo
def busca_arreglo(busca):
    print(f"Buscando en arreglo: {busca}")
    arreglo_palabras = ["rojo", "verde", "azul", "negro", "morado"]
    for item in arreglo_palabras:
        if busca.lower() == item.lower():  # Comparación sin distinguir mayúsculas
            print("Palabra encontrada en el arreglo")
            return "encontrada en el arreglo"
    return "No se encontro en el arreglo"


# Función que busca una palabra en un archivo dado
def busca_in_file(busca, filename):
    try:
        with open(filename, 'r') as f:
            for line in f:
                if busca.lower().strip() == line.lower().strip():
                    print(f"{busca} encontrada en {filename}")
                    return True
    except FileNotFoundError:
        print(f"Archivo {filename} no encontrado.")
    return False


# Función que analiza la palabra usando el arreglo y luego los archivos
def analiza_texto(busca):
    # Buscar primero en arreglo
    resultado_arreglo = busca_arreglo(busca)
    if resultado_arreglo == "encontrada en el arreglo":
        return "Palabra encontrada en el arreglo"

    # Buscar en los archivos de texto
    if busca_in_file(busca, 'palabras.txt'):
        return "Palabra encontrada en palabras.txt"
    elif busca_in_file(busca, 'groserias.txt'):
        return "Palabra encontrada en groserias.txt"
    elif busca_in_file(busca, 'palabras_especiales.txt'):
        return "Palabra encontrada en palabras_especiales.txt"
    
    return "Palabra no encontrada en ningún archivo"


# Función que el bot usará
def busca_con_archivos(busca):
    return analiza_texto(busca)
