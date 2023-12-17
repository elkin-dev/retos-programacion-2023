""" 
 * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
 * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
 * gane cada punto del juego.
 * 
 * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
 * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
 *   15 - Love
 *   30 - Love
 *   30 - 15
 *   30 - 30
 *   40 - 30
 *   Deuce
 *   Ventaja P1
 *   Ha ganado el P1
 * - Si quieres, puedes controlar errores en la entrada de datos.   
 * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos. 
"""
import random

# Definir las puntuaciones posibles en el tenis
scores_game = [0, 15, 30, 40, "Deuce"]


def gameTennis():
    player1 = 0
    player2 = 0

    while True:
        print("Puntajes: Player1 =", player1, ", Player2 =", player2)

        # Verificar si hay un ganador
        if player1 >= 4 and player1 - player2 >= 2:
            print("¡Player1 gana!")
            break
        elif player2 >= 4 and player2 - player1 >= 2:
            print("¡Player2 gana!")
            break

        # Simular un punto aleatorio
        score = random.choice(scores_game)

        # Actualizar los puntajes según el resultado del punto
        if score == "Deuce":
            if player1 == player2 == 3:
                print("Deuce")
        else:
            if score == 40:
                if player1 == player2 == 3:
                    print("Deuce")
                elif player1 > player2:
                    print("Ventaja Player1")
                elif player2 > player1:
                    print("Ventaja Player2")
            elif score == 15:
                player1 += 1
            elif score == 30:
                player2 += 1
            elif score == 40:
                if player1 > player2:
                    print("Player1 gana el juego")
                    break
                elif player2 > player1:
                    print("Player2 gana el juego")
                    break


if __name__ == "__main__":
    gameTennis()
