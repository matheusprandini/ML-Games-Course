import logging
import os

import numpy as np
from agents.neural_network_agent import NeuralNetworkAgent
from data.data_collector import DataCollector
from data.data_handler import DataHandler

from enums.action import Action
from games.game import Game
from games.catch_game import CatchGame
from games.snake_game import SnakeGame
from agents.random_agent import RandomAgent
from agents.human_agent import HumanAgent
from neural_networks.cnn_baseline import CnnBaseline
from neural_networks.mlp_baseline import MlpBaseline


logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(os.getenv('LOG_LEVEL', 'INFO'))

games_translator = {
    'Catch': CatchGame(),
    'Snake': SnakeGame()
}

agents_translator = {
    'Random': RandomAgent(),
    'Human': HumanAgent(),
    'NeuralNetwork': NeuralNetworkAgent()
}

models_translator = {
    'MLP': MlpBaseline(),
    'CNN': CnnBaseline()
}

def play(game, agent, num_tries):
    logger.info(f'----- Starting Execution -----')

    if type(agent) == NeuralNetworkAgent:
        agent.load()

    for i in range(num_tries):
        logger.info(f'Game: {game.name} - Agent: {agent.name} - Try: {i}')
        game.reset()
        frame = game.get_frame()
        game_over = False
        while not game_over:
            action = agent.choose_action(frame)
            frame, environment_action, reward, game_over, score = game.step(action)
            logger.info(f"Action: {Action(environment_action).name} - Reward: {reward} - Game Over: {game_over} - Score: {score}")

def collect_data(game, agent, num_tries):
    logger.info(f'----- Collecting Data -----')
    DataCollector.collect(game, agent, num_tries)

def prepare_data():
    logger.info(f'----- Preparing Data -----')
    DataHandler.prepare()

def train_model(game_name):
    logger.info(f'----- Training Model -----')

    model_mode = os.getenv('MODEL_NODE').upper()
    color_mode = os.getenv('COLOR_MODE').upper()
    frame_height = int(os.getenv('FRAME_HEIGHT'))
    frame_width = int(os.getenv('FRAME_WIDTH'))

    num_output_neurons = 3 if game_name.upper() == 'CATCH' else 4
    num_channels = 1 if color_mode == 'GRAYSCALE' else 3
    input_shape = (frame_height*frame_width*num_channels,) if model_mode == 'MLP' else (frame_height, frame_width, num_channels)

    data = list(np.load(DataHandler.dest_filepath, allow_pickle=True))

    model = models_translator[model_mode]
    model.build(input_shape, num_output_neurons)
    model.training(data)

def process():
    game: Game = games_translator[os.getenv('GAME', 'Catch')]
    agent = agents_translator[os.getenv('AGENT', 'Random')]
    num_tries = int(os.getenv('NUM_TRIES', 10))
    type = os.getenv('TYPE', 'PLAY')

    if type == 'PLAY':
        play(game, agent, num_tries)
    elif type == 'COLLECT':
        collect_data(game, agent, num_tries)
    elif type == 'PREPARE':
        prepare_data()
    elif type == 'TRAIN':
        train_model(game.name)

process()
