import logging
import os
import cv2
import numpy as np

from pathlib import Path

from enums.action import Action
from enums.color_mode import ColorMode

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
        for i in range(number_tries):
            current_frame, *_ = cls.start_game(game)

            game_over = False
            while not game_over:
                preprocessed_current_frame = cls.preprocess_frame(current_frame) 
                action = agent.choose_action(preprocessed_current_frame)
                current_frame, environment_action, _, game_over, score = game.step(action)
                cls.data.append([preprocessed_current_frame, environment_action])
                logger.debug(f'Action: {Action(action).name} - Environment Action: {Action(environment_action).name}')
            logger.info(f'Game {i} - Score: {score}')

        cls.save_data()

    @classmethod
    def start_game(cls, game):
        game.reset()
        return game.step(Action.NOTHING.value)

    @classmethod
    def preprocess_frame(cls, frame):
        preprocessed_frame = cls.convert_frame_color(frame)
        preprocessed_frame = cls.resize_frame(preprocessed_frame)
        return preprocessed_frame

    @classmethod
    def convert_frame_color(cls, frame):
        logger.debug(f'Converting Frame Color to {cls.color_mode}')
        if cls.color_mode.upper() == ColorMode.RGB.value:
            return cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        elif cls.color_mode.upper() == ColorMode.GRAYSCALE.value:
            return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        else:
            return frame

    @classmethod
    def resize_frame(cls, frame):
        logger.debug(f'Resizing Frame to {cls.frame_size}')
        return cv2.resize(frame, cls.frame_size)

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
