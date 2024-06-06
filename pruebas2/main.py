# main.py

from data_source import obtener_datos_desde_archivo
from crazy_words import desordenar_frase

def main():
    frase = obtener_datos_desde_archivo('')
    frase_desordenada = desordenar_frase(frase)
    with open('output.txt', 'w') as file:
        file.write("Frase original: " + frase + "\n")
        file.write("Frase desordenada: " + frase_desordenada + "\n")

if __name__ == "__main__":
    main()