import os
import cv2
import numpy as np
import logging

from enums.color_mode import ColorMode

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(os.getenv('LOG_LEVEL', 'INFO'))

class DataHandler():

    source_filepath = os.getenv('COLLECTED_DATA_PATH', 'extracted_data/data.npy')
    dest_filepath = os.getenv('PREPARED_DATA_PATH', 'prepared_data/data.npy')

    @classmethod
    def prepare_data(cls):
        data = list(np.load(cls.source_filepath))
        cls.validate_data(data)

    def validate_data(cls, data):
        for example in data:
            img = example[0]
            output_move = example[1]
            output_action = example[2]
            cv2.imshow('test', img)
            print(output_move, ' ', output_action)
            if cv2.waitKey(25) & 0xFF == ord('q'): # Destroy all images when close the script
                cv2.destroyAllWindows()
                break

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
