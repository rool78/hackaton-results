import random

options = ["Piedra", "Papel", "Tijeras"]

# El resultado de salida son las siguientes String
#'Empate!'
#'Ganaste!'
#'Perdiste!'
def quienGana(player, ai):
    player = player.lower()
    ai = ai.lower()

    if player == ai:
        return 'Empate!'
    elif player == 'piedra' and ai == 'tijeras':
        return 'Ganaste!'
    elif player == 'papel' and ai == 'piedra':
        return 'Ganaste!'
    elif player == 'tijeras' and ai == 'papel':
        return 'Ganaste!'
    else:
        return 'Perdiste!'

# Entry Point
def Game():
    print("Bienvenido al juego de Piedra, papel y tijera")
    print("1. Piedra, 2. Papel, 3. Tijera")
    player = input("Elije su opción: ")
    player = int(player)

    print("Has elegido... " + options[player-1])
    ai = random.randrange(1, 4)
    print('Tu maquina a seleccionado...' + options[ai-1] + '!')

    player = options[player-1].lower()
    ai = options[ai-1].lower()

    winner = quienGana(player, ai)

    print(winner)

