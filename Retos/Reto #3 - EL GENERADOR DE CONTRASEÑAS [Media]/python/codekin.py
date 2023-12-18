""" 
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
"""
from string import (
    ascii_lowercase as chars_lowercase,
    ascii_uppercase as chars_uppercase,
    digits as chars_digits,
    punctuation as chars_punctuation,
)
from random import choice


from random import choice
import string


def generatePasswords(length = 8,
    include_uppercase=True,
    include_lowercase=True,
    include_digits=True,
    include_punctuation=True,
):
   

    chars_passwords = []

    if include_uppercase:
        chars_passwords += string.ascii_uppercase
    if include_lowercase:
        chars_passwords += string.ascii_lowercase
    if include_digits:
        chars_passwords += string.digits
    if include_punctuation:
        chars_passwords += string.punctuation

    passwords = []
    while True:
        char_random = choice(chars_passwords)
        if len(passwords) < length:
            passwords.append(char_random)
        if len(passwords) == length:
            break

    clean_passwords = "".join(passwords)
    print(f"{clean_passwords}")


if __name__ == "__main__":
    generatePasswords(
        # length=16,
        include_uppercase=True,
        include_punctuation=False,
        include_lowercase=True,
        include_digits=True,
    )
