word = input("Buenos días/tardes/noches estimado usuario! Ahora mismo estás en el diccionario de slang juvenil, a continuación, deberás escribir una palabra o sigla que no entiendas (¡Asegúrate de escribirla con mayúsculas!) e intentaremos definirla por ti, ten en cuenta que son muchas palabras y siglas y es posible que aún no se encuentren disponibles en el diccionario!: ")

meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso, se siente una vergüenza ajena",
            "LOL": "Las siglas son: <Laugh Out Loud> que significa <Reírse a carcajadas/Reírse en voz alta> se usa como respuesta común a algo gracioso.",
            "ROFL": "Las siglas son: <Rolling On The Floor Laughing> que significa <Rodando en el piso, riéndome> una respuesta a una broma.",
            "SHEESH": "Ligera desaprobación, expresión de sorpresa usada positiva y/o negativamente, también se utiliza cuando alguien hace algo impresionante.",
            "CREEPY": "Aterrador, siniestro, tenebroso; cuando este se atribuye a una persona se refiere a alguien con caracterísitcas depravadas, pervertidas, enfermizas, etc.",
            "AGGRO": "Ponerse agresivo/enojado, a veces utilizado como unidad de medida para definir dificultad o agresividad de cierto personaje o enemigo en algún videojuego.",
            "LMAO": "Las siglas son <Laughing My Ass Off> cuyo significado literal es un poco más grosero que el usual, siendo este <Cagándome de risa>, es bastante auto explicativo.",
            "IRL": "<In Real Life>, refiriéndose a <En la vida real> por ejemplo: <If [...] happened IRL...>, <Si [...] pasara en la vida real...>",
            "FYI": "<For Your Information>, para abrir una aclaración; <Para tu información...>",
            "BTW": "<By The Way>, mencionar algo faltante o agregar a una sentencia; <Por cierto...>",
            "OMW": "<On My Way>, la palabra <Way> en este caso tiene un significado distinto y se usa para decir que estás en camino.>",
            "GG": "<Good Game>, se usa al finalizar una partida en la gran mayoría de juegos multijugador, <Buen juego/partida> quizás en ocasiones utilizado para halagar la habilidad del jugador/es contrincante/s.",
            "IDK": "<I Don't Know>, que significa <No lo sé> aclara la falta de conocimiento sobre algún tema o cuestión.",
            "IKR": "<I Know Right>, estar de acuerdo o apoyar algo que se dijo, de cierta manera. <Lo sé, verdad?>",
            "IMO": "<In My Opinion>, es bastante claro, se refiere al momento en que darás tu opinión subjetiva y no intentas establecer un hecho.",
            }

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("Los sentimos, al parecer aún no definimos la palabra que estás buscando :(")

for i in range(5):
    repeat = input("Hagámoslo de nuevo, escribe otra palabra :)")
    if repeat in meme_dict.keys():
        print(meme_dict[repeat])
    else:
        print("Los sentimos, al parecer aún no definimos la palabra que estás buscando :(")
