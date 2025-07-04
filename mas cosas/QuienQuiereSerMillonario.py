import random
import time

preguntas = {
    1: [
        {'pregunta': '¿De qué color es el cielo en un día despejado?',
         'opciones': ['a) Verde', 'b) Azul', 'c) Rojo', 'd) Amarillo', 'e) Comodines'],
         'respuesta': 'b',
         'Locate': '1'},
        {'pregunta': '¿Cuántas patas tiene un perro?',
         'opciones': ['a) 2', 'b) 6', 'c) 4', 'd) 8', 'e) Comodines'],
         'respuesta': 'c',
         'Locate': '2'}
    ],
    2: [
        {'pregunta': '¿Qué planeta es conocido como el "planeta rojo"?',
         'opciones': ['a) Venus', 'b) Marte', 'c) Júpiter', 'd) Saturno', 'e) Comodines'],
         'respuesta': 'b',
         'Locate': '1'},
        {'pregunta': '¿Cuántos lados tiene un triángulo?',
         'opciones': ['a) 4', 'b) 2', 'c) 3', 'd) 5', 'e) Comodines'],
         'respuesta': 'c',
         'Locate': '2'}
    ],
    3: [
        {'pregunta': '¿En qué continente se encuentra Egipto?',
         'opciones': ['a) Asia', 'b) Europa', 'c) América', 'd) África', 'e) Comodines'],
         'respuesta': 'd',
         'Locate': '1'},
        {'pregunta': '¿Qué instrumento mide la temperatura?',
         'opciones': ['a) Barómetro', 'b) Termómetro', 'c) Anemómetro', 'd) Telescopio', 'e) Comodines'],
         'respuesta': 'b',
         'Locate': '2'}
    ],
    4: [
        {'pregunta': '¿Quién escribió “Don Quijote de la Mancha”?',
         'opciones': ['a) Gabriel García Márquez', 'b) Miguel de Cervantes', 'c) Lope de Vega', 'd) Mario Vargas Llosa', 'e) Comodines'],
         'respuesta': 'b',
         'Locate': '1'},
        {'pregunta': '¿Qué gas es esencial para la respiración humana?',
         'opciones': ['a) Dióxido de carbono', 'b) Nitrógeno', 'c) Oxígeno', 'd) Helio', 'e) Comodines'],
         'respuesta': 'c',
         'Locate': '2'}
    ],
    5: [
        {'pregunta': '¿Cuál es el idioma oficial de Brasil?',
         'opciones': ['a) Español', 'b) Portugués', 'c) Inglés', 'd) Francés', 'e) Comodines'],
         'respuesta': 'b',
         'Locate': '1'},
        {'pregunta': '¿Qué país tiene forma de bota en el mapa de Europa?',
         'opciones': ['a) Francia', 'b) España', 'c) Italia', 'd) Alemania', 'e) Comodines'],
         'respuesta': 'c',
         'Locate': '2'}
    ],
    6: [
        {'pregunta': '¿Qué tipo de célula no tiene núcleo definido?',
         'opciones': ['a) Animal', 'b) Vegetal', 'c) Procariota', 'd) Eucariota', 'e) Comodines'],
         'respuesta': 'c',
         'Locate': '1'},
        {'pregunta': '¿Qué científico formuló las leyes del movimiento?',
         'opciones': ['a) Galileo Galilei', 'b) Albert Einstein', 'c) Isaac Newton', 'd) Nikola Tesla', 'e) Comodines'],
         'respuesta': 'c',
         'Locate': '2'}
    ],
    7: [
        {'pregunta': '¿En qué año se firmó la Declaración de Independencia de los Estados Unidos?',
         'opciones': ['a) 1789', 'b) 1776', 'c) 1804', 'd) 1750', 'e) Comodines'],
         'respuesta': 'b',
         'Locate': '1'},
        {'pregunta': '¿Qué órgano del cuerpo humano produce la insulina?',
         'opciones': ['a) Hígado', 'b) Estómago', 'c) Páncreas', 'd) Riñón', 'e) Comodines'],
         'respuesta': 'c',
         'Locate': '2'}
    ],
    8: [
        {'pregunta': '¿Qué filósofo escribió "La República"?',
         'opciones': ['a) Sócrates', 'b) Aristóteles', 'c) Platón', 'd) Pitágoras', 'e) Comodines'],
         'respuesta': 'c',
         'Locate': '1'},
        {'pregunta': '¿Qué compuesto es conocido como la "molécula de la herencia"?',
         'opciones': ['a) ARN', 'b) ATP', 'c) ADN', 'd) Glucosa', 'e) Comodines'],
         'respuesta': 'c',
         'Locate': '2'}
    ],
    9: [
        {'pregunta': '¿Cuál es el nombre de la teoría que unifica la mecánica cuántica y la gravedad?',
         'opciones': ['a) Teoría de cuerdas', 'b) Relatividad general', 'c) Mecánica cuántica', 'd) Termodinámica', 'e) Comodines'],
         'respuesta': 'a',
         'Locate': '1'},
        {'pregunta': '¿Cuál es el significado del número "e" en matemáticas?',
         'opciones': ['a) Base del logaritmo natural', 'b) Unidad imaginaria', 'c) Valor de la gravedad', 'd) Número irracional de pi', 'e) Comodines'],
         'respuesta': 'a',
         'Locate': '2'}
    ],
    10: [
        {'pregunta': '¿Qué científico propuso el principio de incertidumbre en física cuántica?',
         'opciones': ['a) Schrödinger', 'b) Bohr', 'c) Heisenberg', 'd) Dirac', 'e) Comodines'],
         'respuesta': 'c',
         'Locate': '1'},
        {'pregunta': '¿Cuál es el teorema que afirma que no hay algoritmo general que decida la verdad de todos los enunciados matemáticos?',
         'opciones': ['a) Teorema de Gödel', 'b) Teorema de Cantor', 'c) Teorema de Euclides', 'd) Teorema de Zorn', 'e) Comodines'],
         'respuesta': 'a',
         'Locate': '2'}
    ]
}


