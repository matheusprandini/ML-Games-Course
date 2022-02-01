import os

import numpy as np

from agents.agent import Agent
from data.data_handler import DataHandler
from tensorflow.keras.models import load_model


class NeuralNetworkAgent(Agent):

    def __init__(self):
        self.model = load_model(os.getenv('MODEL_NAME'))
        super().__init__(
            name=os.getenv('AGENT_NAME', 'NN Agent')
        )

    def choose_action(self, frame):
        preprocessed_frame = DataHandler.preprocess_frame(frame)
        preprocessed_frame = preprocessed_frame.reshape(-1, 32*32)
        action = np.argmax(self.model.predict(preprocessed_frame))
        return action
