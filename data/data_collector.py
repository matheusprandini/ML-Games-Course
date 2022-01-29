import logging
import os
import numpy as np

from pathlib import Path
from data.data_handler import DataHandler

from enums.action import Action

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(os.getenv('LOG_LEVEL', 'INFO'))

class DataCollector():

    filepath = os.getenv('COLLECTED_DATA_PATH', 'extracted_data/data.npy')
    color_mode = os.getenv('COLOR_MODE', 'RGB')
    frame_size = (
        int(os.getenv('FRAME_HEIGHT', 100)),
        int(os.getenv('FRAME_WIDTH', 100))
    )
    data = []

    @classmethod
    def collect(cls, game, agent, number_tries):
        scores = []
        for i in range(number_tries):
            current_frame, *_ = cls.start_game(game)

            game_over = False
            while not game_over:
                preprocessed_current_frame = DataHandler.preprocess_frame(current_frame) 
                action = agent.choose_action(preprocessed_current_frame)
                current_frame, environment_action, _, game_over, score = game.step(action)
                cls.data.append([preprocessed_current_frame, environment_action])
                logger.debug(f'Action: {Action(action).name} - Environment Action: {Action(environment_action).name}')
            logger.info(f'Game {i+1} - Score: {score}')
            scores.append(score)
        cls.generate_stats(scores)
        cls.save_data()

    @classmethod
    def start_game(cls, game):
        game.reset()
        return game.step(Action.NOTHING.value)

    @classmethod
    def save_data(cls):
        logger.info('Saving Data')
        cls.create_directory()
        with open(cls.filepath, 'wb') as output_file:
            np.save(output_file, cls.data)

    @classmethod
    def create_directory(cls):
        directory = Path(cls.filepath).parent
        directory.mkdir(parents=True, exist_ok=True) 

    @classmethod
    def generate_stats(cls, scores):
        scores = np.array(scores)
        logger.info(
            f'Total Score: {np.sum(scores)} - Max Score: {np.max(scores)}'
            f' - Min Score: {np.min(scores)} - Mean Score: {np.mean(scores)} - Std Score: {np.std(scores)}'
        )
