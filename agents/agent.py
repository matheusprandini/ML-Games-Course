import abc


class Agent(object):

    def __init__(self, name):
        self.name = name

    @abc.abstractmethod
    def choose_action(self, game_state):
        raise NotImplementedError