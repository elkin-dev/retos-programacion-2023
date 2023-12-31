""" 
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 """


def languageHacker():
    text = input("input:  ")
    leet_dict = {
        "a": "4",
        "A": "4",
        "e": "3",
        "E": "3",
        "l": "1",
        "L": "1",
        "o": "0",
        "O": "0",
        "t": "7",
        "T": "7",
        "b": "8",
        "B": "8",
        "c": "<",
        "C": "<",
        "d": "|)",
        "D": "|)",
        "f": "|=",
        "F": "|=",
        "g": "9",
        "G": "9",
        "h": "|-|",
        "H": "|-|",
        "i": "1",
        "I": "1",
        "j": "_|",
        "J": "_|",
        "k": "|<",
        "K": "|<",
        "m": "/\\/\\",
        "M": "/\\/\\",
        "n": "/\\/",
        "N": "/\\/",
        "p": "|°",
        "P": "|°",
        "q": "0_",
        "Q": "0_",
        "r": "|2",
        "R": "|2",
        "s": "5",
        "S": "5",
        "u": "|_|",
        "U": "|_|",
        "v": "\\/",
        "V": "\\/",
        "w": "\\/\\/",
        "W": "\\/\\/",
        "x": "><",
        "X": "><",
        "y": "`/",
        "Y": "`/",
        "z": "2",
        "Z": "2",
    }
    leet_text = "".join(leet_dict.get(char, char) for char in text)
    return f"output: {leet_text}"


if __name__ == "__main__":
    print(languageHacker())
