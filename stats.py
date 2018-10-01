class Stats():

    def __init__(self):

        self.reset_stats()

        self.game_active=False

        self.player_score=0
        self.enemy_score=0

        self.max_score=7
    def reset_stats(self):
        self.player_score = 0
        self.enemy_score = 0