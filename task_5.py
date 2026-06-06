class Results:
    def __init__(self, victories, draws, losses):
        self.victories = victories
        self.draws = draws
        self.losses = losses


class Football(Results):
    def __init__(self, victories, draws, losses):
        super().__init__(victories, draws, losses)

    def number_of_football_wins(self):
        print(f"Футбольных побед: {self.victories}")

    def number_of_football_draws(self):
        print(f"Футбольных ничьих: {self.draws}")

    def number_of_football_losses(self):
        print(f"Футбольных поражений: {self.losses}")

    def total_football_points(self):
        print(f"Общее количество очков: {self.victories*3+self.draws}")


class Hockey(Results):
    def __init__(self, victories, draws, losses):
        super().__init__(victories, draws, losses)

    def number_of_hockey_wins(self):
        print(f"Хоккейных побед: {self.victories}")

    def number_of_hockey_draws(self):
        print(f"Хоккейных ничьих: {self.draws}")

    def number_of_hockey_losses(self):
        print(f"Хоккейных поражений: {self.losses}")

    def total_hockey_points(self):
        print(f"Общее количество очков: {self.victories*2+self.draws}")


football_team = Football(2, 2, 2)
hockey_team = Hockey(2, 2, 2)
all_methods = [
    football_team.number_of_football_wins,
    football_team.number_of_football_draws,
    football_team.number_of_football_losses,
    football_team.total_football_points,
    hockey_team.number_of_hockey_wins,
    hockey_team.number_of_hockey_draws,
    hockey_team.number_of_hockey_losses,
    hockey_team.total_hockey_points,
]


for method in all_methods:
    method()    