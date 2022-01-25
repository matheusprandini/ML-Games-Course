import logging
import os

import pygame
from pygame.locals import *
from agents.agent import Agent


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
                    return 0
                elif event.key == K_RIGHT:
                    return 1
                elif event.key == K_UP:
                    return 2
                elif event.key == K_DOWN:
                    return 3
        return -1
