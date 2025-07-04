import random
import time

dinero = 0
recompensa_por_pregunta = 100000
comodin_usado1 = False
comodin_usado2 = False
comodin_usado3 = False
sin_comodines = True

comodines_disponibles = {
    "1": True,  # Llamar a un amigo
    "2": True,  # 50/50
    "3": True   # Cambio de pregunta
}

preguntas = {
    
    1: [
        {'pregunta': '¿Cuánto es 2 + 2?',
         'opciones': ['a) 3', 'b) 4', 'c) 5', 'd) 6'],
         'respuesta': 'b'},
        {'pregunta': '¿De qué color es el cielo en un día despejado?',
         'opciones': ['a) Verde', 'b) Azul', 'c) Rojo', 'd) Gris'],
         'respuesta': 'b'}
    ],
    2: [
        {'pregunta': '¿Cuál es la capital de Colombia?',
         'opciones': ['a) Cali', 'b) Medellín', 'c) Bogotá', 'd) Cartagena'],
         'respuesta': 'c'},
        {'pregunta': '¿Cuántos días tiene una semana?',
         'opciones': ['a) 5', 'b) 6', 'c) 7', 'd) 8'],
         'respuesta': 'c'}
    ],
    3: [
        {'pregunta': '¿Qué planeta es conocido como el planeta rojo?',
         'opciones': ['a) Venus', 'b) Marte', 'c) Júpiter', 'd) Saturno'],
         'respuesta': 'b'},
        {'pregunta': '¿Qué animal es conocido como el "rey de la selva"?',
         'opciones': ['a) Tigre', 'b) León', 'c) Elefante', 'd) Oso'],
         'respuesta': 'b'}
    ],
    4: [
        {'pregunta': '¿En qué continente se encuentra Egipto?',
         'opciones': ['a) Europa', 'b) Asia', 'c) África', 'd) Oceanía'],
         'respuesta': 'c'},
        {'pregunta': '¿Cuál es el océano más grande del mundo?',
         'opciones': ['a) Atlántico', 'b) Índico', 'c) Pacífico', 'd) Ártico'],
         'respuesta': 'c'}
    ],
    5: [
        {'pregunta': '¿Quién escribió "Cien años de soledad"?',
         'opciones': ['a) Mario Vargas Llosa', 'b) Julio Cortázar', 'c) Gabriel García Márquez', 'd) Isabel Allende'],
         'respuesta': 'c'},
        {'pregunta': '¿Cuántos lados tiene un hexágono?',
         'opciones': ['a) 5', 'b) 6', 'c) 7', 'd) 8'],
         'respuesta': 'b'}
    ],
    6: [
        {'pregunta': '¿Cuál es el símbolo químico del oro?',
         'opciones': ['a) G', 'b) Au', 'c) Ag', 'd) Or'],
         'respuesta': 'b'},
        {'pregunta': '¿Quién pintó "La Última Cena"?',
         'opciones': ['a) Miguel Ángel', 'b) Rafael', 'c) Leonardo da Vinci', 'd) Botticelli'],
         'respuesta': 'c'}
    ],
    7: [
        {'pregunta': '¿Cuál es el país más grande del mundo por superficie?',
         'opciones': ['a) Canadá', 'b) China', 'c) Estados Unidos', 'd) Rusia'],
         'respuesta': 'd'},
        {'pregunta': '¿Qué científico formuló las leyes del movimiento?',
         'opciones': ['a) Albert Einstein', 'b) Isaac Newton', 'c) Galileo Galilei', 'd) Nikola Tesla'],
         'respuesta': 'b'}
    ],
    8: [
        {'pregunta': '¿En qué año comenzó la Segunda Guerra Mundial?',
         'opciones': ['a) 1935', 'b) 1939', 'c) 1941', 'd) 1945'],
         'respuesta': 'b'},
        {'pregunta': '¿Cuál es la capital de Nueva Zelanda?',
         'opciones': ['a) Auckland', 'b) Wellington', 'c) Christchurch', 'd) Dunedin'],
         'respuesta': 'b'}
    ],
    9: [
        {'pregunta': '¿Quién fue el emperador romano asesinado en los idus de marzo?',
         'opciones': ['a) Nerón', 'b) Julio César', 'c) Augusto', 'd) Calígula'],
         'respuesta': 'b'},
        {'pregunta': '¿Qué país tiene como moneda oficial el “baht”?',
         'opciones': ['a) India', 'b) Corea', 'c) Tailandia', 'd) Vietnam'],
         'respuesta': 'c'}
    ],
    10: [
        {'pregunta': '¿Qué partícula subatómica tiene carga negativa?',
         'opciones': ['a) Protón', 'b) Neutrón', 'c) Electrón', 'd) Positrón'],
         'respuesta': 'c'},
        {'pregunta': '¿Cuál es el número atómico del oxígeno?',
         'opciones': ['a) 6', 'b) 8', 'c) 10', 'd) 12'],
         'respuesta': 'b'}
    ]
}

nombre_jugador = input("Concursante! digita tu nombre: ")
print(f"\n¡Bienvenido/a al juego ¿Quién quiere ser millonario?, {nombre_jugador}!\n")

inicio = input("¿Estás listo para comenzar? (si/no): ").lower()
time.sleep(1)

