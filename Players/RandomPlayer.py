import os

import numpy as np
from Players import Player


class RandomPlayer(Player):

    def __init__(self):
        super().__init__(
            name=os.getenv('PLAYER_NAME', 'Random Player')
        )

    def choose_action(self, _):
        return np.random.randint(0, len(self.actions), size=1)[0]
