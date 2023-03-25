from archer import Archer


class Team(list):
    team_score = 0

    def __init__(self):
        self.team = [Archer(), Archer(), Archer(), Archer(), Archer()]

    def update_team_score(self, score):
        self.team_score += score

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.team):
            raise StopIteration
        result = self.team[self.index]
        self.index += 1
        return result
