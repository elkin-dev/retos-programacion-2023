from random import choice


def star_game():
    while True:
        print("⚔️ 🎰 Es hora de que inicie el juego 🎲🪓")
        print("¡Estas son las opciones que puedes elegir!")
        print("1. piedra 🪨\n2. papel 📄\n3. tijera ✂️\n4. lagarto 🦎\n5. spock 🖖")

        combat_game()

        # Preguntar al jugador si desea volver a jugar
        restart = input("¿Quieres jugar de nuevo? (s/n): ").lower()
        if restart != "s":
            break


def combat_game():
    option = {1: "🪨", 2: "📄", 3: "✂️", 4: "🦎", 5: "🖖"}
    pointsplayer1 = 0
    pointsplayer2 = 0
    
    while pointsplayer1 < 2 and pointsplayer2 < 2:
        player1 = int(input("Ingresa tu opción: "))

        if player1 not in option:
            print("Opción no válida. Ingresa un número del 1 al 5.")
            continue

        player2 = choice(list(option.keys()))

        print(f"Tú: {option[player1]} vs jugador 2: {option[player2]}")

        if player1 == player2:
            print("¡Empate!")
        else:
            if (
                (player1 == 1 and player2 == 3)
                or (player1 == 3 and player2 == 2)
                or (player1 == 2 and player2 == 1)
                or (player1 == 1 and player2 == 4)
                or (player1 == 4 and player2 == 5)
                or (player1 == 5 and player2 == 3)
                or (player1 == 3 and player2 == 4)
                or (player1 == 4 and player2 == 2)
                or (player1 == 2 and player2 == 5)
                or (player1 == 5 and player2 == 1)
            ):
                pointsplayer1 += 1
                print(
                    f"Ganas el combate. Puntos: Tú {pointsplayer1}, jugador 2, {pointsplayer2}"
                )
            else:
                pointsplayer2 += 1
                print(
                    f"Pierdes el combate. Puntos: Tú {pointsplayer1}, jugador 2, {pointsplayer2}"
                )

    if pointsplayer1 == 2:
        print("¡Ganaste la serie!")
    elif pointsplayer2 == 2:
        print("¡La jugador 2, ganó la serie!")


if __name__ == "__main__":
    star_game()