RepIni = 1
Dinero=0

while RepIni == 1:
    print("¿Desea Jugar?")
    print("1. Si")
    print("2. NO")
    Inicio = int(input())

    match Inicio:
        case 1:
            RepIni=0
            NomJugador=input("Okey, Vamos a jugar!, Participante digite su nombre: ")
            print(f"\n Bienvenido {NomJugador} a Quien Quiere ser Millonario!!!")
            print("\n las reglas del juego son las siguientes:")
            print("\n- te daremos 10 preguntas una mas dificil que la anterior")
            print("\n- Si Respondes bien, ganaras Dinero, si Respondes mal lo perderas todo")
            print("pero Hey no todo es malo, Tu tienes 3 comodines que podras utilizar")
            print("en cualquier momento de las preguntas, BUENA SUERTE!!!!!")

            Nivel=1
            while Nivel in preguntas:
                # Elegimos una pregunta aleatoria para el nivel actual
                preguntRandom = random.randint(0,1)
                pregunta = preguntas[Nivel][preguntRandom]
                ResCorrect = pregunta['respuesta']
                Opciones = pregunta['opciones']
                # Diccionario de comodines disponibles
                comodinesDisponibles = {
                    1: 'Llamar a un amigo (Llamará a un amigo y él te dirá una opción al azar)',
                    2: '50/50 (Elimina 2 opciones y deja una verdadera y una falsa)',
                    3: 'Cambiar de pregunta (Cambia la pregunta a otra del mismo nivel)'
                }
                # Variables para controlar el uso de comodines
                comodinesUsado1 = 0
                comodinesUsado2 = 0
                comodinesUsado3 = 0
                comodinesUsados = 0
                Ciclo = True
                opciones_5050 = [] 
                while Ciclo:
                    # Mostramos la pregunta y las opciones al jugador
                    print(f"\n ---------------- Pregunta {Nivel} --------------- \n")
                    print(pregunta['pregunta']+"\n")
                    if opciones_5050:
                        print("\n(Comodín 50/50 activado)")
                        for op in opciones_5050:
                            print(op)
                            # Mostrar opcion e) comodines
                        for op in Opciones:
                            if op[0] == 'e':
                                print(op)
                    else:
                        for op in Opciones:
                            print(op)
                    OpcionResp = input("\nDigite la respuesta correcta o elija 'e' para los comodines: ").lower()

                    # Si el comodín 50/50 está activo y el usuario elige una opción eliminada
                    if opciones_5050 == True:
                        letras_validas = [op[0] for op in opciones_5050]
                        if OpcionResp not in letras_validas and OpcionResp != 'e':
                            print("\nEsa opción fue eliminada por el comodín 50/50. Elige una de las opciones que quedan.")
                            continue
                    # Verificamos la respuesta del jugador
                    if OpcionResp == ResCorrect:
                        Nivel += 1
                        if Dinero >= 200000:
                            Dinero *= 5
                        else:
                            Dinero += 100000
                        print(f"\nRespuesta correcta! Has ganado {Dinero} pesos.\n")
                        
                        if Nivel > 10:
                            print(f"\nFelicidades {NomJugador}, has respondido todas las preguntas correctamente y has ganado {Dinero} pesos!")
                            Ciclo = False
                        else:
                            # Seleccionamos una nueva pregunta aleatoria para el siguiente nivel
                            preguntRandom = random.randint(0,1)
                            pregunta = preguntas[Nivel][preguntRandom]
                            ResCorrect = pregunta['respuesta']
                            Opciones = pregunta['opciones']
                            opciones_5050 = None

                    elif OpcionResp == 'e':
                        print("\nHas elegido comodines. Los comodines disponibles son:")
                        for key in comodinesDisponibles:
                            print(f"\n{key}. {comodinesDisponibles[key]}")

                        comodinRes = int(input("Elige uno de los 3 comodines: "))

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
                                    print("\nHas elegido el comodín 50/50")
                                    if comodinesUsado2 == 0:
                                        opcion_correcta = None
                                        opciones_incorrectas = []
                                        for op in Opciones:
                                            if op[0] == ResCorrect:
                                                opcion_correcta = op
                                            elif op[0] in ['a', 'b', 'c', 'd']:
                                                opciones_incorrectas.append(op)
                                        opcion_incorrecta = random.choice(opciones_incorrectas)
                                        opciones_5050 = [opcion_correcta, opcion_incorrecta]
                                        print("\nLas opciones que quedan son:")
                                        for op in opciones_5050:
                                            print(op)
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
                                    print("\nError: opción de comodín no válida.")
                        else:
                            print("\nYa has usado todos los comodines.")
                    elif OpcionResp != Opciones:
                        print("\nLa opción digitada no es válida. Por favor, elige una de las opciones disponibles.")
                    else:
                        print("\nRespuesta incorrecta. Has perdido todo tu dinero.")
                        DineroAComulado= Dinero
                        Ciclo = False
                if Ciclo == False:
                    if Dinero == 0:
                        print(f"\nLo siento {NomJugador}, has perdido. Tu dinero acumulado es: {DineroAComulado} pesos.")
                    break

        case 2:
            print("Esta bien, para la proxima sera!")
            RepIni=0
        case _:
            print("ERROR!! Opcion digitada no existe")