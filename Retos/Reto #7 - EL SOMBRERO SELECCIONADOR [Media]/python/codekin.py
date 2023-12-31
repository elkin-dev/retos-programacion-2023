from random import randint
from collections import Counter

""" 
Crea un programa que simule el comportamiento del sombrero seleccionador del
universo mágico de Harry Potter.
- De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
- Cada pregunta tendrá 4 respuestas posibles (también a selecciona una a través de terminal).
- En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que
  coloque al alumno en una de las 4 casas de Hogwarts (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
- Ten en cuenta los rasgos de cada casa para hacer las preguntas y crear el algoritmo seleccionador.
  Por ejemplo, en Slytherin se premia la ambición y la astucia. 
"""

question_hat = [
    {
        "Pregunta": "¿Qué valor aprecias más?",
        "Respuestas": {
            "Valentía": "Gryffindor",
            "Sabiduría": "Ravenclaw",
            "Lealtad": "Hufflepuff",
            "Ambición": "Slytherin",
        },
    },
    {
        "Pregunta": "¿Cuál es tu mayor miedo?",
        "Respuestas": {
            "Soledad": "Ravenclaw",
            "Ignorancia": "Hufflepuff",
            "Fracaso": "Gryffindor",
            "Traición": "Slytherin",
        },
    },
    {
        "Pregunta": "¿Qué tipo de magia te atrae más?",
        "Respuestas": {
            "Magia oscura": "Slytherin",
            "Magia defensiva": "Gryffindor",
            "Magia curativa": "Hufflepuff",
            "Magia transformadora": "Ravenclaw",
        },
    },
    {
        "Pregunta": "¿Qué animal te representa mejor?",
        "Respuestas": {
            "León": "Gryffindor",
            "Águila": "Ravenclaw",
            "Tejón": "Hufflepuff",
            "Serpiente": "Slytherin",
        },
    },
    {
        "Pregunta": "¿Prefieres aprender a volar en escoba o estudiar criaturas mágicas?",
        "Respuestas": {
            "Volar en escoba": "Gryffindor",
            "Estudiar criaturas mágicas": "Hufflepuff",
            "Ambos": "Ravenclaw",
            "Ninguno": "Slytherin",
        },
    },
    {
        "Pregunta": "¿Qué cualidad personal es más importante para ti?",
        "Respuestas": {
            "Honestidad": "Gryffindor",
            "Inteligencia": "Ravenclaw",
            "Valentía": "Hufflepuff",
            "Astucia": "Slytherin",
        },
    },
    {
        "Pregunta": "¿En qué tipo de aventuras te gustaría participar?",
        "Respuestas": {
            "Aventuras emocionantes": "Gryffindor",
            "Aventuras intelectuales": "Ravenclaw",
            "Aventuras desafiantes": "Hufflepuff",
            "Aventuras misteriosas": "Slytherin",
        },
    },
    {
        "Pregunta": "¿Cuál es tu asignatura favorita en la escuela de magia?",
        "Respuestas": {
            "Defensa contra las Artes Oscuras": "Gryffindor",
            "Pociones": "Slytherin",
            "Transformaciones": "Ravenclaw",
            "Cuidado de Criaturas Mágicas": "Hufflepuff",
        },
    },
    {
        "Pregunta": "¿Cómo reaccionarías ante una injusticia?",
        "Respuestas": {
            "Lucharía contra ella": "Gryffindor",
            "Buscaría una solución diplomática": "Ravenclaw",
            "Me adaptaría": "Hufflepuff",
            "Me vengaría": "Slytherin",
        },
    },
    {
        "Pregunta": "¿Qué tipo de hechizo prefieres?",
        "Respuestas": {
            "Hechizos ofensivos": "Slytherin",
            "Hechizos defensivos": "Ravenclaw",
            "Hechizos curativos": "Hufflepuff",
            "Hechizos de transformación": "Gryffindor",
        },
    },
]

print("¡Bienvenido al Sombrero Seleccionador de Hogwarts!")


def chosen_answer():
    question_random = randint(0, len(question_hat) - 1)

    print(question_hat[question_random]["Pregunta"])
    for index, answer in enumerate(question_hat[question_random]["Respuestas"]):
        letter_enum = chr(ord("a") + index)
        print(f"{letter_enum}) {answer}")

    response_user = input("Seleccione una opcion: ").lower()
    print()

    to_number = {"a": 0, "b": 1, "c": 2, "d": 3}
    dit_options = question_hat[question_random]["Respuestas"]

    values_option = list(dit_options.values())
    keys_option = list(dit_options.keys())

    if response_user in to_number:
        associated_value = to_number[response_user]
        print(f"Haz seleccionado, {keys_option[associated_value]}")
        return values_option[associated_value]
    else:
        print("¡Error! Por favor, elige entre a, b, c o d.")
        return None


def selected_house():
    save_response = []
    accumulator, repetitions = 1, 5

    while accumulator < repetitions + 1:
        save_response.append(chosen_answer())
        accumulator += 1

        response = input("¿Quieres seguir? (presiona Enter para continuar, 'n' para finalizar): ")
        print()
        if response.lower() == "n":
            print("¡Has finalizado las preguntas!")
            break

    counter_result = Counter(save_response)
    house_result = counter_result.most_common(1)

    if house_result:
        print(f"¡Oh sí! Ya sé a qué casa deberías ir, {house_result[0][0]}")
    else:
        print("No se han recopilado respuestas.")


if __name__ == "__main__":
    selected_house()