if inicio == "si":
    print("¡Comenzamos en!")
    for i in range(5, 0, -1):
        print(i)
        time.sleep(1)
    print("¡Empieza el juego!")

    nivel = 1
    while nivel in preguntas:
        pregunta = preguntas[nivel][0]
        correcta = pregunta['respuesta']
        opciones_actuales = pregunta['opciones']
        mostrar_comodines = True

        while True:
            if mostrar_comodines:
                print(f"\n--- Nivel {nivel} ---")

            print(pregunta['pregunta'])
            time.sleep(1)
            for op in opciones_actuales:
                print(op)
                time.sleep(1)

            opcion = input('Escribe "r" para responder o "c" para usar un comodín: ').lower()
            if opcion == "r":
                respuesta = input("Respuesta: ").lower()
                if respuesta == correcta:
                    dinero += recompensa_por_pregunta
                    print("¡Correcto!\n")
                    break
                else:
                    print(f"Incorrecto. La respuesta correcta era '{correcta}'.")
                    print(f"Perdiste en el nivel {nivel}. Ganaste un total de: ${dinero}")
                    exit()
            elif opcion == "c":
                for disponible in comodines_disponibles:
                    if comodines_disponibles[disponible]:
                        sin_comodines = False
                        break
                    if sin_comodines:
                        print("Ya no tienes comodines disponibles.")
                        continue
                    mostrar_comodines=False
                    
                print("Comodines disponibles:")
                if comodines_disponibles["1"]:
                    print("1 - Llamar a un amigo,te dará una respuesta al azar")
                if comodines_disponibles["2"]:
                    print("2 - 50/50, dos incorrectas se van. Queda la buena y la mala.")
                if comodines_disponibles["3"]:
                    print("3 -Cambio de pregunta, ¿Esta te complica? Te daremos otra del mismo nivel.")

                eleccion = input("¿Qué comodín quieres usar? (1, 2 o 3): ")
                if eleccion in comodines_disponibles and comodines_disponibles[eleccion]:
                    comodines_disponibles[eleccion] = False
                    if eleccion == "1":
                        print("Llamando a un amigo...")
                        time.sleep(2)
                        sugerencia = random.choice(['a', 'b', 'c', 'd'])
                        print(f"Tu amigo dice que cree que la respuesta es: '{sugerencia}'")
                        comodin_usado1 = True
                        time.sleep(1)
                        
                    elif eleccion == "2":
                        print("Se eliminan dos respuestas incorrectas")
                        letras = ['a', 'b', 'c', 'd']
                        opciones_incorrectas = letras
                        opciones_incorrectas.remove(correcta)
                        opIncorrecta = random.choice(opciones_incorrectas)
                        print("Opciones después del 50/50:")
                        time.sleep(1)
                        for op in pregunta['opciones']:
                            if op[0] == correcta or op[0] == opIncorrecta:
                                print(op)
                                time.sleep(1)
                        comodin_usado2 = True
                        
                        
                    elif eleccion == "3":
                        print("Cambio de pregunta. Nueva pregunta:")
                        nueva = pregunta
                        while nueva == pregunta:
                            nueva = random.choice(preguntas[nivel])
                        pregunta = nueva
                        correcta = pregunta['respuesta']
                        opciones_actuales = pregunta['opciones']
                        comodin_usado3 = True
                        print("\n¡Pregunta cambiada!")
                        continue  # Vuelve a mostrar la nueva pregunta
                else:
                    print("Comodín no disponible o ya usado.")
            else:
                print("Opción no válida. Intenta de nuevo.")

        nivel += 1

    print(f"\n¡Felicidades, {nombre_jugador}! Completaste todos los niveles. Ganaste un total de: ${dinero}")
    print("Gracias por jugar.")
else:
    print("Juego cancelado :(")
    print("Tal vez la próxima vez. ¡Hasta luego!")










    if comodinesUsados < 3:
                            match comodinRes:
                                case 1:
                                    # Comodín de llamar a un amigo
                                    if comodinesUsado1 == 0:
                                        print("\nHas elegido: Llamar a un amigo. Dame un momento...")
                                        print("\nLlamando a un amigo...\n.....")
                                        RandomAmigo = random.choice(["a", "b", "c", "d"])
                                        print(f"\nTu amigo cree que la respuesta correcta es la '{RandomAmigo}'")
                                        comodinesUsado1 += 1
                                        comodinesUsados += comodinesUsado1
                                        comodinesDisponibles.update({1: 'Llamar a un amigo (Ya usado)'})
                                    elif comodinesUsado1 > 0:
                                        print("\nYa has usado el comodín de llamar a un amigo.")
                                case 2:
                                    # Comodín 50/50
                                    print("Has elegido el comodín 50/50")
                                    if comodinesUsado2 == 0:
                                        # Primero buscamos la opción correcta
                                        opcion_correcta = None
                                        opciones_incorrectas = []
                                        for op in Opciones:
                                            if op[0] == ResCorrect:
                                                opcion_correcta = op
                                            elif op[0] in ['a', 'b', 'c', 'd']:
                                                opciones_incorrectas.append(op)
                                        # Elegimos una incorrecta al azar
                                        opcion_incorrecta = random.choice(opciones_incorrectas)
                                        # Mostramos solo la correcta y una incorrecta
                                        print("\nLas opciones que quedan son:")
                                        print(opcion_correcta)
                                        print(opcion_incorrecta)
                                    comodinesUsado2 += 1
                                    comodinesUsados += comodinesUsado2
                                    comodinesDisponibles.pop(2)
                                case 3:
                                    # Comodín cambiar de pregunta
                                    print("\nHas elegido el comodín cambiar de pregunta.")
                                    comodinesUsado3 += 1
                                    comodinesUsados += comodinesUsado3
                                    comodinesDisponibles.pop(3)
                                case _:
                                    print("Error: opción de comodín no válida.")
                        else:
                            print("Ya has usado todos los comodines.")