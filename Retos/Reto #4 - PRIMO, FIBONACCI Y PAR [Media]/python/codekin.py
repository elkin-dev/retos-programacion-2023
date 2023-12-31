""" 
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
"""
from math import sqrt


def checkNumber(n):
    def primo(n):
        if n > 1 and all(n % i != 0 for i in range(2, int(sqrt(n)) + 1)):
            return True
        return False

    def par(n):
        if n != 0 and n % 2 == 0:
            return True
        return False

    def fibonacci(n):
        a, b = 0, 1
        for _ in range(n):
            if a == n:
                return True
            a, b = b, a + b
        return False

    is_prime = primo(n)
    is_even = par(n)
    is_fibonacci = fibonacci(n)

    result = f"{n} es "

    if is_prime:
        result += "primo"
    else:
        result += "no es primo"

    if is_fibonacci:
        result += ", fibonacci"
    else:
        result += ", no es fibonacci"

    if is_even:
        result += " y es par"
    else:
        result += " y es impar"

    print(result)


numbers = 7
if __name__ == "__main__":
    checkNumber(numbers)
