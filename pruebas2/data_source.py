# data_source.py

def obtener_datos_desde_archivo():
    """
    Esta función recoge los datos desde un archivo.
    Retorna: una única cadena de caracteres.
    """
    with open(' ', 'r') as file:
        return file.read()