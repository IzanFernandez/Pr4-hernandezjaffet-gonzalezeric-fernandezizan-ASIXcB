# crazy_words.py

import random

def desordenar_palabra(palabra):
    """
    Desordena las letras internas de una palabra, manteniendo la primera y la última.
    """
    if len(palabra) <= 3:
        return palabra
    medio = list(palabra[1:-1])
    random.shuffle(medio)
    return palabra[0] + ''.join(medio) + palabra[-1]

def desordenar_frase(frase):
    """
    Aplica desordenar_palabra a cada palabra de una frase.
    """
    palabras = frase.split()
    palabras_desordenadas = [desordenar_palabra(palabra) for palabra in palabras]
    return ' '.join(palabras_desordenadas)