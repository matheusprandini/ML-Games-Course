import os

import pygame
from pygame.locals import *
from agents.agent import Agent
from enums.action import Action


class HumanAgent(Agent):

    def __init__(self):
        super().__init__(
            name=os.getenv('AGENT_NAME', 'Human Agent')
        )

    def choose_action(self, _):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    return Action.LEFT.value
                elif event.key == K_RIGHT:
                    return Action.RIGHT.value
                elif event.key == K_UP:
                    return Action.UP.value
                elif event.key == K_DOWN:
                    return Action.DOWN.value
        return -1
