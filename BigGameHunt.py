from archer import Archer

import random


# Empieza los juegos simulados segun la cantidad de juegos asignados

def start_game(team_1, team_2):
    games = 40
    while games > 0:
        restore_endurance(team_1, team_2)
        start_rounds(team_1, team_2)
        games -= 1


def restore_endurance(team_1, team_2):
    for archer in team_1:
        archer.restore_endurance()
    for archer in team_2:
        archer.restore_endurance()


def start_rounds(team_1, team_2):
    rounds = 10
    while rounds > 0:
        for Archer in team_1:
            shoot_til_tired(Archer)
        for Archer in team_1:
            shoot_til_tired(Archer)
        rounds -= 1

def raffle_free_schoot(team):
    print()

def shoot_til_tired(Archer):
    print("\n############################################################\n")
    print("la resistencia inicial es " + str(Archer.endurance))
    endurance = Archer.endurance
    individual_score = 0
    while endurance > 5:
        # Realiza tiro, regresa el puntaje del tiro
        individual_score += making_shot(Archer)
        print("RESISTENCIA: "+str(endurance))
        endurance -= 5 
    if random.random() < 0.5:
        Archer.endurance -= 2
    else:
        Archer.endurance -= 1
    print("Score: ", individual_score)
    # Establece el score individual en el Archer
    Archer.update_individual_score(individual_score)
    print("Score Individual: ", Archer.individual_score)
    print("la resistencia bajo a " + str(Archer.endurance))


# Recibe el arquero, valida el genero y establece las probabilidades
# de los tiros realizados, retorna el Puntaje segun el tiro realizado
def making_shot(Archer):
    shot = random.random()
    if Archer.gender == 0:
        print("Hommbre")
        if shot <= 0.2:
            print("Central", shot)
            return 10
        elif shot > 0.2 and shot <= 0.53:
            print("Intermedia", shot)
            return 9
        elif shot > 0.53 and shot <= 0.93:
            print("Exterior", shot)
            return 8
        else:
            print("Error", shot)
            return 0
    elif Archer.gender == 1:
        print("Mujer")
        if shot <= 0.3:
            print("Central", shot)
            return 10
        elif shot > 0.3 and shot <= 0.68:
            print("Intermedia", shot)
            return 9
        elif shot > 0.68 and shot <= 0.95:
            print("Exterior", shot)
            return 8
        else:
            print("Error", shot)
            return 0

team_1_score = 0
team_2_score = 0
# Crea un equipo con 5 arqueros
team_1 = [Archer(), Archer(), Archer(), Archer(), Archer()]
# Crea el equipo 2 con 5 Arqueros
team_2 = [Archer(), Archer(), Archer(), Archer(), Archer()]

print("Equipo 1")

for Archer in team_1:
    print("Resistencia: "+str(Archer.endurance) + " EXP: "+str(Archer.experiencia) +
          " Genero: " + str(Archer.gender)+" Suerte: "+str(Archer.suerte))

print("Equipo 2")
for Archer in team_2:
    print("Resistencia: "+str(Archer.endurance) + " EXP: "+str(Archer.experiencia) +
          " Genero: " + str(Archer.gender)+" Suerte: "+str(Archer.suerte))

startgame(team_1, team_2) #INICIA EL JUEGO miau miau
