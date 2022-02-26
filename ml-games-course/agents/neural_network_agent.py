import os

import numpy as np

from agents.agent import Agent
from data.data_handler import DataHandler
from tensorflow.keras.models import load_model


class NeuralNetworkAgent(Agent):

    def __init__(self):
        super().__init__(
            name=os.getenv('AGENT_NAME', 'NN Agent')
        )

    def load(self):
        self.model = load_model(os.getenv('MODEL_NAME'))
        self.mode = os.getenv('MODEL_MODE', 'MLP')
        self.color = os.getenv('COLOR_MODE', 'GRAYSCALE')

    def convert_frame_shape(self, frame):
        frame_shape = frame.shape
        converted_frame_shape = frame_shape + (1,) if self.color == 'GRAYSCALE' else frame_shape
        converted_frame_shape = (-1,) + (np.prod(converted_frame_shape),) if self.mode == 'MLP' else (-1,) + converted_frame_shape
        return converted_frame_shape

    def choose_action(self, frame):
        preprocessed_frame = DataHandler.preprocess_frame(frame)
        preprocessed_frame = preprocessed_frame.reshape(self.convert_frame_shape(preprocessed_frame)) 
        action = np.argmax(self.model.predict(preprocessed_frame))
        return action
