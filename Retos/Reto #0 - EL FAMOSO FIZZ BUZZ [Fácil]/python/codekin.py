<<<<<<< HEAD
"""
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 """


def fizzbuzz(start, end):
    for number in range(start, end + 1):
        if number % 3 == 0 and number % 5 == 0:
            print(f"{number} fizzbuzz")
        elif number % 3 == 0:
            print(f"{number} fizz")
        elif number % 5 == 0:
            print(f"{number} buzz")
        else:
            print(number)

if __name__ == "__main__":
    fizzbuzz(1, 100)
=======
"""
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 """


def fizzbuzz(start, end):
    for number in range(start, end + 1):
        if number % 3 == 0 and number % 5 == 0:
            print(f"{number} fizzbuzz")
        elif number % 3 == 0:
            print(f"{number} fizz")
        elif number % 5 == 0:
            print(f"{number} buzz")
        else:
            print(number)

if __name__ == "__main__":
    fizzbuzz(1, 100)
>>>>>>> 0bd83db74 (Reto #0 FIZZBUZZ)
