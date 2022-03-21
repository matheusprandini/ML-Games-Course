from tensorflow.keras import *

from neural_networks.nn_model import NnModel


class MlpBaseline(NnModel):

    model_mode = 'MLP'

    def build(self, input_shape, output_neurons):
        self.model = Sequential()
        self.model.add(layers.Dense(1024, activation='relu', input_shape=input_shape))
        self.model.add(layers.Dense(1024, activation='relu'))
        self.model.add(layers.Dense(output_neurons, activation='sigmoid'))

        self.model.summary()
