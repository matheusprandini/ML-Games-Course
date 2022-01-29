import logging
import os
import cv2
import numpy as np

from pathlib import Path

from enums.action import Action
from enums.color_mode import ColorMode

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

class DataCollector():

    filepath = os.getenv('COLLECTED_DATA_PATH', 'extracted_data/data.npy')
    color_mode = os.getenv('COLOR_MODE', 'RGB')
    frame_size = os.getenv('FRAME_SIZE', (100, 100))
    data = []

    @classmethod
    def collect(cls, game, agent, number_tries):
        for _ in range(number_tries):
            current_frame, *_ = cls.start_game(game)

            game_over = False
            while not game_over:
                preprocessed_current_frame = cls.preprocess_frame(current_frame) 
                action = agent.choose_action(preprocessed_current_frame)
                current_frame, environment_action, _, game_over, score = game.step(action)
                cls.data.append([preprocessed_current_frame, environment_action])
                logger.info(f'Action: {Action(action).name} - Environment Action: {Action(environment_action).name}')
            logger.info(f'Game Over - Score: {score}')

        cls.save_data()

    @classmethod
    def start_game(cls, game):
        game.reset()
        return game.step(Action.NOTHING.value)

    @classmethod
    def preprocess_frame(cls, frame):
        if cls.color_mode.upper() == ColorMode.RGB.value:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        elif cls.color_mode.upper() == ColorMode.GRAYSCALE.value:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame = cv2.resize(frame, cls.shape)
        return frame

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
