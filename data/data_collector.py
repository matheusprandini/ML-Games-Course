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
    mode = "RGB"
    shape = (100, 100)
    data = []

    @classmethod
    def collect(cls, game, agent, number_tries):
        for _ in range(number_tries):
            game_over = False
            game.reset()
            action = Action.NOTHING.value

            while not game_over:
                current_frame, _, game_over, score = game.step(action)
                preprocessed_current_frame = cls.preprocess_frame(current_frame) 
                action = agent.choose_action(preprocessed_current_frame)
                cls.data.append([preprocessed_current_frame, action])
                logger.info(f'Action: {Action(action).name}')
            logger.info(f'Game Over - Score: {score}')

        cls.save_data()

    @classmethod
    def preprocess_frame(cls, frame):
        if cls.mode.upper() == ColorMode.RGB:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        elif cls.mode.upper() == ColorMode.GRAYSCALE:
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
