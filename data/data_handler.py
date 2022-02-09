import os
import cv2
import numpy as np
import logging

import pandas as pd
from pathlib import Path

from enums.color_mode import ColorMode

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(os.getenv('LOG_LEVEL', 'INFO'))

class DataHandler():

    source_filepath = os.getenv('COLLECTED_DATA_PATH', 'extracted_data/data.npy')
    dest_filepath = os.getenv('PREPARED_DATA_PATH', 'prepared_data/data.npy')
    color_mode = os.getenv('COLOR_MODE', 'RGB')
    frame_size = (
        int(os.getenv('FRAME_HEIGHT', 100)),
        int(os.getenv('FRAME_WIDTH', 100))
    )
    prepared_data = []

    @classmethod
    def prepare(cls):
        data = list(np.load(cls.source_filepath, allow_pickle=True))
        cls.balance_data(data)
        cls.save_data(cls.dest_filepath, cls.prepared_data)

    @classmethod
    def balance_data(cls, data):
        df = pd.DataFrame(data, columns=['frame_representation', 'action'])
        num_examples_of_action_with_less_data = df.groupby(['action']).count().min().iloc[0]

        unique_actions = df['action'].unique()
        for action in unique_actions:
            chosen_indexes = np.random.choice(
                df[df.action == action].index.values,
                num_examples_of_action_with_less_data
            )
            examples = df.loc[chosen_indexes].values.tolist()
            cls.prepared_data.extend(examples)

    @classmethod
    def apply_pixel_wise_normalization(cls, frame):
        return (frame.astype('float32') / 255.0)

    @classmethod
    def preprocess_frame(cls, frame):
        preprocessed_frame = cls.convert_frame_color(frame)
        preprocessed_frame = cls.resize_frame(preprocessed_frame)
        preprocessed_frame = cls.apply_pixel_wise_normalization(preprocessed_frame)
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
    def save_data(cls, filepath, data):
        logger.info('Saving Data')
        cls.create_directory(filepath)
        with open(filepath, 'wb') as output_file:
            np.save(output_file, data)

    @classmethod
    def create_directory(cls, filepath):
        directory = Path(filepath).parent
        directory.mkdir(parents=True, exist_ok=True) 
