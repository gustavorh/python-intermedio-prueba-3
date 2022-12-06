import random
jugando = True
while jugando:
    print("juego de 'piedra', 'papel','tijeras'.") 
    ordenador = random.choice(["piedra","papel","tijeras"])
    jugador = input("elige una opcion:")
    if jugador == "piedra":
        if ordenador == "piedra":
            print("ordenador elige 'piedra'. Empate.")
        elif ordenador == "papel":
            print("ordenador elige 'papel'. papel envuelve piedra. Pierdes.")
        else:
            print("ordenador elige 'tijeras'. piedra rompe tijeras. ganas.")
    elif jugador == "papel":
        if ordenador == "piedra":
            print("ordenador elige 'piedra. papel envuelve piedra. Ganas.")
        elif ordenador == "papel":
            print("ordenador elige 'papel', Empate.")
        else:
            print("ordenador elige 'tijeras'. tijeras cortan papel. Pierdes.")
    elif jugador == "tijeras":
        if ordenador == "piedra":
            print("ordenador elige 'piedra. piedra rompe tijeras. Pierdes.")
        elif ordenador == "papel":
            print("ordenador elige 'papel', tijeras cortan papel. Ganas.")
        else:
            print("ordenador elige 'tijeras'. Empate.")
    else:
        print("no has elegido una opcion correcta")

    seguir = ""
    while seguir != "no" or seguir !="si":
        seguir = input ("quieres volver a jugar(si/no):")
        if seguir == "no":
            jugando = False
            break
        elif seguir == "si":
            break
        else:
            print("no entiendo que quieres decir...")


