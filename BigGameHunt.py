from Teams import Team
import random


# Empieza los juegos simulados segun la cantidad de juegos asignados
def start_game(team_1, team_2):
    games = 40
    while games > 0:
        restore_endurance(team_1, team_2)
        start_rounds(team_1, team_2)
        games -= 1
    print("TEAM 1 SCORE: " + str(team_1.team_score))
    print("TEAM 2 SCORE: " + str(team_2.team_score))


def restore_endurance(team_1, team_2):
    for archer in team_1:
        archer.restore_endurance()
    for archer in team_2:
        archer.restore_endurance()


def start_rounds(team_1_local, team_2_local):
    round = 0
    while round < 10:
        for archer in team_1_local:
            shoot_til_tired(archer, team_1_local)
        for archer in team_2_local:
            shoot_til_tired(archer, team_2_local)
        raffle_free_shoot(team_1_local, round)
        raffle_free_shoot(team_2_local, round)
        #Finalizada la ronda se recalcula la suerte de todos los arqueros
        for archer in team_1_local:
            archer.recalculate_luck()
        for archer in team_2_local:
            archer.recalculate_luck()
        round += 1


# Recibe un equipo y por medio del que tenga mas suerte dispara un tiro adicional
# Agrega el puntaje al equipo pero no al individual
def raffle_free_shoot(team, round):
    max_luck = 0
    luckiest_archer = None
    for archer in team:
        if archer.luck > max_luck:
            max_luck = archer.luck
            luckiest_archer = archer
            print(str(archer))
    team.update_team_score(making_shot(luckiest_archer))

    if luckiest_archer.update_streak(round) == 1:  # Realiza el tiro extra si fueron 3 rondas de suerte seguidas
        team.update_team_score(making_shot(luckiest_archer))


# Dispara tiros hasta que se queda sin resistencia
# Le agrega al final el puntaje individual
def shoot_til_tired(Archer, team):
    print("\n############################################################\n")
    print("la resistencia inicial es " + str(Archer.endurance))
    endurance = Archer.endurance
    individual_score = 0
    while endurance > 5:  # Realiza tiro, regresa el puntaje del tiro
        individual_score += making_shot(Archer)
        print("RESISTENCIA: " + str(endurance))
        endurance -= 5
    if random.random() < 0.5:
        Archer.endurance -= 2
    else:
        Archer.endurance -= 1
    print("Score: ", individual_score)
    # Establece el score individual en el Archer
    Archer.update_individual_score(individual_score)
    team.update_team_score(individual_score)
    print("Score Individual: ", Archer.individual_score)
    print("la resistencia bajo a " + str(Archer.endurance))


# Recibe el arquero, valida el genero y establece las probabilidades
# de los tiros realizados, retorna el Puntaje segun el tiro realizado
def making_shot(archer):
    shot = random.random()
    if archer.gender == 0:
        print("Hommbre")
        if shot <= 0.2:
            print("Central", shot)
            return 10
        elif 0.2 < shot <= 0.53:
            print("Intermedia", shot)
            return 9
        elif 0.53 < shot <= 0.93:
            print("Exterior", shot)
            return 8
        else:
            print("Error", shot)
            return 0
    elif archer.gender == 1:
        print("Mujer")
        if shot <= 0.3:
            print("Central", shot)
            return 10
        elif 0.3 < shot <= 0.68:
            print("Intermedia", shot)
            return 9
        elif 0.68 < shot <= 0.95:
            print("Exterior", shot)
            return 8
        else:
            print("Error", shot)
            return 0


start_game(Team(), Team())  # INICIA EL JUEGO miau miau
