import os

import numpy as np
from agents.agent import Agent
from enums.action import Action


class RandomAgent(Agent):

    def __init__(self):
        super().__init__(
            name=os.getenv('AGENT_NAME', 'Random Agent')
        )

    def choose_action(self, _):
        return np.random.randint(0, len(Action), size=1)[0]
