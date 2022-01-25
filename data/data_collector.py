import logging
import os
import numpy as np

from pathlib import Path

from enums.action import Action

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

class DataCollector():

    filepath = os.getenv('COLLECTED_DATA_PATH', 'extracted_data/data.npy')
    data = []

    @classmethod
    def collect(cls, game, agent, number_tries):
        for _ in range(number_tries):
            game_over = False
            game.reset()
            current_frame = game.get_frame()

            while not game_over:
                action = agent.choose_action(current_frame)
                cls.data.append([current_frame, action])
                current_frame, _, game_over, _ = game.step(action)
                logger.info(f'Action: {Action(action).name}')
                
        cls.save_data()

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
