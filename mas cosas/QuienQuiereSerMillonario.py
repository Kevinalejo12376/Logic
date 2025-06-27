import random
import time

preguntas = {
    1: [
        {'pregunta': '¿De qué color es el cielo en un día despejado?',
         'opciones': ['a) Verde', 'b) Azul', 'c) Rojo', 'd) Amarillo', 'e) Comodines'],
         'respuesta': 'b'},
        {'pregunta': '¿Cuántas patas tiene un perro?',
         'opciones': ['a) 2', 'b) 6', 'c) 4', 'd) 8', 'e) Comodines'],
         'respuesta': 'c'}
    ],
    2: [
        {'pregunta': '¿Qué planeta es conocido como el "planeta rojo"?',
         'opciones': ['a) Venus', 'b) Marte', 'c) Júpiter', 'd) Saturno', 'e) Comodines'],
         'respuesta': 'b'},
        {'pregunta': '¿Cuántos lados tiene un triángulo?',
         'opciones': ['a) 4', 'b) 2', 'c) 3', 'd) 5', 'e) Comodines'],
         'respuesta': 'c'}
    ],
    3: [
        {'pregunta': '¿En qué continente se encuentra Egipto?',
         'opciones': ['a) Asia', 'b) Europa', 'c) América', 'd) África', 'e) Comodines'],
         'respuesta': 'd'},
        {'pregunta': '¿Qué instrumento mide la temperatura?',
         'opciones': ['a) Barómetro', 'b) Termómetro', 'c) Anemómetro', 'd) Telescopio', 'e) Comodines'],
         'respuesta': 'b'}
    ],
    4: [
        {'pregunta': '¿Quién escribió “Don Quijote de la Mancha”?',
         'opciones': ['a) Gabriel García Márquez', 'b) Miguel de Cervantes', 'c) Lope de Vega', 'd) Mario Vargas Llosa', 'e) Comodines'],
         'respuesta': 'b'},
        {'pregunta': '¿Qué gas es esencial para la respiración humana?',
         'opciones': ['a) Dióxido de carbono', 'b) Nitrógeno', 'c) Oxígeno', 'd) Helio', 'e) Comodines'],
         'respuesta': 'c'}
    ],
    5: [
        {'pregunta': '¿Cuál es el idioma oficial de Brasil?',
         'opciones': ['a) Español', 'b) Portugués', 'c) Inglés', 'd) Francés', 'e) Comodines'],
         'respuesta': 'b'},
        {'pregunta': '¿Qué país tiene forma de bota en el mapa de Europa?',
         'opciones': ['a) Francia', 'b) España', 'c) Italia', 'd) Alemania', 'e) Comodines'],
         'respuesta': 'c'}
    ],
    6: [
        {'pregunta': '¿Qué tipo de célula no tiene núcleo definido?',
         'opciones': ['a) Animal', 'b) Vegetal', 'c) Procariota', 'd) Eucariota', 'e) Comodines'],
         'respuesta': 'c'},
        {'pregunta': '¿Qué científico formuló las leyes del movimiento?',
         'opciones': ['a) Galileo Galilei', 'b) Albert Einstein', 'c) Isaac Newton', 'd) Nikola Tesla', 'e) Comodines'],
         'respuesta': 'c'}
    ],
    7: [
        {'pregunta': '¿En qué año se firmó la Declaración de Independencia de los Estados Unidos?',
         'opciones': ['a) 1789', 'b) 1776', 'c) 1804', 'd) 1750', 'e) Comodines'],
         'respuesta': 'b'},
        {'pregunta': '¿Qué órgano del cuerpo humano produce la insulina?',
         'opciones': ['a) Hígado', 'b) Estómago', 'c) Páncreas', 'd) Riñón', 'e) Comodines'],
         'respuesta': 'c'}
    ],
    8: [
        {'pregunta': '¿Qué filósofo escribió "La República"?',
         'opciones': ['a) Sócrates', 'b) Aristóteles', 'c) Platón', 'd) Pitágoras', 'e) Comodines'],
         'respuesta': 'c'},
        {'pregunta': '¿Qué compuesto es conocido como la "molécula de la herencia"?',
         'opciones': ['a) ARN', 'b) ATP', 'c) ADN', 'd) Glucosa', 'e) Comodines'],
         'respuesta': 'c'}
    ],
    9: [
        {'pregunta': '¿Cuál es el nombre de la teoría que unifica la mecánica cuántica y la gravedad?',
         'opciones': ['a) Teoría de cuerdas', 'b) Relatividad general', 'c) Mecánica cuántica', 'd) Termodinámica', 'e) Comodines'],
         'respuesta': 'a'},
        {'pregunta': '¿Cuál es el significado del número "e" en matemáticas?',
         'opciones': ['a) Base del logaritmo natural', 'b) Unidad imaginaria', 'c) Valor de la gravedad', 'd) Número irracional de pi', 'e) Comodines'],
         'respuesta': 'a'}
    ],
    10: [
        {'pregunta': '¿Qué científico propuso el principio de incertidumbre en física cuántica?',
         'opciones': ['a) Schrödinger', 'b) Bohr', 'c) Heisenberg', 'd) Dirac', 'e) Comodines'],
         'respuesta': 'c'},
        {'pregunta': '¿Cuál es el teorema que afirma que no hay algoritmo general que decida la verdad de todos los enunciados matemáticos?',
         'opciones': ['a) Teorema de Gödel', 'b) Teorema de Cantor', 'c) Teorema de Euclides', 'd) Teorema de Zorn', 'e) Comodines'],
         'respuesta': 'a'}
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

            Niv=1
            for niv in preguntas:
                preguntRandom= random.randint(0,1)
                pregunta = preguntas[Niv][preguntRandom]
                ResCorrect= pregunta['respuesta']
                Opciones=pregunta['opciones']
                comodines=True

                while True:
                    print(f"\n ---------------- Pregunta {Niv}--------------- \n")
                    print(pregunta['pregunta'])
                    for op in Opciones:
                        print(op)
                    
                    OpcionResp=input("Digite la respuesta correcta o eliga los comodines: ").lower()

                    if OpcionResp == ResCorrect:
                        if Dinero >= 200000:
                            Dinero=Dinero*Dinero
                        else:
                            Dinero+=100000
                    print(Dinero)
        case 2:
            print("Esta bien, para la proxima sera!")
            RepIni=0
        case _:
            print("ERROR!! Opcion digitada no existe")
