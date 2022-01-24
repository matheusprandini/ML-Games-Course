import abc
import os


class Agent(object):

    def __init__(self, name):
        self.name = name
        self.actions = [0, 1, 2, 3]

    @abc.abstractmethod
    def choose_action(self, game_state):
        raise NotImplementedError