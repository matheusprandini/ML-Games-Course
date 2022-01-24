import os

import numpy as np
from Agents import Agent


class RandomAgent(Agent):

    def __init__(self):
        super().__init__(
            name=os.getenv('AGENT_NAME', 'Random Agent')
        )

    def choose_action(self, _):
        return np.random.randint(0, len(self.actions), size=1)[0]
