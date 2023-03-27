import random


class Archer:
    _rounds_won = 0
    _games_won = 0
    _gender = None  # 0 para hombre y 1 para mujer
    _max_endurance = None  # la resistencia que es definitiva
    _endurance = None  # 35 ± 10
    _exp = None  # Entero 10
    _luck = None  # 1 a 3
    _stacked_luck = None
    _individual_score = 0  # Puntaje individual
    _ultra_stacket_individual_score = 0
    _first_lucky_round = None
    _second_lucky_round = None
    _last_lucky_round = None
    _endurance_bonus_round_activated = None

    def __init__(self):  # aca para que se creen pseudo aleatoriamente
        # Determina el género con el metodo montecarlo 0.5 de chance cada género
        self._especial_endurance = None
        self._stacked_luck = 0
        ri = random.random()
        if ri < 0.5:
            self._gender = "Hombre"
        else:
            self._gender = "Mujer"
        # Resistencia 35 ± 10
        if ri < 0.5:
            fleeting_endurance = 35 - random.randint(1, 10)
        else:
            fleeting_endurance = 35 + random.randint(1, 10)
        # Flotante XD
        self._luck = random.uniform(1, 3)
        self._endurance = fleeting_endurance
        self._exp = 10
        self._individual_score = 0
        self._max_endurance = fleeting_endurance

    def update_individual_score(self, score):
        self._ultra_stacket_individual_score += score
        self._individual_score += score

    def get_luck(self):
        return self._luck

    def restore_endurance(self):
        self._endurance = self._max_endurance

    def get_gender(self):
        return self._gender

    def recalculate_luck(self):
        self._luck = random.uniform(1, 3)

    def especial_endurance_check(self, game_rounds):
        if self._exp >= 19 and self._endurance_bonus_round_activated is None:
            self._endurance_bonus_round_activated = game_rounds
            return True
        elif self._exp >= 19 and self._endurance_bonus_round_activated + 1 == game_rounds:
            return True
        else:
            return False

    def get_rounds_won(self):
        return self._rounds_won

    def get_stacket_luck(self):
        return self._stacked_luck

    def reset_score(self):
        self._individual_score = 0

    def reduce_endurance(self, num):
        self._endurance -= num

    def get_endurance(self):
        return self._endurance

    def acumulate_luck(self):
        self._stacked_luck += 1

    # Actualiza la racha de lanzamientos extra al llegar a 3 se reinicia
    def update_streak(self, game_rounds):
        if self._first_lucky_round is None:
            self._first_lucky_round = game_rounds
            return 0
        elif self._second_lucky_round is None:
            if game_rounds - self._first_lucky_round == 1:
                self._second_lucky_round = game_rounds
                return 0
            else:
                self._first_lucky_round = game_rounds
                return 0
        elif game_rounds - self._second_lucky_round == 1:
            return 1
        else:
            self._first_lucky_round = None
            self._second_lucky_round = None
            return 0

    def round_win_reward(self):
        self._rounds_won += 1
        self._exp += 3
        if self._exp >= 19:
            self._especial_endurance = True

    def update_games_won(self):
        self._games_won += 1

    def reset_exp(self):
        self._exp = 10

    def get_staked_score(self):
        return self._ultra_stacket_individual_score

    def __str__(self):
        return f"Gender: {self._gender},Resistencia: {self._max_endurance}, Rondas individuales Ganadas: {self._rounds_won}, juegos Individuales Ganados: {self._games_won}"
