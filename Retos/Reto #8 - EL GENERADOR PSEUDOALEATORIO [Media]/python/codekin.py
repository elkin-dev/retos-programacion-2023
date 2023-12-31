""" 
Crea un generador de números pseudoaleatorios entre 0 y 100.
- No puedes usar ninguna función "random" (o semejante) del lenguaje de programación seleccionado.
Es más complicado de lo que parece... 
"""
import datetime, time

# Xn+1 = (a . Xn + c) mod m
# Xn valor de número inicial
# a, c y m Parámetros constantes del algoritmo
# \mod representa la operación de modulo que devuelve el residuo de la división

def number_random():
    starting_point = 0
    seed = 7

    a, c, m = (
        datetime.datetime.now().microsecond,
        time.time_ns() ** 2,
        time.time_ns(),
    )
    while starting_point < 101:
        result = (a * seed + c) % m

        number_random = result % 101

        seed = result
        print(number_random)
        starting_point += 1


if __name__ == "__main__":
    number_random()
