import logging
import os

from games.game import Game
from games.catch_game import CatchGame
from games.snake_game import SnakeGame
from agents.random_agent import RandomAgent
from agents.human_agent import HumanAgent


logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

games_translator = {
    'Catch': CatchGame(),
    'Snake': SnakeGame()
}

agents_translator = {
    'Random': RandomAgent(),
    'Human': HumanAgent()
}

def process():
    game: Game = games_translator[os.getenv('GAME', 'Catch')]
    agent = agents_translator[os.getenv('AGENT', 'Random')]
    num_tries = int(os.getenv('NUM_TRIES', 10))

    logger.info(f'----- Starting Execution -----')

    for i in range(num_tries):
        logger.info(f'Game: {game.name} - Agent: {agent.name} - Try: {i}')
        game.reset()
        frame = game.get_frame()
        game_over = False
        while not game_over:
            action = agent.choose_action(frame)
            frame, reward, game_over, score = game.step(action)
            logger.info(f"Action: {action} - Reward: {reward} - Game Over: {game_over} - Score: {score}")

process()
