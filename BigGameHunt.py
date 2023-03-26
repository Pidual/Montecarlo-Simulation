from Teams import Team
import random

# Empieza los juegos simulados segun la cantidad de juegos asignados
def start_game(team_1, team_2):
    games = 60
    while games > 0:
        restore_endurance(team_1, team_2)
        start_rounds(team_1, team_2)
        games -= 1
    print("\nTeam 1 scores\n")
    for archer in team_1:
        print(str(archer))
    print("\nTeam 2 scores\n")
    for archer in team_2:
        print(str(archer))
    print("\nTEAM 1 SCORE: " + str(team_1))  # Un summary
    print("TEAM 2 SCORE: " + str(team_2))


def restore_endurance(team_1, team_2):
    for archer in team_1:
        archer.restore_endurance()
    for archer in team_2:
        archer.restore_endurance()


# Bueno este metodo salio bien cargado juas juas juas
def start_rounds(team_1_local, team_2_local):
    round = 0
    max_score = 0
    while round < 10:
        round_winner = None
        for archer in team_1_local:
            archer_current_score = shoot_til_tired(archer, team_1_local, round)  # guarda el puntaje del arquero
            if archer_current_score > max_score:  # lo compara con el puntaje maximo
                max_score = archer_current_score
                round_winner = archer
        for archer in team_2_local:
            archer_current_score = shoot_til_tired(archer, team_2_local, round)
            if archer_current_score > max_score:
                max_score = archer_current_score
                round_winner = archer
        max_score = 0
        raffle_free_shoot(team_1_local, round)
        raffle_free_shoot(team_2_local, round)
        round_winner.round_win_reward()
        # Finalizada la ronda se recalcula la suerte de todos los arqueros
        # Finalizada la ronda se recalcula la experiencia de todos los arqueros
        for archer in team_1_local:
            archer.recalculate_luck()
            archer.reset_exp()
        for archer in team_2_local:
            archer.recalculate_luck()
            archer.reset_exp()
        round += 1  # Aumenta la ronda


# Recibe un equipo y por medio del que tenga mas suerte dispara un tiro adicional
# Agrega el puntaje al equipo pero no al individual
def raffle_free_shoot(team, round):
    max_luck = 0
    luckiest_archer = None
    for archer in team:
        if archer.luck > max_luck:
            max_luck = archer.luck
            luckiest_archer = archer
    team.update_team_score(making_shot(luckiest_archer))
    if luckiest_archer.update_streak(round) == 1:  # Realiza el tiro extra si fueron 3 rondas de suerte seguidas
        team.update_team_score(making_shot(luckiest_archer))


# Dispara tiros hasta que se queda sin resistencia
# Le agrega al final el puntaje individual
def shoot_til_tired(archer, team, round):
    endurance = archer.endurance
    individual_score = 0
    if archer.especial_endurance_check(round):
        while endurance > 1:  # Realiza tiro, regresa el puntaje del tiro
            individual_score += making_shot(archer)
            endurance -= 1
    else:
        while endurance > 5:  # Realiza tiro, regresa el puntaje del tiro
            individual_score += making_shot(archer)
            endurance -= 5
    if random.random() < 0.5:
        archer.endurance -= 2
    else:
        archer.endurance -= 1
    archer.update_individual_score(individual_score)  # Establece el score individual en el Archer
    team.update_team_score(individual_score)  # Suma el puntaje del arquero
    return individual_score


# Recibe el arquero, valida el genero y establece las probabilidades
# de los tiros realizados, retorna el Puntaje segun el tiro realizado
def making_shot(archer):
    shot = random.random()
    if archer.gender == 0:
        if shot <= 0.2:
            return 10
        elif 0.2 < shot <= 0.53:
            return 9
        elif 0.53 < shot <= 0.93:
            return 8
        else:
            return 0
    elif archer.gender == 1:
        if shot <= 0.3:
            return 10
        elif 0.3 < shot <= 0.68:
            return 9
        elif 0.68 < shot <= 0.95:
            return 8
        else:
            return 0


start_game(Team(), Team())  # INICIA EL JUEGO miau miau
