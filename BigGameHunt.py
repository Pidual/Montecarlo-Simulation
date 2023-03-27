from Teams import Team
from archer import Archer
import random

# Empieza los juegos simulados segun la cantidad de juegos asignados
team_1 = Team()
team_2 = Team()


def get_teams():
    return [team_1, team_2]


def get_luckiest_archer():
    luckiest_archer = Archer()
    for archer in team_1.team + team_2.team:
        if archer.get_stacket_luck() > luckiest_archer.get_stacket_luck():
            luckiest_archer = archer
    return luckiest_archer


def restore_attributes(team_1, team_2):
    for archer in team_1.team + team_2.team:
        archer.restore_endurance()
        archer.reset_exp()


def restore_scores(team1, team2):
    team1.reset_score()
    team2.reset_score()


# Empieza los juegos
def start_game(games):
    while games > 0:
        start_rounds(team_1, team_2)
        chose_winning_team(team_1, team_2)
        choose_winning_archer(team_1, team_2)
        restore_attributes(team_1, team_2)
        restore_scores(team_1, team_2)
        games -= 1
    print("\nTeam 1 scores\n")
    for archer in team_1:
        print(str(archer))
    print("\nTeam 2 scores\n")
    for archer in team_2:
        print(str(archer))
    print("\nTEAM 1 SCORE: " + str(team_1))  # Un summary
    print("TEAM 2 SCORE: " + str(team_2))


def chose_winning_team(team_1, team_2):
    if team_1.team_score > team_2.team_score:
        team_1.increment_round_wins()
    elif team_2.team_score > team_1.team_score:
        team_2.increment_round_wins()


def choose_winning_archer(team1, team2):
    winning_archer = Archer()
    for archer in team1.team:
        if archer.get_rounds_won() > winning_archer.get_rounds_won():
            winning_archer = archer
    for archer in team2.team:
        if archer.get_rounds_won() > winning_archer.get_rounds_won():
            winning_archer = archer
    winning_archer.update_games_won()


# Bueno este metodo salió bien cargado
def start_rounds(team_1_local, team_2_local):
    game_rounds = 0
    while game_rounds < 10:
        round_winner = Archer()
        max_score = 0
        for archer in team_1_local:
            archer_current_score = shoot_til_tired(archer, team_1_local, game_rounds)  # guarda el puntaje del arquero
            if archer_current_score > max_score:  # lo compara con el puntaje maximo
                max_score = archer_current_score
                round_winner = archer
        for archer in team_2_local:
            archer_current_score = shoot_til_tired(archer, team_2_local, game_rounds)
            if archer_current_score > max_score:
                max_score = archer_current_score
                round_winner = archer
        raffle_free_shoot(team_1_local, game_rounds)
        raffle_free_shoot(team_2_local, game_rounds)
        round_winner.round_win_reward()
        # Finalizada la ronda se recalcula la suerte de todos los arqueros
        for archer in team_1_local:
            archer.recalculate_luck()
            archer.reset_score()
        for archer in team_2_local:
            archer.recalculate_luck()
            archer.reset_score()
        game_rounds += 1  # Aumenta la ronda


# Recibe un equipo y por medio del que tenga mas suerte dispara un tiro adicional
# Agrega el puntaje al equipo pero no al individual
def raffle_free_shoot(team, game_rounds):
    max_luck = 0
    luckiest_archer = Archer()
    for archer in team:
        if archer.get_luck() > max_luck:
            max_luck = archer.get_luck()
            luckiest_archer = archer
    team.update_team_score(making_shot(luckiest_archer))
    if luckiest_archer.update_streak(game_rounds) == 1:  # Realiza el tiro extra si fueron 3 rondas de suerte seguidas
        print("TIRO EXTRA ")
        team.update_team_score(making_shot(luckiest_archer))
    luckiest_archer.acumulate_luck()


# Dispara tiros hasta que se queda sin resistencia
# Le agrega al final el puntaje individual
def shoot_til_tired(archer, team, game_rounds):
    endurance = archer.get_endurance()
    individual_score = 0
    if archer.especial_endurance_check(game_rounds):
        while endurance > 1:  # Realiza tiro, regresa el puntaje del tiro
            individual_score += making_shot(archer)
            endurance -= 1
    else:
        while endurance > 5:  # Realiza tiro, regresa el puntaje del tiro
            individual_score += making_shot(archer)
            endurance -= 5
    if random.random() < 0.5:
        archer.reduce_endurance(2)
    else:
        archer.reduce_endurance(1)
    archer.update_individual_score(individual_score)  # Establece el score individual en el Archer
    team.update_team_score(individual_score)  # Suma el puntaje del arquero
    return individual_score


# Recibe el arquero, valida el genero y establece las probabilidades
# de los tiros realizados, retorna el Puntaje segun el tiro realizado
def making_shot(archer):
    shot = random.random()
    if archer.get_gender() == "Hombre":
        if shot <= 0.2:
            return 10
        elif 0.2 < shot <= 0.53:
            return 9
        elif 0.53 < shot <= 0.93:
            return 8
        else:
            return 0
    elif archer.get_gender() == "Mujer":
        if shot <= 0.3:
            return 10
        elif 0.3 < shot <= 0.68:
            return 9
        elif 0.68 < shot <= 0.95:
            return 8
        else:
            return 0


def get_gender_rounds_won():
    male_score = 0
    fem_score = 0
    for archer in team_1.team + team_2.team:
        if archer.get_gender() == "Hombre":
            male_score += archer.get_rounds_won()
        else:
            fem_score += archer.get_rounds_won()
    return [male_score, fem_score]
