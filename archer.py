import random


class Archer:
    gender = None  # 0 para hombre y 1 para mujer
    max_endurance = None  # la resistencia que es definitiva
    endurance = None  # 35 ± 10
    exp = None  # Entero 10
    luck = None  # 1 a 3
    individual_score = None  # Puntaje individual
    first_lucky_round = None
    second_lucky_round = None
    last_lucky_round = None

    def __init__(self):  # aca para que se creen pseudo aletoriamente
        # Escoje el genero con el metodo montecarlo 0.5 de chance cada genero
        ri = random.random()
        if ri < 0.5:
            self.gender = 0
        else:
            self.gender = 1
        # Resistencia 35 ± 10
        if ri < 0.5:
            self.endurance = 35 - random.randint(1, 10)
        else:
            self.endurance = 35 + random.randint(1, 10)
        # Flotante XD
        self.luck = random.uniform(1, 3)
        self.exp = 10
        self.individual_score = 0
        self.max_endurance = self.endurance

    def update_individual_score(self, score):
        self.individual_score += score

    def restore_endurance(self):
        self.endurance = self.max_endurance

    def recalculate_luck(self):
        self.luck = random.uniform(1, 3)

    # Acutualiza la racha de lanzamientos extra al llegar a 3 se reinicia
    def update_streak(self, round):
        if self.first_lucky_round is None:
            self.first_lucky_round = round
            return 0
        elif self.second_lucky_round is None:
            if round - self.first_lucky_round == 1:
                self.second_lucky_round = round
                return 0
            else:
                self.first_lucky_round = round
                return 0
        elif round - self.second_lucky_round == 1:
            return 1
        else:
            self.first_lucky_round = None
            self.second_lucky_round = None
            return 0
