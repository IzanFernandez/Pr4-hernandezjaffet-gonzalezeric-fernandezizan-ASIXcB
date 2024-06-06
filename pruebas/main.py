# main.py

from data_source import obtener_datos_desde_teclado
from crazy_words import desordenar_frase

def main():
    frase = obtener_datos_desde_teclado()
    frase_desordenada = desordenar_frase(frase)
    print("Frase original:", frase)
    print("Frase desordenada:", frase_desordenada)

if __name__ == "__main__":
    main()
