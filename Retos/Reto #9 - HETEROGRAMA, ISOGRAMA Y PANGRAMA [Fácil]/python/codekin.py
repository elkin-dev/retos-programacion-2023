import re

""" 
Crea 3 funciones, cada una encargada de detectar si una cadena de
texto es un heterograma, un isograma o un pangrama.
- Debes buscar la definición de cada uno de estos términos.

"""
# heterograma: Cada letra aparece solo una vez
# isograma:  Ninguna letra se repite en la palabra
# pangrama: frase que contiene todas las letras del alfabeto al menos una vez
# word = "The quick brown fox jumps over a lazy dog."
word = "murciélago"


def is_heterograma(word):
    letters_repeat = re.findall(r"(\w).*\1", word, re.I)
    words_repeat = re.findall(r"\b(\w+)\b.*\b\1\b", word, re.I)

    if not (letters_repeat or words_repeat):
        return True
    else:
        return False


def is_isograma(word):
    letters_repeat = re.findall(r"(\w).*\1", word, re.I)
    if letters_repeat:
        return False
    else:
        return True


def is_pangrama(word):
    word = word.lower()
    letras = set(re.findall(r"[a-z]", word))
    return len(letras) == 26


if __name__ == "__main__":
    if is_pangrama(word):
        print("Es un pangrama")
    else:
        print("No es un pangrama")
    
    if is_heterograma(word):
        print("Es un heterograma")
    else:
        print("No es un heterograma")
        
    if is_isograma(word):
        print("Es un isograma")
    else:
        print("No es un isograma")
