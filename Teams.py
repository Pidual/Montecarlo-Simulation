from archer import Archer


class Team(list):
    team_score = 0
    round_wins = 0

    def __init__(self):
        self.team = [Archer(), Archer(), Archer(), Archer(), Archer()]

    def update_team_score(self, score):
        self.team_score += score

    def update_team_wins(self):
        self.round_wins += 1

    def increment_round_wins(self):
        self.round_wins += 1

    def __str__(self):
        return f"Puntaje Equipo: {self.team_score}, Wins: {self.round_wins}"

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.team):
            raise StopIteration
        result = self.team[self.index]
        self.index += 1
        return result
